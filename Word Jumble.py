#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:12:49 2018

@author: kefei
"""

import requests
def words_list():
    """Downloads and procsses a word list containing 274,926 words!
    You may need to install the 'requests' package through the `pip install requests`.
    """
    req = requests.get("https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt")
    words = req.text.split("\n")
    return words

def jumble_decode(jumbled_word):
    """This method is going to find the valid English words given a string of letters
    
    Need a string of letters as parameter and return a list of of valid English words"""
    ans = []
    anag_list = anagrams(jumbled_word)
    whole_list = words_list()
    
    # check if the words are valid English words
    for i in anag_list:
        if i in whole_list:
            ans.append(i)
    return ans
        
def anagrams(word):
    """This method is going to find all generated anagrams regardless of whether they are valid English words
    
    Need a string of letters as parameter and return a Python list of all generated anagrams """
    if word == "":
        return[word]
    else:
        ans = []
        for w in anagrams(word[1:]):  # do the recursion
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + word[0] +w[pos:])
    
    for i in range(len(ans)):  # find if there is any redundant words in the list
        if ans[i] in ans[(i+1):]:
            ans[i] = 0  # if two words are the same then set one with 0
    
    ans[:] = (value for value in ans if value != 0)  # delete all the 0 in the list
    return ans

# For example
jumble = jumble_decode("plaep")
print(jumble)