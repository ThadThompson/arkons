"""
Convert the text copied from https://ark.gamepedia.com/Item_IDs/Ammunition?action=edit
to Python dictionary in 'ark_items.py
"""


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


def blueprint(v: str):
    return f"\"Blueprint'/Game/{v}'\""


keys = set()

with open('items.txt', 'r') as fin:
    with open('ark_items.py', 'w') as fout:
        fout.write('ark_items = {\n')
        for line in fin:
            line = line.rstrip()
            if not line:
                continue

            if line.startswith("#"):
                fout.write("\n")
                fout.write("    " + line)
                fout.write("\n")
                continue

            values = line.split('|')
            key = get_key(values[1])
            bp = blueprint(values[5])

            if key in keys:
                continue

            keys.add(key)
            key = "    '{}':".format(key).ljust(42)
            fout.write(key + bp + ",\n")
        fout.write('\n}\n')
