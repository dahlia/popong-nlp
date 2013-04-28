#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

## Settings
data = {
    "codebook"  : "_input",
    "officials" : "/home/e9t/data/popong/people",
    "bills"     : "/home/e9t/data/popong/bills/pdf",
    "HHdic"     : "/home/e9t/data/hanja-hangul.json"
}

results = {
    "dict"      : "./_output",
    "test"      : "./_output"
}

importer = {
    "fieldname" : "district",
    "runopt"    : "all" # test, all, [some integer]
}

## Global variables
features = ["district", "education"]
others = ["name_kr", "name_cn", "assembly_no", "party", "birthday",\
    "birthmonth", "birthyear", "image", "sex", "cand_no", "elected", "address"]

main = {
    "opts" : {
        1: "get_data",
        2: "do_babylon (in preparation)",
        3: "do_bills (in preparation)",
        4: "do_structurize",
        5: "do_count (in preparation)"
    }
}

district = {
    "levels"    : ["시", "군", "구"],
    "sublevels" : ["갑", "을", "병"],
    "stopwords" : ["제", "선거구", "지역구"],
    "aliases"   : {
        "서울": "서울특별시",
        "대전": "대전광역시",
        "대구": "대구광역시",
        "부산": "부산광역시",
        "울산": "울산광역시",
        "광주": "광주광역시",
        "인천": "인천광역시",
        "제주": "제주특별자치도",
        "경기": "경기도",
        "강원": "강원도",
        "충북": "충청북도",
        "충남": "충청남도",
        "전남": "전라남도",
        "전북": "전라북도",
        "경남": "경상남도",
        "경북": "경상북도"
    }
}

education = {
    "statuses"  : ["졸", "졸업", "수료", "중퇴", "제적"],
    "stopwords" : ["한문수학","한수","한문"],
    "aliases"   : {
        "대졸":"대학 졸업",
        "중졸":"중학교 졸업",
        "소졸":"소학교 졸업",
        "전졸":"전문대학 졸업",
        "고졸":"고등학교 졸업",
        "국졸":"국민학교 졸업",
        "보졸":"보통학교 졸업",
        "초졸":"초등학교 졸업",
        "고보졸":"고등보통학교 졸업",
        "대퇴":"대학 중퇴"
    }
}
