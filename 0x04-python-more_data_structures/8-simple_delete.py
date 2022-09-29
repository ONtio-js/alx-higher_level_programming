#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    return {k: val for k,val in a_dictionary.items() if k != key}