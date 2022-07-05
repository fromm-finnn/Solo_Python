#재귀함수

##반복문으로 팩토리얼 구하기
def factorial(n):
    output = 1
    for i in range(1, n+1):
        output *= i
    return output

print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))
print()

##재귀함수로 팩토리얼 구하기
def factorial(n):
    if n == 0:
        return 1
    else :
        return n * factorial(n - 1)

for i in range (1, 100):
    print(i,factorial(i))

for i in range(1, 100):
    print(i, 2**i)
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))
print()

##재귀함수로 피보나치수열 구현 - 계산시간 오래걸림
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci(1):", fibonacci(1))
print("fibonacci(2):", fibonacci(2))
print("fibonacci(3):", fibonacci(3))
print("fibonacci(4):", fibonacci(4))
print("fibonacci(5):", fibonacci(5))
print()


##재귀함수로 피보나치수열 구현(2)
counter = 0

def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter ##파이썬은 함수 외부에 있는 변수를 참조하지 못함 > global로 해결
    counter += 1
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))
print()

##메모화
dictionary = {              ##메모변수 만든다
    1: 1,
    2: 1,
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n] ##메모 되어 있으면 메모된 값을 리턴
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output       ##메모 되어 있지 않으면 값을 구한다

print("fibonacci(10):", fibonacci(10))
print("fibonacci(20):", fibonacci(20))
print("fibonacci(30):", fibonacci(30))
print("fibonacci(40):", fibonacci(40))
print("fibonacci(50):", fibonacci(50))
print()
