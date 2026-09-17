"""Shared, language-independent UI layered onto both generated build guides."""
from pathlib import Path

SHARED = Path(__file__).resolve().parents[1] / 'shared'
THEME_COLOR = {'silverfist': '#07080a', 'oracle': '#06060c'}


def enhance(template, lang, build):
    css = '\n'.join((SHARED / name).read_text(encoding='utf-8') for name in ['guide.css', 'poe2.css', 'build-now.css'])
    template = template.replace('</style>', '\n' + css + '\n</style>', 1)
    # Palette before first paint (no flash): everything before </style> ends up in <head>.
    template = ('<script>document.documentElement.dataset.build=%r</script>\n<meta name="theme-color" content="%s">\n'
                % (build, THEME_COLOR.get(build, '#07080a'))) + template
    template = template.replace('<nav class="tabs" role="tablist" id="tabs"></nav>', '<div id="navigator"><div id="guideTools"></div><div id="navGroups"></div><nav class="tabs" role="tablist" id="tabs"></nav></div>\n<div id="readingGuide"></div>\n<section class="view" id="v-craft"></section>')
    marker = '/* ------------------------------------------------ boot */'
    assert marker in template
    start = template.index('/* ------------------------------------------------ side panel */')
    end = template.index('/* ------------------------------------------------ views */', start)
    template = template[:start] + template[end:]
    scripts = ['craft-data.js', 'craft-detail.js', 'craft.js', 'weights.js', 'guide.js', 'poe2.js', 'build-now.js']
    tags = ''.join('<script src="../shared/%s"></script>\n' % s for s in scripts)
    template = template.replace(marker, '</script>\n' + tags + '<script>\n' + marker, 1)
    return template
