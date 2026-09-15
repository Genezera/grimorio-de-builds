# A Trilha do Mighty Silverfist · The Mighty Silverfist Trail

Guia interativo **Spirit Walker / Mighty Silverfist (Zoo Chober Chaber)** para Path of Exile 2 — patch 0.5.5, liga Forbidden Rites. Baseado no guia do Mattjestic, com explicações de cada gem, support, item, unique e passiva, do nível 1 ao 100, em modo barato e completo.

Interactive **Spirit Walker / Mighty Silverfist (Chober Chaber zoo)** guide for Path of Exile 2 — patch 0.5.5, Forbidden Rites league. Built on Mattjestic's guide, with explanations for every gem, support, item, unique and passive from level 1 to 100, in budget and full mode.

| Página / Page | Idioma / Language |
|---|---|
| `index.html` | Português (BR) |
| `en.html` | English |

O botão **PT / EN** no topo troca de idioma; o progresso (nível, modo, checklists, zoo) é compartilhado entre as duas versões.
The **PT / EN** switch at the top changes language; progress (level, mode, checklists, zoo) is shared between both versions.

---

## Publicar no GitHub Pages / Publish on GitHub Pages

1. Crie um repositório no GitHub (ex.: `trilha-silverfist`) · Create a GitHub repository.
2. Nesta pasta / In this folder:

   ```bash
   git init
   git add .
   git commit -m "Trilha do Silverfist"
   git branch -M main
   git remote add origin https://github.com/SEU-USUARIO/trilha-silverfist.git
   git push -u origin main
   ```

3. No GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)` → Save**.
4. Em ~1 minuto o site fica em / In about a minute the site is live at:
   `https://SEU-USUARIO.github.io/trilha-silverfist/` (PT) e `.../en.html` (EN).

O site é 100% estático (HTML + JS). Também funciona abrindo `index.html` direto no navegador.
The site is fully static (HTML + JS). It also works by opening `index.html` directly in a browser.

## Estrutura / Structure

```
index.html            app em português
en.html               app in English
assets/assets.js      árvore de passivas, ícones e sets (compartilhado) · tree, icons, sets (shared)
planilha/             planilha Excel completa · full Excel workbook (PT)
tools/                scripts para regenerar tudo · scripts to rebuild everything
```

## Regenerar / Rebuild (opcional)

Requer Python 3 com `openpyxl` e `Pillow`.

```bash
cd tools
python build_assets.py     # assets.json (árvore, ícones, sets) — usa dl/, tree.json, iconcache/
python build_site.py ..    # gera ../index.html, ../en.html e ../assets/assets.js
python build_xlsx.py       # gera out.xlsx
```

- Dados da build: `tools/chober.py` (sobre `meta.py` e `data.py`).
- Tradução: `tools/i18n/en_*.json` (textos dos dados) e `tools/ui_en.py` (textos da interface).

## Fontes / Sources

Mattjestic (Mobalytics), imortilize (Mobalytics), Zizaran (Maxroll), poe.ninja, PoE2DB e dados da árvore do Path of Building (PoE2). Preços da liga são um retrato do momento da pesquisa · League prices are a snapshot from research time.

Projeto de fã, sem vínculo com a Grinding Gear Games. Path of Exile é marca da Grinding Gear Games.
Fan project, not affiliated with Grinding Gear Games.
