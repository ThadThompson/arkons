"""
Convert the text copied from https://ark.gamepedia.com/Item_IDs/Ammunition?action=edit
to Python dictionary in 'ark_items.py
"""

import json

def get_key(k: str):
    bidx = k.find('(')
    if bidx >= 0:
        k = k[:bidx]
    k = k.strip()
    k = k.replace(' ', '_')
    k = k.replace('-', '_')
    k = k.replace('"', '')
    k = k.replace("'", '')
    return k.upper()


def get_blueprint(v: str):
    return f"\"Blueprint'/Game/{v}'\""


def get_group(line: str):
    g = line.replace('#', '')
    g = g.strip()
    return g.upper()


items = {}
groups = {}

with open('items.txt', 'r') as fin:
    for line in fin:
        line = line.rstrip()
        if not line:
            continue

        if line.startswith("#"):
            group = get_group(line)
            groups[group] = []
            continue

        values = line.split('|')
        key = get_key(values[1])
        bp = get_blueprint(values[5])

        if key in items:
            continue

        items[key] = bp
        groups[group].append(key)

ARK_DATA = {
    'items': items,
    'groups': groups,
}

with open('www/ark_data.json', 'w', encoding='utf-8') as f:
    json.dump(ARK_DATA, f, ensure_ascii=False, indent=4)

