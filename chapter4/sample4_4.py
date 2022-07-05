#리스트 함수 min(), max(), sum()

import enum
from unicodedata import east_asian_width


numbers = [103, 52, 273, 32, 77]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print()

print(min(103, 52, 273, 32, 77),"\n{}".format(max(103, 52, 273, 32, 77)))
print()

#reversed()

list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]) :", list_reversed)
print("list(reversed([1, 2, 3, 4, 5]) :", list(list_reversed))
print()

print("# reversed() 함수와 반복문")
print("for i in reversed([1,2,3,4,5]):")
for i in reversed(list_a):
    print("-", i)

##revesed()함수는 제너레이터 : 반복문과 조합할 때 함수의 결과를 여러 번 활용하지 않고 for 구문 내부에 revered()함수를 곧바로 넣어서 사용
numbers = [1, 2, 3, 4, 5, 6]

for i in reversed(numbers):
    print("첫 번째 반복문: {}". format(i))

for i in reversed(numbers):
    print("두 번째 반복문: {}". format(i))
print()

temp = reversed(numbers)

for i in temp:
    print("첫 번째 반복문: {}". format(i))

for i in temp:
    print("두 번째 반복문: {}". format(i)) ## 두번째 반복문은 출력이 안된다
print()

#확장 슬라이싱 (뒤집는 다른 방법) [::-1]
numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])
print("안녕하세요"[::-1])
print()

#enumerate() - enumerate(리스트)
example_list = ["요소A", "요소B", "요소C"]

print("# 단순 출력")
print(example_list)
print()

print("# enumerate() 함수 적용 출력") ##이터레이터
print(enumerate(example_list))
print()

print("# list()함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문과 조합하기")
for i, value in enumerate(example_list): ##enumerate()사용시 반복 변수를 i, value와 같이 넣을 수 있다
    print("{}번째 요소는 {}입니다.".format(i,value))
print()

#items() - 딕셔너리.item()
example_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C",
}

print("# 딕셔너리의 items() 함수")
print("items():", example_dictionary.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))
print()

#리스트 내포

##방법1 - 반복문 단순 사용
array = []

for i in range(0,20,2):
    array.append(i * i)
print(array)
print()

##방법2 - 리스트 안에 for문 사용
array = [i * i for i in range(0,20,2)]

print(array)
print()

##방법3 - 조건을 활용한 리스트 내포
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)
print()

#심화 1 - 구문 내부에 여러 줄 문자열을 사용했을 때의 문제점

##if 조건문과 여러 줄 문자열(1) - 예상치 못한 들여쓰기가 들어간다
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 짝수입니다.""".format(number, number))

else :
    print("""\
        입력한 문자열은 {}입니다.
        {}는(은) 홀수입니다.""".format(number, number))
print()

##if 조건문과 여러 줄 문자열(2) - 코드 구조가 이상하다
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("""입력한 문자열은 {}입니다.
{}는(은) 짝수입니다.""".format(number, number))

else :
    print("""입력한 문자열은 {}입니다.
{}는(은) 홀수입니다.""".format(number, number))
print()

##if 조건문과 긴 문자열 - 코드가 복잡해진다
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))

else :
    print("입력한 문자열은 {}입니다.\n{}는(은) 홀수입니다.".format(number, number))
print()

##괄호로 문자열 연결하기
test = (
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어 "
    "생성됩니다."
)

print("test:", test)
print("type(test):", type(test))
print()

##여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(1)
number = int(input("정수 입력> "))

if number % 2 == 0:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 짝수입니다."
    ).format(number, number))

else :
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}는(은) 홀수입니다."
    ).format(number, number))
print()

##join() - 문자열.join(문자열로 구성된 리스트)
print(":".join(["1", "2", "3", "4", "5"]))
print()

##여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결(2)
number = int(input("정수 입력> "))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 짝수입니다."
    ]).format(number, number))

else :
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}는(은) 홀수입니다."
    ]).format(number, number))
print()

#심화 2 - 이터레이터

##이터러블 : 리스트, 딕셔너리, 튜플처럼 내부에서 요소를 차례차례 꺼낼 수 있는 것
##이터레이터 : 이터러블 중에서 next()함수를 적용해 하나하나 꺼낼 수 있는 요소
##쓰는 이유 : 메모리의 효율성을 위해서 리스트를 바로 리턴 하는 것이 아니라 이터레이터를 리턴하고 next를 사용해서 요소 하나하나를 리턴한다

##reversed()함수와 이터레이터
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
