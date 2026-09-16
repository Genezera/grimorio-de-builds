"""Shared, language-independent UI layered onto both generated build guides."""
from pathlib import Path

def enhance(template, lang, build):
    css = (Path(__file__).resolve().parents[1] / 'shared' / 'guide.css').read_text(encoding='utf-8')
    template = template.replace('</style>', '\n' + css + '\n</style>', 1)
    template = template.replace('<nav class="tabs" role="tablist" id="tabs"></nav>', '<div id="navigator"><div id="guideTools"></div><div id="navGroups"></div><nav class="tabs" role="tablist" id="tabs"></nav></div>\n<div id="readingGuide"></div>\n<section class="view" id="v-craft"></section>')
    marker = '/* ------------------------------------------------ boot */'
    assert marker in template
    template = template.replace(marker, '</script>\n<script src="../shared/craft-data.js"></script>\n<script src="../shared/craft-detail.js"></script>\n<script src="../shared/craft.js"></script>\n<script src="../shared/weights.js"></script>\n<script src="../shared/guide.js"></script>\n<script>\n' + marker, 1)
    return template
