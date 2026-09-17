"""Shared, language-independent UI layered onto both generated build guides."""
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1] / 'shared'
THEME_COLOR = {'silverfist': '#07080a', 'oracle': '#06060c', 'tactician': '#08080a', 'infernalist': '#0a0505', 'acolyte': '#07050b', 'pathfinder': '#060906', 'smith': '#09070a', 'martial': '#05070b'}

def asset_version(*names):
    """Hash curto do conteúdo: muda a URL sempre que o arquivo muda (o GitHub Pages guarda cache por 10 min)."""
    import hashlib
    h = hashlib.md5()
    for n in names: h.update((SHARED / n).read_bytes())
    return h.hexdigest()[:8]


def enhance(template, lang, build):
    css = '\n'.join((SHARED / name).read_text(encoding='utf-8') for name in ['guide.css', 'poe2.css', 'build-now.css'])
    template = template.replace('</style>', '\n' + css + '\n</style>', 1)
    # Palette before first paint (no flash): everything before </style> ends up in <head>.
    template = ('<script>document.documentElement.dataset.build=%r</script>\n<meta name="theme-color" content="%s">\n'
                % (build, THEME_COLOR.get(build, '#07080a'))
                + '<link rel="stylesheet" href="../shared/loader.css?v=%s"><script src="../shared/loader.js?v=%s"></script>\n'
                % (asset_version('loader.css'), asset_version('loader.js'))) + template
    template = template.replace('<nav class="tabs" role="tablist" id="tabs"></nav>', '<div id="navigator"><div id="guideTools"></div><div id="navGroups"></div><nav class="tabs" role="tablist" id="tabs"></nav></div>\n<div id="readingGuide"></div>\n<section class="view" id="v-craft"></section>')
    marker = '/* ------------------------------------------------ boot */'
    assert marker in template
    start = template.index('/* ------------------------------------------------ side panel */')
    end = template.index('/* ------------------------------------------------ views */', start)
    template = template[:start] + template[end:]
    scripts = ['craft-data.js', 'craft-detail.js', 'craft.js', 'weights.js', 'guide.js', 'poe2.js', 'build-now.js']
    tags = ''.join('<script src="../shared/%s?v=%s"></script>\n' % (s, asset_version(s)) for s in scripts)
    template = template.replace(marker, '</script>\n' + tags + '<script>\n' + marker, 1)
    return template
