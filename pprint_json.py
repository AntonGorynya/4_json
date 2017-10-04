import json
from sys import argv

filepath = argv[1]
#print(filepath)

def load_data(filepath):
    with open(filepath) as f:
        json_data = json.load(f)
     #   print(json_data)
    return json_data

def pretty_print_json(json_data, deep = 1, comma = 0):
    if isinstance(json_data, dict):
        comma2 = len(json_data.keys())
        print("\t" * (deep-1), "{")
        for key,value in json_data.items():
            print("\t"*deep,"\"{}\":".format(key), end = '')
            if isinstance(value,list):
                comma = print_list(deep,comma2,value)

            if isinstance(value,dict):
                comma=print_dict(deep,comma2, value)

            if (isinstance(value,list) == False and isinstance(value,dict) == False):
                print_value(comma2, deep+1, value)
            comma2 = comma2-1

        print_right_border(comma, deep - 1, bound_type='dict')

    elif isinstance(json_data, list):
        comma=print_list(deep, comma2, json_data)
    else:
        print_value(comma, deep, json_data)

def print_list(deep,comma2,value):
    print("\t" * (deep), "[")
    comma = len(value)
    for listvalue in value:
        pretty_print_json(listvalue, deep + 1, comma)
        comma = comma - 1
    print_right_border(comma2, deep, bound_type='list')
    return comma

def print_dict(deep,comma2,value):
    print("\t" * (deep), "{")
    comma = len(value)
    for dictkey in value:
        print("\t" * (deep + 1), "\"{}\":".format(dictkey), end='')
        pretty_print_json(value[dictkey], deep + 2, comma)
        comma = comma - 1
    print_right_border(comma2, deep, bound_type='dict')
    return comma

def print_right_border(comma, deep, bound_type ='dict'):
    if bound_type == 'dict':
        if comma > 1:
            print("\t" * (deep), "},")
        else:
            print("\t" * (deep), "}")
    elif bound_type == 'list':
        if comma > 1:
            print("\t" * (deep), "],")
        else:
            print("\t" * (deep), "]")

def print_value(comma,deep,json_data):
    if comma > 1:
        print("\t" * (deep), "\"{}\",".format(json_data))

    else:
        print("\t" * (deep), "\"{}\"".format(json_data))

if __name__ == '__main__':
    deep = 0
    pretty_print_json(load_data(filepath))
