import os
import sys
import urllib.request 
import json

client_id = ""
client_secret = ""

encText = urllib.parse.quote("닥터 스트레인지")
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    response_body = response_body.decode('utf-8')
    response_body = response_body.replace('<b>', ' ')
    response_body = response_body.replace('</b>',' ')
    response_body = response_body.replace('|', ' ')
    data = json.loads(response_body)
    for a in data["items"]:
        print(a["title"])
        print(a["link"])
        print(a["director"])
        print("\n")
else:
    print("Error Code:" + rescode)