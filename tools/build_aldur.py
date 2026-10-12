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
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#071419">
<link rel="icon" href="../shared/aldur-mark.svg" type="image/svg+xml">
<link rel="alternate" hreflang="pt-BR" href="index.html"><link rel="alternate" hreflang="en" href="en.html">
<link rel="stylesheet" href="../shared/aldur.css?v={asset_version('aldur.css')}"><link rel="stylesheet" href="../shared/fonts.css?v={asset_version('fonts.css')}"><link rel="stylesheet" href="../shared/loader.css?v={asset_version('loader.css')}"><script src="../shared/loader.js?v={asset_version('loader.js')}"></script>
</head><body><a class="skip" href="#challenges">{'Ir para desafios' if current == 'pt' else 'Skip to challenges'}</a><div class="world" aria-hidden="true"><canvas id="embers"></canvas></div>
<header class="site-header"><a class="back" href="{home}">← {'Grimório de Builds' if current == 'pt' else 'Build Grimoire'}</a><nav class="site-nav" aria-label="{'Guias de liga' if current == 'pt' else 'League guides'}"><a href="../rites/{'en.html' if current == 'en' else ''}">Forbidden Rites</a><a href="#challenges">{'Challenges' if current == 'pt' else 'Challenges'}</a></nav><nav class="language" aria-label="Idioma / Language"><a href="./" {'aria-current="page"' if current == 'pt' else ''}>PT</a><a href="en.html" {'aria-current="page"' if current == 'en' else ''}>EN</a></nav></header>
<main id="app"></main><noscript><p class="noscript">JavaScript is required for the interactive checklist.</p></noscript>
<script src="../shared/aldur.js?v={asset_version('aldur.js')}" defer></script></body></html>
''', encoding='utf-8', newline='\n')

harden.run()
print('aldur ok')
