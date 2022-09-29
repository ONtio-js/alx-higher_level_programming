#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list1 = []
    for word in my_list :
        if word == search :
            word = replace
        my_list1.append(word)

        
    return my_list1