# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import pandas as pd
import json
import requests

client_id = "g49bTiA60G2NgCaApKO4"
client_secret = "FwBghmHPuD"
encText = urllib.parse.quote("떡볶이")
url = "https://openapi.naver.com/v1/search/image?query=" + encText + "&display=1&start=1"# JSON 결과
#url_xml = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # XML 결과

index = 1
i = 1
for i in range(1,201):
    url= "https://openapi.naver.com/v1/search/image?query=" + encText + "&display=1&start="+str(i)
    print(url)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)

    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
    # print(response_body.decode('utf-8')) # 디코딩 해서 전체 출력
    else:
        print("Error Code:" + rescode)
    print(response) # <http.client.HTTPResponse object at 0x1048fcca0>
    result = response_body.decode('utf-8') # 디코딩 한 거 저장하고
    print(type(result)) # <class 'str'>

    news_result = json.loads(response_body) # json 형태로 저장
    # i+=1
    for item in news_result['items']:   #json의 목록 1개 중에서
        df = pd.DataFrame(news_result['items'])   # news_result로 데이터 프레임 생성
        df = df['link'] # link 부분만 가져와서 column만 df에 넣겠다.
        df.to_csv("naver_food_link.csv", mode='a') # Save as csv

    #new_result에 1개씩 가져와서 csv에 append 하고 link의 이미지 다운로드 * 200번 반복하기
    for item in news_result['items']:
        img_file = requests.get(item['link'])
        print(item['link'])
        with open("food" + str(index) + '.jpg', 'wb') as f:     #이미지 파일 만들어서 저장할거임
            f.write(img_file.content)
            index+=1
# print(news_result) # json 형태로 쫘르륵 나옴




print('Download Finished')

