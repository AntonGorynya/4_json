#! /usr/bin/python3

import json
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as input_file:
        json_data = json.load(input_file)
    return json_data


def pretty_print_json(input_data):
    print(json.dumps(input_data, sort_keys=True, indent=4,
                     ensure_ascii=False))


def create_parser():
    parser = argparse.ArgumentParser(description='--> Pretty json output <--')
    parser.add_argument("path", help="path to json file")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.path:
        print(namespace.path)
        pretty_print_json(load_data(namespace.path))
