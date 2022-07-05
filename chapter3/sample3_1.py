#비교 연산자

from pickle import TRUE
from turtle import Turtle


print(10 == 100)
print(10 != 100)
print(10 < 100)
print(10 > 100)
print(10 <= 100)
print(10 >= 100)
print()

print("가방" == "하마")
print("가방" != "하마")
print("가방" <= "하마")
print("가방" >= "하마")
print()

#논리 연산자
print(not True)
print(not False)
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print()

x = 10
under_20 = x < 20
print(x, "is under_ 20 :", under_20)
print(x, "is not under_20 :", not under_20)
print()

#조건문의 기본 사용

number = input("정수 입력 > ")  # 입력받기 
number = int(number)            # 입력을 정수로 변환

if number > 0 :
    print("양수입니다") 

if number < 0 :
    print("음수입니다")

if number == 0 :
    print("0입니다")

print()

#날짜/시간 출력

import datetime                 # 날짜,시간과 관련된 기능 가져오기

now = datetime.datetime.now()   # 현재 날짜,시간 구하기

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

#format이용 한번에 출력

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
print()

#오전/오후 구분

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다".format(now.hour%12))

if now.hour > 12:
    print("현재 시각은 {}시로 오후입니다".format(now.hour%12))

#계절 구분

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

if 12 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))

print()

#홀수 짝수 구분

number = input("정수 입력 > ")

last_character = number[-1]         # 마지막 자리 추출

last_number = int(last_character)   # 정수로 변환

# 첫번째 방법

if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8 :
    print("짝수입니다")

if last_number == 1 \
    or last_number == 3 \
    or last_number == 5 \
    or last_number == 7 \
    or last_number == 9 :
    print("홀수입니다")

# 두번째 방법 

if int(number) % 2 == 0 :
    print("짝수입니다")

if int(number) % 2 == 1 :
    print("홀수입니다")

# 세번째 방법

if last_character in "02468":
    print("짝수입니다")

if last_character in "13579":
    print("홀수입니다")
