# -*- coding: utf-8 -*-
"""Build the bilingual Runes of Aldur challenge guide."""
from pathlib import Path
from enhance import asset_version
import harden

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'aldur'
OUT.mkdir(exist_ok=True)

for lang, file, title, desc in (
    ('pt-BR', 'index.html', 'Runes of Aldur · Guia das Challenges', 'Acompanhe as oito challenges de Runes of Aldur em Path of Exile 2, com checklist e progresso salvo.'),
    ('en', 'en.html', 'Runes of Aldur · Challenge Guide', 'Track the eight Runes of Aldur challenges in Path of Exile 2 with checklists and saved progress.'),
):
    home = '../' if lang == 'pt-BR' else '../en.html'
    current = 'pt' if lang == 'pt-BR' else 'en'
    (OUT / file).write_text(f'''<!doctype html>
<html lang="{lang}" data-page="aldur"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#050d0f">
<link rel="icon" href="../shared/aldur-mark.svg" type="image/svg+xml">
<link rel="alternate" hreflang="pt-BR" href="index.html"><link rel="alternate" hreflang="en" href="en.html">
<link rel="stylesheet" href="../shared/fonts.css?v={asset_version('fonts.css')}"><link rel="stylesheet" href="../shared/rites.css?v={asset_version('rites.css')}"><link rel="stylesheet" href="../shared/aldur.css?v={asset_version('aldur.css')}"><link rel="stylesheet" href="../shared/loader.css?v={asset_version('loader.css')}"><script src="../shared/loader.js?v={asset_version('loader.js')}"></script>
</head><body><a class="skip" href="#challenges">{'Ir para: Challenges' if current == 'pt' else 'Jump to: Challenges'}</a>
<div class="void" aria-hidden="true"><div class="totem-bg"></div><div class="fog f1"></div><div class="fog f2"></div><canvas id="embers"></canvas><div class="vignette"></div></div>
<header class="top"><a class="homelink" href="{home}">← {'Builds' if current == 'pt' else 'Builds'}</a><a class="sibling" href="../rites/{'en.html' if current == 'en' else ''}">✦ Forbidden Rites</a><nav class="lang" aria-label="Idioma / Language"><a href="index.html" {'aria-current="page"' if current == 'pt' else ''}>PT</a><a href="en.html" {'aria-current="page"' if current == 'en' else ''}>EN</a></nav></header>
<main id="app"></main><noscript><p style="padding:24px;color:#e9dcc0">JavaScript</p></noscript>
<script src="../shared/aldur.js?v={asset_version('aldur.js')}" defer></script></body></html>
''', encoding='utf-8', newline='\n')

harden.run()
print('aldur ok')
