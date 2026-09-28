"""Passo final (idempotente) sobre TODAS as páginas publicadas: segurança, URLs limpas, SEO e peso da página.
O GitHub Pages não deixa configurar cabeçalhos HTTP, então a política de segurança vai em <meta>.
  - CSP (sem terceiros: fontes e scripts são do próprio site), referrer, base-uri/form-action/object-src travados
  - canonical + hreflang absolutos (o Lighthouse rejeita hreflang relativo)
  - Google Fonts -> shared/fonts.css (fontes próprias, ver selfhost_fonts.py)
  - links para a pasta (…/silverfist/) em vez de …/silverfist/index.html
  - página inicial: ícones em base64 (200 KB de HTML) viram arquivos em shared/ico/, imagens abaixo da dobra ficam lazy
Uso: python tools/harden.py   (os scripts de build chamam run() no fim)"""
import hashlib, re, base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://genezera.github.io/grimorio-de-builds/'
CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline' 'inline-speculation-rules'; style-src 'self' 'unsafe-inline'; "
       "img-src 'self' data: https://web.poecdn.com https://cdn.poe2db.tw; font-src 'self'; connect-src 'self'; "
       "object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests")
SEC = ('<meta http-equiv="Content-Security-Policy" content="%s">\n<meta name="referrer" content="strict-origin-when-cross-origin">\n' % CSP)
GFONTS = re.compile(r'<link rel="preconnect" href="https://fonts\.(?:googleapis|gstatic)\.com"(?: crossorigin)?>\s*|<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2[^"]*">\s*')
HREFLANG = re.compile(r'<link rel="(?:alternate|canonical)"[^>]*>\s*')


def _lum(rgb):
    f = lambda c: c / 12.92 if c <= .03928 else ((c + .055) / 1.055) ** 2.4
    r, g, b = (f(x / 255) for x in rgb)
    return .2126 * r + .7152 * g + .0722 * b


def _contrast(a, b):
    la, lb = _lum(a), _lum(b)
    return (max(la, lb) + .05) / (min(la, lb) + .05)


def _faint(m):
    """--faint (texto discreto) precisa de contraste >= 4.5:1 (WCAG AA) sobre os cards escuros (#1B1713); clareia mantendo o matiz."""
    import colorsys
    hexv = m.group(1); rgb = tuple(int(hexv[i:i + 2], 16) for i in (0, 2, 4))
    bg = (0x1b, 0x17, 0x13)
    if _contrast(rgb, bg) >= 4.6: return m.group(0)
    h, l, s_ = colorsys.rgb_to_hls(*(c / 255 for c in rgb))
    while _contrast(tuple(round(c * 255) for c in colorsys.hls_to_rgb(h, l, s_)), bg) < 4.6 and l < 1: l += .005
    return '--faint:#%02x%02x%02x' % tuple(round(c * 255) for c in colorsys.hls_to_rgb(h, l, s_))


FAINT = re.compile(r'--faint:\s*#([0-9a-fA-F]{6})')


def pages():
    out = []
    for p in sorted(ROOT.glob('*.html')) + sorted(ROOT.glob('*/index.html')) + sorted(ROOT.glob('*/en.html')):
        if p.parent.name in ('tools', 'docs', 'planilha', 'shared'): continue
        if 'shared/loader.js' in p.read_text(encoding='utf-8'): out.append(p)
    return out


def fonts_v():
    return hashlib.md5((ROOT / 'shared' / 'fonts.css').read_bytes()).hexdigest()[:8]


def versioned(m):
    f = ROOT / 'shared' / m.group(2)
    return '%s?v=%s' % (m.group(1), hashlib.md5(f.read_bytes()).hexdigest()[:8]) if f.exists() else m.group(0)


def extract_icons(h):
    ico = ROOT / 'shared' / 'ico'; ico.mkdir(exist_ok=True)
    def rep(m):
        data = base64.b64decode(m.group(2))
        name = hashlib.md5(data).hexdigest()[:10] + '.webp'
        f = ico / name
        if not f.exists(): f.write_bytes(data)
        return '%ssrc="shared/ico/%s"' % (m.group(1), name)
    return re.sub(r'(<img [^>]*?)src="data:image/webp;base64,([A-Za-z0-9+/=]+)"', rep, h)


def lazy_cards(h):
    n = [0]
    def rep(m):
        tag = m.group(0); n[0] += 1
        if 'loading=' in tag or 'fetchpriority=' in tag: return tag
        if n[0] <= 2: return tag.replace('<img ', '<img fetchpriority="high" ', 1)
        return tag.replace('<img ', '<img loading="lazy" ', 1)
    h = re.sub(r'<img class="asc"[^>]*>', rep, h)
    return re.sub(r'<img class="main-icon"(?![^>]*loading=)', '<img loading="lazy" class="main-icon"', h)


def clean_hrefs(h):
    def rep(m):
        pre, rest = m.group(1), m.group(2) or ''
        return 'href="%s%s"' % (pre or './', rest)
    return re.sub(r'href="((?:\.\./|[A-Za-z0-9_-]+/)*)index\.html((?:#|\?)[^"]*)?"', rep, h)


def harden(p):
    h0 = h = p.read_text(encoding='utf-8')
    d = p.parent.name if p.parent != ROOT else ''
    up = '../' if d else ''
    en = p.name == 'en.html'
    if 'Content-Security-Policy' not in h:
        h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + SEC, 1)
    h = HREFLANG.sub('', h)
    pt_url, en_url = BASE + (d + '/' if d else ''), BASE + (d + '/en' if d else 'en')
    seo = ('<link rel="canonical" href="%s"><link rel="alternate" hreflang="pt-BR" href="%s"><link rel="alternate" hreflang="en" href="%s"><link rel="alternate" hreflang="x-default" href="%s">\n'
           % (en_url if en else pt_url, pt_url, en_url, pt_url))
    h = re.sub(r'(<meta name="viewport"[^>]*>)', lambda m: m.group(1) + '\n' + seo, h, count=1)
    if GFONTS.search(h):
        h = GFONTS.sub('', h)
        h = re.sub(r'(<link rel="stylesheet" href="%sshared/loader\.css)' % re.escape(up), lambda m: '<link rel="stylesheet" href="%sshared/fonts.css?v=%s">' % (up, fonts_v()) + m.group(1), h, count=1) \
            if 'shared/loader.css' in h else h
        if 'shared/fonts.css' not in h:
            h = h.replace('</head>', '<link rel="stylesheet" href="%sshared/fonts.css?v=%s">\n</head>' % (up, fonts_v()), 1)
    if not d:
        h = extract_icons(h)
        h = lazy_cards(h)
    h = clean_hrefs(h)
    h = FAINT.sub(_faint, h)
    h = re.sub(r'(shared/([\w.-]+))\?v=[0-9a-f]{8}', versioned, h)   # ?v= sempre em dia com o conteúdo do arquivo (cache de 10 min do GitHub Pages)
    if h != h0: p.write_text(h, encoding='utf-8', newline='\n')
    return h != h0


def run():
    for css in ('poe2.css', 'landing.css', 'rites.css'):
        f = ROOT / 'shared' / css; t = f.read_text(encoding='utf-8'); t2 = FAINT.sub(_faint, t)
        if t2 != t: f.write_text(t2, encoding='utf-8', newline='\n')
    n = sum(harden(p) for p in pages())
    urls = []
    for p in pages():
        d = p.parent.name if p.parent != ROOT else ''
        urls.append(BASE + (d + '/' if d else '') if p.name == 'index.html' else BASE + (d + '/' if d else '') + 'en')
    smap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join('<url><loc>%s</loc></url>\n' % u for u in sorted(set(urls))) + '</urlset>\n'
    (ROOT / 'sitemap.xml').write_text(smap, encoding='utf-8', newline='\n')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: %ssitemap.xml\n' % BASE, encoding='utf-8', newline='\n')
    print('harden: %d páginas atualizadas' % n)


if __name__ == '__main__':
    run()
