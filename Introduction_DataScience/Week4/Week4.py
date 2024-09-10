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
for i in range(1,11):
    url= "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=20&start="+str(i)
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    print(response)
    rescode = response.getcode()


    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)


    result = response_body.decode('utf-8')
    print(result)
    print(type(result))

    news_result = json.loads(result)
    print(news_result)

    df = pd.DataFrame(news_result['items'])
    print(df)
    df.to_csv("naver_result.csv", mode='a')
