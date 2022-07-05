#표준모듈

#math 모듈

# sin(x) ~ tan(x)
# log(x[,base])
# ceil(x) 올림
# floor(x) 내림

#from구문

# from math import sin, cos, tan, floor, ceil, pi

# print(sin(pi/6), cos(0), tan(0), floor(2.5), ceil(2.5), sep="\n")
# print()

#as 구문

# import math as m

# print(m.sin(m.pi/6), m.cos(0), m.tan(0), m.floor(2.5), m.ceil(2.5), sep="\n")
# print()

#random 모듈

# import random
# print("# random 모듈")

# print("- randonm():", random.random()) #radnom(): 0.0 <= x < 1.0 사이의 float을 리턴

# print("- uniform(10,20):", random.uniform(10,20)) #uniform(mix,max) : 지정한 범위 사이의 float을 리턴

# print("- randrange(10):", random.randrange(10)) #randrange(): 지정한 범위의 int를 리턴 // randrange(max) : 0부터 max 사이의 값을 리턴 // randrange(min,max) : mix부터 max 사이의 값을 리턴

# print("- choice([1,2,3,4,5]):", random.choice([1,2,3,4,5])) #choice(list) : 리스트 내부에 있는 요소를 랜덤하게 선택

# print("- shuffle([1,2,3,4,5]):", random.shuffle([1,2,3,4,5])) #random.shuffle : 리시트의 요소들을 랜덤하게 섞음

# print("- sample([1,2,3,4,5], k=2):", random.sample([1,2,3,4,5], k=2)) # sample(list, k=숫자) : 리스트의 요소 중에 k개를 뽑음

# print()
## 사용하는 모듈고 같은 이름으로 파일명 저장시 TypeError 뜸

# #sys모듈

# import sys
# print(sys.argv) # 명령 매개변수 출력
# print("---")

# #컴퓨터 환경과 관련된 정보 출력
# print("getwindowsversion:()", sys.getwindowsversion()) 
# print("---")
# print("copyright:", sys.copyright)
# print("---")
# print("version:", sys.version)

# # 프로그램 강제종료
# sys.exit()

#os 모듈

# import os

# #기본정보 출력
# print("현재 운영체제:", os.name)
# print("현재 폴더:", os.getcwd())
# print("혀내 폴더 내부의 요소:", os.listdir())

# #폴더 만들고 제거[폴더가 비어있을 때만 제거 가능]
# os.mkdir("hello")
# os.rmdir("hello")

# #v파일을 생성하고 이름 변경
# with open("original.txt", "w") as file:
#   file.write("hello")
# os.rename("original.txt", "new.txt")

# #파일을 제거
# os.remove("new.txt") ##os.unlink("new.txt")

# #시스템 명령어 실행
# os.system("dir")

# datetime모듈

# import datetime

# print("# 현재 시각 출력하기")
# now = datetime.datetime.now()
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print()

# print("# 시간을 포멧에 맞춰 출력하기")
# output_a = now.strftime("%Y.%m.%d %H:%M:%S")
# output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
#   now.month,\
#   now.day,\
#   now.hour,\
#   now.minute,\
#   now.second)
# output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초")
# print(output_a)
# print(output_b)
# print(output_c)
# print()

#시간처리하기

# import datetime
# now = datetime.datetime.now()

# #특정 시간 이후의 시간 구하기
# print("# datetime.timedelta로 시간 더하기") ##timedelta는 n년후를 구하지는 못함
# after = now + datetime.timedelta(\
#   weeks=1,\
#   days=1, \
#   hours=1, \
#   minutes=1, \
#   seconds=1)
# print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))
# print()

# #특정 시간 요소 교체하기
# print("# now.replace()로 1년 더하기")
# output = now.replace(year=(now.year +1 ))
# print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초"))

#time 모듈

# import time

# print("지금부터 5초 동안 정지합니다!")
# time.sleep(5)
# print("프로그램을 종료합니다")

#urllib 모듈
# from urllib import request

# target = request.urlopen("https://google.com")
# output = target.read()

# print(output)