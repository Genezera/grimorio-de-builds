# Build Grimoire — Path of Exile 2 build guides

Interactive, level 1 → 100 build guides for **Path of Exile 2** (patch 0.5.5, Forbidden Rites league), published as a static website.

**Live site:** https://genezera.github.io/grimorio-de-builds/

Each guide walks a build through the whole game: which skill and support gems to run at every level, which items to wear (a ranked list per slot, unique or rare, in a "cheap" and a "full" mode), which passive tree nodes to take and when, what each ascendancy point does, what to craft, and what to do when something goes wrong. The guide adapts to what the player ticks in **My character** (level, Spirit, items already owned). The site is available in Portuguese and English (**PT / EN** switch); this README is English only.

> Fan project, not affiliated with Grinding Gear Games. Path of Exile is a trademark of Grinding Gear Games.

---

## What this project is

A **build-guide generator plus the site it produces**. A small Python toolkit takes a build's source data (a Path of Building code, a Maxroll planner, a Mobalytics guide, poe.ninja ladder data), combines it with game data (gem tiers and descriptions, base items, passive tree, prices) and writes one self-contained, interactive HTML app per build. A weekly GitHub Actions job refreshes market data, re-ranks the builds, looks for strong builds that have no guide yet, rebuilds everything, audits the result and only publishes if the audit and the tests pass.

Design goals:

- **Followable from level 1.** The guide never asks for something the player cannot have yet (gem tier, item level, Spirit budget, tree connectivity are all checked against data).
- **Honest about what is measured and what is not.** Anything adapted or estimated says so in the guide (see [Limitations](#limitations)). Nothing is invented: levels, tiers and prices come from data or are labelled as approximate.
- **Static and portable.** No backend, no framework, no build step on the visitor's side. It also works when the files are opened straight from disk.

## The builds

| Guide | Name | Build | Source |
|---|---|---|---|
| `silverfist/` | **The Mighty Silverfist Trail** | Huntress · Spirit Walker — Mighty Silverfist companion zoo | Mattjestic, imortilize, Zizaran (Mobalytics / Maxroll) |
| `oracle/` | **The Oracle of Totems** | Druid · Oracle — Spell Totem | Lowepe (Mobalytics) |
| `hyperspeed/` | **Hyper Speed Monk** | Monk · Martial Artist — Hollow Palm (unarmed): Tempest Flurry + Staggering Palm + Falling Thunder | Ronarray (Mobalytics) |
| `tactician/` | **Grenade Tactician** | Mercenary · Tactician — Pin2Win Grenades | BlazeworksTV |
| `infernalist/` | **Infernal Pact** | Witch · Infernalist — Spark → Cast on Critical Comet, recoup and a luxury CoA version | Ignatius, kingkongor |
| `acolyte/` | **Chayula's Dream** | Monk · Acolyte of Chayula — Poisonburst Arrow, then Tornado Sprinkler + Archon of Chayula | Goratha (Maxroll) |
| `pathfinder/` | **Venom Trail** | Ranger · Pathfinder — poison bow → Corpsewade Decompose | Skadoosh |
| `smith/` | **Kitava's Forge** | Warrior · Smith of Kitava — Shield Wall + Avatar of Fire | Lexd (Mobalytics) |
| `martial/` | **Oil Barrage Teleport** | Monk · Martial Artist — Oil Barrage + Cast on Critical + Lightning Warp | havoc616 (Maxroll) + poe.ninja ladder |
| `shaman/` | **Mana Storm** | Druid · Shaman — Archmage Spark + Cast on Critical Comet | Top 10 Shamans by DPS on poe.ninja |
| `legionnaire/` | **Cleaving Thunder** | Mercenary · Gemling Legionnaire — Falling Thunder quarterstaff with Power Charges | poe.ninja Path of Building (level 96) |
| `whirling/` | **Frost Cyclone** | Mercenary · Gemling Legionnaire — Whirling Slash + Glacial Bolt (ice crossbow) | Phylaris POE (Mobalytics) |
| `twister/` | **Spear Twister** | Mercenary · Gemling Legionnaire — Spear Throw Twister | Maxroll Path of Building |
| `rites/` | **Forbidden Rites Challenges** | Forbidden Rites league guide — the 8 challenges (checklists, Omen planner, saved progress) | — |

Every guide has a Portuguese page (`index.html`) and an English page (`en.html`); the landing page (`/index.html`, `/en.html`) lets visitors filter and rank the builds (easiest, hardest, damage, clear, boss, most durable, off-meta).

`whirling/whirling-glacial-bolt.filter` is a loot-filter layer for the Whirling build; `python tools/build_filter.py --install` layers it on top of NeverSink's filter and writes it to the game's filter folder.

## What a guide contains

- **Now** — one prioritized action at a time for the current level.
- **Route** — seven phases (Acts 1–4, Maps, Endgame, Max) with goals, rotation, gems, supports, stats, tree, things to avoid and exit conditions.
- **Skills & supports** — when each gem becomes available, why each support is there, Spirit reservation budget.
- **Items** — per slot, ranked options for the player's level in *cheap* and *full* modes, with unique levels taken from poe.ninja's level requirement, price classes and a "next upgrade" pointer.
- **Passive tree** — the allocation order for every phase, the notable/keystone schedule, jewel sockets and which jewel goes where, and the respec point when the leveling tree differs from the final one.
- **Ascendancy** — the four Trials in order, what each node does and why it matters for this build.
- **Crafting workshop** — 12 equipment categories, three investment routes (buy, progressive craft, advanced) with concrete recipes.
- **Tricks, troubleshooting, atlas checklist, quests, timeline, sources.**
- **My character** — tick what you own; every tab adapts.

## How it works

```
sources ──► extract ──► variants ──► assets ──► template patch ──► HTML app
(PoB, Maxroll,  (per-build   (tree per   (icons,     (kpatch.py:        (kbuild.py + enhance.py:
 Mobalytics,     scripts)     phase,      passive     gear ranking,      bilingual, inlined
 poe.ninja)                   items)      order)      jewels, ...)       CSS/JS, versioned assets)
```

1. **Collect** — a build's Path of Building code, planner or guide is downloaded into `tools/dl/`. Game data comes from Path of Building's PoE2 data (`tools/dl/pob/`: gems, tiers, skill descriptions), RePoE2 (base items), PoE2DB (crafting pools) and poe.ninja (economy and ladder).
2. **Variants** — `tools/builds/<build>/mkvariants.py` (or the extract scripts in `tools/kit/`) turn the source into per-phase variants: the tree cut at 17/34/50/72/95 points, the items of each phase and the jewels.
3. **Build data** — `tools/builds/<build>/bdata.py` holds the guide itself as Python data: phases, gems per level, supports and why, uniques, gear rankings, tree stages, ascendancy, tricks, troubleshooting, timeline, sources. All text is bilingual (`L(pt, en)`).
4. **Assets** — `kit/kassets.py` builds the icon set and computes the **allocation order** of the passive tree for every phase (each phase is a connected cut from the class start; nothing the player cannot actually click).
5. **Template patch and build** — `kit/kpatch.py` generates the build's app template and applies the gear-ranking and jewel patches; `kit/kbuild.py` renders it; `tools/enhance.py` inlines CSS/JS and versions the shared assets.
6. **Landing page and league page** — `tools/build_landing.py`, `landing_v2.py`, `landing_registry.py` and `build_rites.py`.

`tools/build_all.py` runs the whole pipeline (about 4 minutes).

### Passive-tree logic

The kit reads the game's passive tree (`tools/tree.json`) and can:

- walk a Path of Building tree in an order the class can really allocate (`pobxml.walk_order`), including trees that start elsewhere through the Split Personality jewel;
- order nodes "damage first" (`pobxml.walk_greedy`) or in **stages** that close exactly on the phase cuts and force mechanic nodes at the right level (`pobxml.staged_greedy`);
- score nodes *for one specific build* (`kit/treescore.py`): a caster does not want melee nodes, a quarterstaff build does not want projectile nodes.

When a source only has an endgame tree and the road from the class start is a line of attribute nodes, the leveling tree is built separately and the guide states the respec level.

## The weekly automation

`.github/workflows/update.yml` runs every Monday at 06:00 UTC (and on demand) and calls `tools/update_all.py`:

| Step | Script | What it does |
|---|---|---|
| Collect | `ninja_meta.py` | Reads poe.ninja's build API for the current league: usage per ascendancy and skill, DPS/EHP of top characters |
| Classify | `registry.py` | Class, ascendancy, playstyle and the rankings |
| Discover | `discover.py` | Lists strong, off-meta ascendancy + skill combinations that have no guide → `docs/candidates.md` |
| Rebuild | `build_all.py` | Regenerates every page |
| Audit | `audit.py` | Finds anything lost, broken or impossible to follow → `docs/audit.md` |
| Tests | `unittest` | Repository test suite |
| Publish | workflow | Commits **only if the audit and the tests pass**; otherwise opens or updates an issue with the report |

**What the audit checks:** contract completeness, level ranges without gaps or overlaps, gems that enter after their phase ends, supports without an explanation, uniques defined but never used (or used but undefined), Spirit budget against quest rewards, passive-tree connectivity along the order the page actually shows, jewel sockets, notables named in a phase's tree text that the phase's tree does not contain, tree damage per phase (`tools/deepcheck.py`), sources with URLs, registration in every shared file, page and asset existence, and a fresh poe.ninja snapshot.

**What is not automatic:** writing a new guide (the cycle finds candidates and shows the numbers; phases, items, tree and rotation need curation), judging whether a build is *fun* or *easy to follow*, clear-speed rankings (poe.ninja exposes no clear measure, so those are editorial 1–5 scores and the landing says so), and playing the build. See [`docs/AUTOMACAO.md`](docs/AUTOMACAO.md).

## Tech stack

| Layer | Technology |
|---|---|
| Generators and data pipeline | **Python 3** (standard library, plus `Pillow` for images and `openpyxl` for the Silverfist Excel workbook) |
| Front end | **Vanilla JavaScript**, **HTML** and **CSS**: no framework, no bundler; one generated `index.html`/`en.html` per build plus `assets/assets.js` |
| Tests | Python `unittest`; **Node.js** with **Playwright** for browser, mobile, overlap and recipe tests |
| Automation | **GitHub Actions** (weekly cycle), **GitHub Pages** hosting |
| Data | Path of Building PoE2 data (**Lua** tables read as text), poe.ninja HTTP/JSON API, RePoE2 JSON, PoE2DB pages, Maxroll and Mobalytics guides |
| Windows helper | one small PowerShell script (`tools/recalc.ps1`) that recalculates the Excel workbook through Excel's COM interface |

## Repository layout

```
index.html, en.html           landing page (PT / EN)
<build>/                      generated app: index.html, en.html, assets/assets.js
planilha/                     Silverfist Excel workbook (built by tools/build_xlsx.py)
shared/                       shared front end: skin, effects, loader, crafting, build-now panel, art
tools/
  build_all.py                full rebuild
  update_all.py               weekly cycle (collect → classify → discover → rebuild → audit → test)
  audit.py, deepcheck.py      coherence audit and tree-damage measurement
  registry.py, ninja_meta.py, discover.py     rankings and candidate discovery
  kit/                        generic build kit: pobxml, ninja, kassets, kpatch, kbuild, treescore, jewels, craftkit, ...
  builds/<build>/             per-build data: bdata.py, bcraft.py, gear_opts.py, mkvariants.py
  craft/                      crafting data and its sources (see tools/craft/README.md)
  dl/                         downloaded sources and snapshots (PoB data, RePoE, poe.ninja, planners)
  tests/                      unit tests and Playwright suites
docs/                         AUTOMACAO.md, COMO-ADICIONAR-BUILD.md, audit.md, candidates.md, ...
.github/workflows/update.yml  weekly automation
```

Silverfist and Oracle predate the kit and still have their own scripts (`tools/data.py`, `tools/build_site.py`, `tools/oracle/`); every other build is generated by the kit.

## Running it locally

Only the standard library is needed to rebuild the site from the saved snapshots:

```bash
python tools/build_all.py
python -m http.server 8000      # then open http://localhost:8000
```

`Pillow` is needed for image generation and `openpyxl` for the Excel workbook. A local server gives PT/EN a single origin so progress is shared between the two versions (`localStorage` behaviour on `file://` varies by browser).

Rebuild a single kit build:

```bash
cd tools
python builds/<build>/mkvariants.py        # if the build has one
python kit/kassets.py <build> && python kit/kpatch.py <build> && python kit/kbuild.py <build>
```

Run the weekly cycle by hand: `python tools/update_all.py` (`--no-fetch` uses the saved snapshot, `--no-build` only refreshes data and audits).

## Verification

```bash
python tools/audit.py                        # 0 errors and 0 warnings expected
python -m unittest discover -s tools/tests
# Node + Playwright (and a browser) required:
node tools/tests/browser.cjs                 # every page and tab, PT/EN, 4 widths, crafting routes, search, keyboard
node tools/tests/mobile.cjs                  # phone/tablet: clipped text, off-screen, tiny targets, distorted images
node tools/tests/overlap.cjs                 # overlap audit, all tabs, 10 screen sizes
node tools/tests/recipes.cjs                 # crafting recipe order, PT/EN
node tools/tests/build-now.cjs               # adaptive panel, keyboard, scrolling, reduced motion
```

The browser suite starts a temporary local server, opens every page (landing, league guide and both languages of every build) at 1366, 1024, 768 and 390 px, walks every tab and crafting route, and fails on any runtime error or horizontal overflow.

## Adding a build

The step-by-step guide and the contract every build must satisfy (identity, seven phases, skills, tree, items, ascendancy, honest text, crafting, extras) is in [`docs/COMO-ADICIONAR-BUILD.md`](docs/COMO-ADICIONAR-BUILD.md). In short:

1. Download the source (Path of Building code, Maxroll planner, Mobalytics guide) into `tools/dl/`.
2. Create `tools/builds/<build>/mkvariants.py` (copy `twister` or `whirling`), `bdata.py` (start from `twister`), `gear_opts.py` and `bcraft.py`.
3. Generate art with `kit/mkart.py` and register the build in the shared files (the audit lists whatever is missing).
4. Run the pipeline, then `audit.py`, the unit tests and the browser/mobile suites. Commit and push; the weekly cycle re-runs everything and publishes only if it still passes.

## Limitations

- **Nobody plays the build automatically.** The audit checks internal coherence and data; it cannot tell whether a leveling route feels good in the game. Numbers such as "tree damage per phase" are sums of node modifiers on the tree, **not** in-game DPS.
- **Some leveling routes are adaptations.** Many sources only publish an endgame tree or Path of Building. Where the leveling plan is assembled here (gems from gem tiers, tree from a damage-first walk, items from a ranking), the guide says so in its "Fixes / adaptation" notes, including the respec level where the leveling tree differs from the final tree.
- **Rankings are partly editorial.** Difficulty comes from the guide's own complexity; damage and durability come from poe.ninja's characters; clear and boss scores are editorial.
- **Prices are a snapshot** of the last successful poe.ninja fetch and change quickly; unique prices from poe.ninja's unique endpoints are not refreshed automatically.
- **Gem availability** is derived from Path of Building's gem tier; the exact level at which a given uncut gem drops in the game is not verified by data.

## Credits and data sources

Build authors: Mattjestic, imortilize, Zizaran, Lowepe, BlazeworksTV, Ignatius, kingkongor, Goratha, Skadoosh, Lexd, havoc616 and Phylaris POE (Mobalytics and Maxroll guides). Data: [poe.ninja](https://poe.ninja/poe2), [Path of Building (PoE2)](https://github.com/PathOfBuildingCommunity/PathOfBuilding-PoE2), RePoE2, [PoE2DB](https://poe2db.tw), Maxroll and Mobalytics. Loot-filter base: NeverSink.

Fan project, not affiliated with Grinding Gear Games. Path of Exile is a trademark of Grinding Gear Games.
