#함수의 기본

##기본적인 함수
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()
print()

##매개변수의 기본 - 매개변수 수 안맞으면 TypeError 뜸
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)
print()

##가변 매개변수  - 1. 가변 매개변수 뒤에 일반 매개변수 올 수 없음 2. 가변 매개변수는 하나만 사용 가능
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

##기본 매개변수 - 1. 기본 매개변수 뒤에 일반 매개변수 올 수 없음 
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요") ##n을 입력하지 않으면 2가 기본값으로 들어감 
print()

##키워드 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)

##여러 함수 호출 형태
def test(a, b=10, c=100):
    print(a + b + c)

test(10,20,30)
test(a=10, b=100, c=200)
test(c=10, a=100, b=200)
test(10, c=200)
print()

##자료없이 리턴하기
def return_test():
    print("A 위치입니다.")
    return                  ##return 1. 함수를 실행했던 위치로 돌아가라 2. 함수를 여기서 끝내라
    print("B 위치입니다.")

return_test()
print()

##자료와 함께 리턴하기
def return_test():
    return 100

value = return_test()
print(value)
print()

##아무것도 리턴하지 않았을 때
def return_test():
    return

value = return_test()
print(value)
print()

##범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output=0
    for i in range(start, end + 1):
        output += i
    return output 

print("0 to 100:", sum_all(0,100))
print("0 to 1000:", sum_all(0,1000))
print("50 to 100:", sum_all(50,100))
print("500 to 1000:", sum_all(500,1000))
print()

##기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))