#튜플 - 리스트와 달리 값이 고정됨

##요소를 하나만 가지는 튜플 - (value, ) 

##리스트와 튜플의 특이한 사용
[a,b] = [10,20]
(c,d) = (10,20)

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print()

##괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

a,b,c = 10,20,30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)
print()

##변수의 값을 교환하는 튜플
a,b = 10,20

print("# 교환 전 값")
print("a:",a)
print("b:",b)
print()

a,b = b,a

print("# 교환 후 값")
print("a:",a)
print("b:",b)
print()

##여러 개의 값 리턴하기
def test():
    return (10,20)

a,b = test()

print("a:",a)
print("b:",b)
print()

##divmod()
a,b = 97,40 
print(divmod(a, b)) ##(a // b, a % b)

##함수의 매개 변수로 함수 전달하기
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)
print()

##map()함수와 filter()함수
def power(item):
    return item*item
def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a) ##리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트(str)를 구성
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a) ##제너레이터가 출력됨
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a) ##리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트를 구성
print("# filter() 함수의 실행결과")
print("filter(power, list_input_a):", output_b) ##제너레이터가 출력됨
print("filter(power, list_input_a):", list(output_b))
print()

#람다 - lambda 매개변수: 리턴값 - 함수를 쉽게 선언
power = lambda x: x*x
under_3 = lambda x: x<3

list_input_a = [1,2,3,4,5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a) 
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(power, list_input_a):", output_b) 
print("filter(power, list_input_a):", list(output_b))
print()

##인라인 람다
list_input_a = [1,2,3,4,5]

output_a = map(lambda x : x * x, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a) 
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(lambda x : x < 3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(power, list_input_a):", output_b) 
print("filter(power, list_input_a):", list(output_b))
print()

#파일처리

##파일 열고 닫기
file = open("basic.txt", "w") ##basic.txt라는 폴더 생성 후 연다, "w" 새로쓰기 / "a" 이어쓰기 / "r" 읽기

file.write("Hello Python Programming")

file.close()

##with키워드
with open("basic.txt", "w") as file:
    file.write("Hellp Pythone Programming...!") ##with 구문이 종료될 때 자동으로 파일이 닫힘

##read()
with open("basic.txt", "r") as file:
    contents = file.read()

print(contents)

##랜덤하게 1000명의 키와 몸무게 만들기
import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt.", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        file.write("{}, {}, {}\n".format(name, weight, height))

##반복문으로 파일 한 줄씩 읽기
with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ") ##strip() : 공백제거 / split(‘구분자’) : 특정 구분자를 기준으로 나눔

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height)/ 100) **2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([                               ##'\n'.join() : 띄워쓰면서 합친다
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}",
        ]).format(name, weight, height, bmi, result))
        print()

#심화

##제너레이터 함수
def test():
    print("함수가 호출되었습니다.")
    yield "test"    #yield키워드는 제너러이터를 반환한다 - 대용량의 파일을 읽거나, 스트림 데이터를 처리할 때 유용하게 사용될 수 있다

print("A지점 통과")
test()

print("B지점 통과")
test()
print(test())
print()

##제너러이터 객체와 next() 함수
def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")

output = test()

print("D 지점 통과")
a = next(output)
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)
print(c)

next(output)


