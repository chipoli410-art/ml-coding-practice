# -*- coding: utf-8 -*-
import urllib.request
import datetime
import json

client_id = 'H9035OclH0ZJBPEd7rzA'
client_secret = 'c9L3L_G6HK'

def main():

    node = 'news'                                            # 크롤링할 대상
    srch_text = input('검색어를 입력하세요:')

    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srch_text, 1, 100)      # [CODE 2]
    total = jsonResponse['total']

    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)                # [CODE 3]

            s
