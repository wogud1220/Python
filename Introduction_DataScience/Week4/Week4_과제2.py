# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import pandas as pd
import json

client_id = "g49bTiA60G2NgCaApKO4"
client_secret = "FwBghmHPuD"
encText = urllib.parse.quote("상명대학교")
# url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=20&start="# JSON 결과
#url_xml = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # XML 결과

i = 1

df = pd.DataFrame()

for i in range(1,111): # 1000번 반복
    url= "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=1&start="+str(i)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    print(response)
    rescode = response.getcode()


    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8')) # 전체 다 출력
    else:
        print("Error Code:" + rescode)

    result = response_body.decode('utf-8')
    # print(result)
    # print(type(result))
    news_result = json.loads(result)
    # print(news_result)

    # i+=1  # 검색 위치 20개씩 증가시켜야함 display가 20개씩 보여줘서

    for item in news_result['items']:   #json의 목록 1개 중에서
        df = pd.DataFrame(news_result['items'])   # news_result로 데이터 프레임 생성
        df.to_csv("naver_result.csv", mode='a') # Save as csv


    for item in news_result['items']:
        text = item['description']
        with open('naver_text.txt', mode='a') as f:
            f.write(text + '\n')
