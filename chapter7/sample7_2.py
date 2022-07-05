# 외부모듈

# BeautifulSoup 모듈로 날씨 가져오기

# from urllib import request
# from bs4 import BeautifulSoup

# target = request.urlopen("https://weather.naver.com/")

# soup = BeautifulSoup(target, "html.parser")

# for location in soup.select("location"):
#   print("도시:", location.select_one("city").string)
#   print("날씨:", location.select_one("wf").string)
#   print("최저기온:", location.select_one("tmn").string)
#   print("최고기온:", location.select_one("tmx").string)
#   print()

#Flast 모듈 사용하기
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#   return "<h1>Hello World!</h1>"

#데코레이터
def test(function):
  def wrapper():
    print("인사가 시작되었습니다.")
    function()
    print("인사가 종료되었습니다.")
  return wrapper

@test #데코레이터를 붙여서 함수 만들기
def hello():
  print("hello")

hello()