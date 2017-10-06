#! /usr/bin/python3

import json
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as input_file:
        json_data = json.load(input_file)
    return json_data


def pretty_print_json(input_datat):
    print(json.dumps(input_datat, sort_keys=True, indent=4,
                     ensure_ascii=False))


def create_parser():
    parser = argparse.ArgumentParser(description='--> Pretty json output <--')
    parser.add_argument("path", nargs=1, help="path to json file")
    return parser


'''
C:/Users/g84086619/Documents/Devman/4_json-master/4_json-master/pprint_json.py ../new2.json   - выполняется успешно
C:/Users/g84086619/Documents/Devman/4_json-master/4_json-master/pprint_json.py new2.json      - выполняется успешно
'''
if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.path:
        pretty_print_json(load_data(namespace.path[0]))
