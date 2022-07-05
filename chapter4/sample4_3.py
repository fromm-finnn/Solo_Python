#range

#for 반복문과 범위
for i in range(5):
    print(str(i) + "= 반복 변수")
print()

for i in range(5,10):
    print(str(i) + "= 반복 변수")
print()

for i in range(0,10,3):
    print(str(i) + "= 반복 변수")
print()

#리스트와 범위
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))

#역반복문

##방법1
for i in range(4, -1, -1):
    print("현재 반복 변수: {}".format(i))
print()

##방법2
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
print()

#while 무한 반복

# while True:
#     print(".", end="") ##end="" : 줄바꿈 일어나지 않게함 // 강제종료 ctrl+c

#while반복문을 for처럼 사용
i = 0
while i < 10 :
    print("{}번째 반복입니다.".format(i))
    i += 1

#해당하는 값 모두 제거하기
list_test = [1, 2, 1, 2]
value = 2

while value in list_test:
    list_test.remove(value)

print(list_test)

#5초동안 반복하기

##유닉스 타임(Unix Time) : 1970년 1월 1일 0시 0분 0초 기준으로 몇 초가 지났는지 정수로 나타낸것 >> import itme / time.time()
import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("5초 동안 {}번 반복했습니다.".format(number))

#break

i = 0

while True: ##무한반복
    print("{}번째 반복문입니다.".format(i))
    i = i + 1

    input_text = input("> 종료하시겠습니까?(y/n): ")
    if input_text in ["y", "Y"] :
        print("반복을 종료합니다.")
        break

#continue 

numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10 :
        continue 
    print(number) ##continue 사용시 if number >= 10 에 비해 들여쓰기 하나를 줄일 수 있다

    