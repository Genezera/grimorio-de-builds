"""Publish cached mod tables with provenance, without claiming verified drop odds."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
DL = ROOT / 'tools' / 'dl'
PAGES = ['Amulets', 'Rings', 'Belts', 'Wands', 'Sceptres', 'Two_Hand_Maces',
         'Helmets_int', 'Helmets_dex_int', 'Body_Armours_int', 'Body_Armours_dex',
         'Gloves_int', 'Gloves_dex', 'Boots_int', 'Boots_dex', 'Life_Flasks', 'Mana_Flasks', 'Charms']
data = {'reviewed': '2026-09-16', 'patch': '0.5.5', 'pools': {}, 'prices': {}}
for page in PAGES:
    source = DL / 'web' / f'mods_{page}.json'
    rows = json.loads(source.read_text(encoding='utf-8'))[0]['mods']
    data['pools'][page] = [{k: m[k] for k in ('kind', 'name', 'level', 'gen', 'family', 'weight', 'text')}
                           for m in rows if m['kind'] in ('normal', 'desecrated', 'essence', 'perfect_essence')]
for category in ['Currency', 'Essences', 'Abyss', 'Omens', 'Ritual', 'Breach', 'Runes']:
    path = DL / f'ex_{category}.json'
    if not path.exists():
        continue
    payload = json.loads(path.read_text(encoding='utf-8'))
    if payload.get('core', {}).get('primary') != 'divine':
        continue
    names = {i['id']: i['name'] for i in payload.get('items', []) + payload.get('core', {}).get('items', [])}
    for row in payload.get('lines', []):
        if row['id'] in names and isinstance(row.get('primaryValue'), (int, float)):
            data['prices'][names[row['id']]] = row['primaryValue']
data['priceNote'] = 'poe.ninja exchange overview, league Forbidden Rites, fetched 2026-09-16.'
(ROOT / 'shared').mkdir(exist_ok=True)
(ROOT / 'shared' / 'craft-data.js').write_text('window.CRAFT_DATA=' + json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + ';\n', encoding='utf-8')
print('Crafting tables:', len(data['pools']), 'classes;', len(data['prices']), 'cached prices')
