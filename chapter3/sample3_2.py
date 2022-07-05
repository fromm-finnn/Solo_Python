#else

number = input("정수 입력 >")
number = int(number)

if number % 2 ==0 :
    print("짝수입니다")
else:
    print("홀수입니다")
print()

#계절구하기

import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month :
    print("현재는 봄입니다")
elif 6 <= month :
    print("현재는 여름입니다")
elif 9 <= month  :
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")
print()

#False로 변환되는 값

print("#if 조건문에 0 넣기")
if 0:
    print("0은 True로 변환됩니다")
else:
    print("0은 False로 변환됩니다")
print()

print("#빈 조건문에 빈 문자열 넣기")
if "" :
    print("빈 문자열은 True로 변환됩니다")
else :
    print("빈 문자열은 False로 변환됩니다")

#pass키워드

number = input("정수 입력 > ")
number = int(number)

if number > 0 :
    pass            # 아직 미구현
else :
    pass            # 아직 미구현