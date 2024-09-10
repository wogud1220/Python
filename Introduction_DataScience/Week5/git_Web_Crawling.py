import requests
from bs4 import BeautifulSoup
url1 = "https://github.com/wogud1220/Python"
url2 = "https://github.com/wogud1220/BlueMoon"
url3 = 'https://github.com/wogud1220/MacSwift'
url4 = 'https://github.com/wogud1220/Java'
url5 = 'https://github.com/wogud1220/Cafe-ING'
url6 = 'https://github.com/wogud1220/Face_Detection_Music'
url7 = 'https://github.com/wogud1220/html'
url8 = 'https://github.com/wogud1220/Bae-joonHub-'
url9 = 'https://github.com/wogud1220/wogud1220'
url10 = 'https://github.com/wogud1220/C-Programming'

def get_url(url1):
    response = requests.get(url1)
    # print(response.text)   
    soup = BeautifulSoup(response.text, "html.parser") 
    repo_names = soup.find_all('a',class_='Link--primary') # 폴더 유형
    # print(repo_names)
    print()
    with open('git_url.txt','a') as f:
        for td in repo_names:
            text = td.get_text(strip = True) #true 앞뒤 공백 지우기
            print(text)
            f.write(text + '\n')
        repo_names = soup.find_all('div', class_='Box-sc-g0xbh4-0 bJMeLZ js-snippet-clipboard-copy-unpositioned')
        #ReadMe 파일의 제목과 내용을 파일에 입력
        for td in repo_names:
            text = td.get_text(strip = True)
            f.write(text +'\n\n\n\n\n')

get_url(url1)
get_url(url2)
get_url(url3)
get_url(url4)
get_url(url5)
get_url(url6)
get_url(url7)
get_url(url8)
get_url(url9)
get_url(url10)



