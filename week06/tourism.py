# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json
import pandas as pd

service_key = "27abaeaae1e3e2aaf79e45f5312beb77036874ff34a49a55f8a5cc202fdd2efd"

"""### [CODE 0]"""

def main():
    jsonResult =[]
    result = []

    print("<< 국내 입국한 외국인의 통계 데이터를 수집 합시다. >>")
    nat_cd = input('국가 코드를 입력하세요(중국:112 / 일본: 130 / 미국: 275):')
    