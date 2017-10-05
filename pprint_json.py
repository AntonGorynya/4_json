#! /usr/bin/python3
# -*- coding: utf-8 -*-

from sys import argv
import json
import argparse


def load_data(filepath):
    with open(filepath, encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


def pretty_print_json(json_data_in):
    print(json.dumps(json_data_in, sort_keys=True, indent=4,
                     ensure_ascii=False))


def create_parser():
    parser = argparse.ArgumentParser(description='--> Pretty json output <--')
    parser.add_argument("path", nargs='+', help="path to json file")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.path:
        pretty_print_json(load_data(namespace.path[0]))
