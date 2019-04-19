import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
open(storage_path, 'a').close()

if args.key is not None:
    with open(storage_path, 'r+') as f:
        jsonFile = f.read()
        if not jsonFile:
            map_items = {}
        else:
            map_items = json.loads(jsonFile)
        item = map_items.get(args.key, None)
        if args.val is not None:
            if item is not None:
                item.append(args.val)
            else:
                item = [args.val]
            map_items[args.key] = item
            f.seek(0)
            json.dump(map_items, f)
        else:
            if item:
                print(', '.join(item))
else:
    print(None)
