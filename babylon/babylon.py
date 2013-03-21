#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys, json
from urllib2 import HTTPError
import gevent
from gevent.monkey import patch_all; patch_all()

from canonizer.wikipedia import canonical_name

# FIXME: global name 'etree' not defined Error

def print_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def build_dict(fieldname, obj):

    text = textify(obj)
    filename = '_output/%s.txt' % (fieldname)
    with open(filename, 'w') as f:
        f.write(text.encode('utf-8'))

    words = unique_words(text)
    filename = '_output/%s-wordlist.json' % (fieldname)
    print_json(filename, words)

    sys.stdout.write('n(unique_words)\t: ')
    print len(words)

    dic = {}
    i = 0
    jobs = []

    for word in words:
        sys.stdout.write(str(i)+'\t')
        #hashing(word, dic)
        job = gevent.spawn(hashing, word, dic)
        jobs.append(job)
        i += 1

    gevent.joinall(jobs)
    filename = '_output/%s.json' % (fieldname)
    print_json(filename, dic)

    return dic

def textify(obj):
    if isinstance(obj, list):
        return '<s> ' + ' </s>\n<s> '.join(obj) + ' </s>'
    else:
        raise ValueError

def unique_words(text):
   l = text.split()
   w = list(set(l))
   return w

def hashing(word, dic):
    try:
        canon = canonical_name(word.encode('utf-8'))
        dic[word] = canon
        print word, '\t: ', canon
    except HTTPError, e:
        print word

if __name__ == '__main__':
    print "Good"
    # etime - stime, "seconds"
    # education 전체로 돌렸을 때 9083 sec
    # party 전체로 돌렸을 때 82 sec
