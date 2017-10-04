import json
from sys import argv


filepath = argv[1]
print(filepath)


def load_data(filepath):
    with open(filepath) as f:
        data = json.load(f)
        print(data)
    return data


def pretty_print_json(data,deep = 1, comma = 0):
 #   print('[\n\t{')
    if isinstance(data,dict):
        comma2 = len(data.keys())
        print("\t" * (deep-1), "{")
        for key,value in data.items():
            print("\t"*deep,"\"{}\":".format(key), end = '')


            if isinstance(value,list):
                print("\t"*(deep),"[")
                comma = len(value)

                for listvalue in value:
                    pretty_print_json(listvalue,deep+1, comma)
                    comma = comma - 1
                    #print("comma =",comma)

                if comma2 > 1:
                    print("\t"*(deep),"],")
                else:
                    print("\t" * (deep), "]")

            if isinstance(value,dict):
                print("\t" * (deep), "{")
                comma = len(value)

                for dictkey in value:
                    print("\t"*(deep+1),"\"{}\":".format(dictkey), end = '')
                    pretty_print_json(value[dictkey],deep+2, comma )
                    comma = comma - 1

                if comma2 > 1:
                    print("\t" * (deep), "},")
                else:
                    print("\t" * (deep), "}")

            if (isinstance(value,list) == False and isinstance(value,dict) == False):
               # print("comma2=",comma2)

                if comma2 >1:
                    print("\t"*(deep+1),"\"{}\",".format(value))
                else:
                    print("\t" * (deep + 1), "\"{}\"".format(value))
            comma2 = comma2-1
        if comma > 1:
            print("\t" * (deep-1), "},")
        else:
            print("\t" * (deep - 1), "}")

    elif isinstance(data,list):
        # comma?
        comma = len(data)
        for listvalue2 in data:
            print("\t" * (deep), "[")
            pretty_print_json(listvalue2,deep+1,comma)
            comma = comma - 1
            print("\t" * (deep), "]")
    else:
        if comma>1:
            print("\t"*(deep),"\"{}\",".format(data))

        else:
            print("\t" * (deep), "\"{}\"".format(data))





if __name__ == '__main__':
    deep = 0
    pretty_print_json(load_data(filepath))
