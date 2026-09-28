"""Baixa as fontes do Google Fonts usadas pelas páginas e gera shared/fonts.css + shared/fonts/*.woff2 (só latin (cobre PT e EN)).
Uma vez rodado, o site não depende mais de fonts.googleapis.com / fonts.gstatic.com (mais rápido, sem terceiros, CSP mais estrita).
Uso: python tools/selfhost_fonts.py   (lê as URLs dos HTML publicados + tools/fonts_urls.txt)"""
import re, sys, urllib.request, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'shared' / 'fonts'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
KEEP = {'latin'}

def get(url, binary=False):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    return data if binary else data.decode('utf-8')

def collect_urls():
    urls = set()
    pat = re.compile(r'https://fonts\.googleapis\.com/css2\?[^"\'\s)<>]+')
    for p in list(ROOT.glob('*.html')) + list(ROOT.glob('*/index.html')) + list(ROOT.glob('*/en.html')):
        urls.update(u.replace('&amp;', '&') for u in pat.findall(p.read_text(encoding='utf-8')))
    f = ROOT / 'tools' / 'fonts_urls.txt'
    if f.exists(): urls.update(l.strip() for l in f.read_text(encoding='utf-8').splitlines() if l.strip())
    else: f.write_text('\n'.join(sorted(urls)) + '\n', encoding='utf-8')
    return sorted(urls)

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    faces = {}
    for url in collect_urls():
        css = get(url)
        for m in re.finditer(r'/\*\s*([a-z-]+)\s*\*/\s*@font-face\s*\{(.*?)\}', css, re.S):
            subset, body = m.group(1), m.group(2)
            if subset not in KEEP: continue
            g = lambda k: (re.search(k + r':\s*([^;]+);', body) or [None, ''])[1].strip()
            fam = g('font-family').strip('\'"'); style = g('font-style'); weight = g('font-weight'); rng = g('unicode-range')
            src = re.search(r'url\((https://[^)]+\.woff2)\)', body).group(1)
            key = (fam, style, weight, subset)
            if key in faces: continue
            faces[key] = (src, rng)
    files = {}
    css_out = ['/* gerado por tools/selfhost_fonts.py — não editar */']
    for (fam, style, weight, subset), (src, rng) in sorted(faces.items()):
        if src not in files:
            name = re.sub(r'[^a-z0-9]+', '-', fam.lower()).strip('-') + '-' + hashlib.md5(src.encode()).hexdigest()[:8] + '.woff2'
            (OUT / name).write_bytes(get(src, True))
            files[src] = name
        css_out.append('@font-face{font-family:"%s";font-style:%s;font-weight:%s;font-display:swap;src:url(fonts/%s) format("woff2")}'
                       % (fam, style, weight, files[src]))
    (ROOT / 'shared' / 'fonts.css').write_text('\n'.join(css_out) + '\n', encoding='utf-8')
    total = sum(p.stat().st_size for p in OUT.glob('*.woff2'))
    print(len(faces), 'faces,', len(files), 'arquivos,', total // 1024, 'KiB')

if __name__ == '__main__':
    main()
