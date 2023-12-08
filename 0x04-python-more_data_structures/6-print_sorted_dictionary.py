#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for m in sorted(a_dictionary.keys()):
        print("{}: {}".format(m, a_dictionary.get(m)))
