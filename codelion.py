import os
import sys
import urllib.request
import json

client_id = "******************"
client_secret = "***********"
encText = urllib.parse.quote("아이언맨")
url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_body = response_body.decode('utf-8')  # 한국어로 정보를 얻기 위해 utf-8로 디코딩 함

    response_body = response_body.replace('<b>', ' ')
    response_body = response_body.replace('</b>', ' ')
    response_body = response_body.replace('|', ', ')
    data = json.loads(response_body)
    data_dict = data['items']   # list


    for i in range(len(data_dict)):
        print("TITLE : ",data_dict[i]['title'])
        print("LINK : ",data_dict[i]['link'])
        print("DIRECTOR : ",data_dict[i]['director'])
        print("\n")

else:
    print("Error Code:" + rescode)