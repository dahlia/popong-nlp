#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys

from ..utils import encoder
from .. import settings as s
from . import district
from . import education

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CM_REGION = encoder.get_codemap('region')
CM_EDUCATION = encoder.get_codemap('education')

def structurize(string, _type):
    if _type=='district':
        return district.struct(string, CM_REGION)
    elif _type=='education':
        return education.struct(string, CM_EDUCATION)
    else:
        print 'Warning: Invalid input'
        sys.exit(2)

def markup(string, _type):
    if _type=='district':
        return district.markup(string, CM_REGION)
    elif _type=='education':
        return education.markup(string, CM_EDUCATION)
    else:
        print 'Warning: Invalid input'
        sys.exit(2)


if __name__=='__main__':
    print structurize('district', u'서울 관악구 봉천동')
