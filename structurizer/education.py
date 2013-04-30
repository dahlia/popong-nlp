#! /usr/bin/python3
# -*- coding: utf=8 -*-

from babylon import canonizer
from utils import utils
import settings as s
import base

STARTS = s.education['countries']
ENDS = s.education['statuses']
STOPWORDS = s.education['stopwords']
ABBREVS = s.education['aliases']
ALIASES = utils.read_json('dict/aliases-education.json')

def convert(line):
    endsplit = base.endsplitter(line, ENDS)
    startsplit = base.startsplitter(endsplit, STARTS)
    words = base.wordify(startsplit)
    erased = base.eraser(words, STOPWORDS)
    canonized = base.canonizer(erased, ABBREVS)
    canonized = base.canonizer(canonized, ALIASES)
    return ' '.join(canonized)

def struct(string, codemap):
    print 'tba'

def markup(string, codemap):
    print 'tba'

def main(codemap):

    def write_results(filename, sth):
        with open(filename, 'w') as f:
            f.write('\n'.join(sth).encode('utf-8'))
            print 'Written to ' + filename

    ## Get data
    data = utils.read_text('./_output/people-all-education.txt')
    lines = data.split('\n')
    lines = data.split('\n')[-100:-30]

    ## Convert data
    converted = [convert(line) for line in lines]

    ## Print results
    for l, c in zip(lines, converted): print '%s -> %s' % (l, c)
    #write_results('_output/people-all-education-semistructured.txt', converted)
