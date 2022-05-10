# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
client_id = "############"
client_secret = "############"
encText = urllib.parse.quote("아이언맨")
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
print(request)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response = response_body.decode('utf-8')
    json_response = json.loads(response_body)
    for i in range(10):
        print(f'{i}번째 영화입니다.')
        print(json_response['items'][i]['title'].replace('<b>', '').replace('</b>', ''))
        print(json_response['items'][i]['link'])
        print(json_response['items'][i]['director'].replace('|', ''))
else:
    print("Error Code:" + rescode)
