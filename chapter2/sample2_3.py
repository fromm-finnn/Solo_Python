#변수 선언과 할당
pi = 3.14159265
r = 10

#변수참조
print("원주율 = ", pi)
print("반지름 = ", r)
print("원의 둘레 = ", 2*pi*r)
print("원의 넓이 = ", pi * (r**2))
print()

number = 100
number += 10 #110
number -= 20 #90
number *= 30 #2700
number /= 90  #30
number %= 7  #2
number **=3  #8
print("number = ", number)
print()
string = "안녕하세요"
string += "!"
string += "!"
print("string = ", string)
print()

string = input("입력 :")
print("자료 :",string)
print("자료형 :",type(string))
print("입력 + 100 :", int(string) + 100)
print()

string_a = input("입력 A : ")
int_a = int(string_a)
string_b = input("입력 B : ")
int_b = int(string_b)
string_c = input("입력 C : ")
float_c = float(string_c)

print("문자열 자료 :", string_a + string_b)
print("숫자 자료 : ", int_a + int_b)

print(type(int("52")))

print("덧셈결과 :", int_a + float_c)
print("뺄셈결과 :", int_a - float_c)
print("곱셈결과 :", int_a * float_c)
print("나눗셈결과 :", int_a / float_c)

str_a = str(int_a)
print(str_a)
print(type(str_a))


