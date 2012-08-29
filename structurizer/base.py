#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is a library to structurize 
short free texts written in the Korean language.

[Params]
 - fieldname:
    votenum, district, elected, name_kr, voterate, name_cn, 
    experience, sex, birthyear, job, party, assembly_no, education

 - opt:
    Integer in [1,82] || String in {'all', 'test'}
"""

import re, os, json 
from pprint import pprint
from collections import Counter
from glob import glob

import utils
from importer import importer
from preprocessor import preprocessor
from rules import apply_rules
from wordify import wordify

settings = {
    'DIR': '''../../crawlers/election_commission/data/''',
    'MAX_PRINT': 30,
    'MAX_ELECTIONS': 20,
    'DELIMS': '[\W]'
    }

def test(fieldname, nprint, flatten, opt):

    rawlist = importer(settings['DIR'], opt, fieldname)
    fieldlist = preprocessor(rawlist)
    fieldlist = apply_rules(fieldname, fieldlist)
    fieldlist = wordify(fieldlist, ['졸업','수료','박사','석사'])
    fieldlist = list(fieldlist)

    wordlist = list_parser(fieldlist)

    '''
    t = list(wordlist)
    pprint(t)
    print(len(t))
    '''

    birthyear = importer(settings['DIR'], opt, 'birthyear')
    name_kr = importer(settings['DIR'], opt, 'name_kr')
    tmp = list(zip(birthyear, name_kr, wordlist, rawlist))
    #tmp = list(zip(birthyear, name_kr, fieldlist, rawlist))
    pprint(tmp)
    print(len(tmp))

    if flatten == 1:
        wordlist = list_parser(fieldlist)
        wordlist = flatten_list(wordlist)
    else:
        wordlist = fieldlist
    '''
    for word in wordlist:
        if len(word) < 3:
            print(word)
    '''
    cnt = word_counter(wordlist)
    aa = cnt.most_common(nprint)
    pprint(aa)

    return cnt

def word_counter(wordlist):
    cnt = Counter()
    for word in wordlist:
        cnt[word] += 1
    return cnt

def flatten_list(listoflist):
    def str2list(item):
        if isinstance(item, str):
            item = [item]
        else:
            pass
        return item

    listoflist = [str2list(item) for item in listoflist]
    return [item for sublist in listoflist for item in sublist]

def list_parser(rawlist):
    wordlist = (list(filter(None, re.split(settings["DELIMS"],item))) for item in rawlist)
    '''
    wordlist = []
    for item in rawlist:
        wordlist.append(re.split(settings["DELIMS"],item))
    '''
    return wordlist

if __name__ == '__main__':
    test()