import json
from sys import argv

def load_data(filepath):
    with open(filepath) as f:
        json_data = json.load(f)
    return json_data

def pretty_print_json(json_data, deep = 0, comma = 0):
    print(json.dumps(load_data(filepath), sort_keys=True, indent=4))

if __name__ == '__main__':
    filepath = argv[1]
    pretty_print_json(load_data(filepath))
