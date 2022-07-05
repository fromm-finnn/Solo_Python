# format() 함수로 숫자를 문자열로 변환하기
string_a = "{}".format(10)

print(string_a)
print(type(string_a))
print()

format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)
print()

#정수를 특정 칸에 출력하기
num_a = "{:d}".format(52)
num_b = "{:5d}".format(52)
num_c = "{:10d}".format(52)
num_d = "{:05d}".format(52)
num_e = "{:05d}".format(-52)

print("# 기본")
print(num_a)
print()
print("# 특정 칸에 출력하기")
print(num_b)
print(num_c)
print()
print("# 빈칸을 0으로 채우기")
print(num_d)
print(num_e)
print()

#기호와 함께 출력하기
num_f = "{:+d}".format(52)
num_g = "{:+d}".format(-52)
num_h = "{: d}".format(52)
num_i = "{: d}".format(-52)

print("기호와 함께 출력하기")
print(num_f)
print(num_g)
print(num_h)
print(num_i)
print()

#조합하기
num_h = "{:+5d}".format(52)
num_i = "{:+5d}".format(-52)
num_j = "{:=+5d}".format(52)
num_k = "{:=+5d}".format(-52)
num_l = "{:+05d}".format(52)
num_m = "{:+05d}".format(-52)


print("#조합하기")
print(num_h)
print(num_i)
print(num_j)
print(num_k)
print(num_l)
print(num_m)
print()

#float format
float_a = "{:f}".format(52.273)
float_b = "{:15f}".format(52.273)
float_c = "{:+15f}".format(52.273)
float_d = "{:+015f}".format(52.273)

print(float_a)
print(float_b)
print(float_c)
print(float_d)
print()

#소숫점 지정

float_e = "{:15.3f}".format(52.273)
float_f = "{:15.2f}".format(52.273)
float_g = "{:15.1f}".format(52.273)

print(float_e)
print(float_f)
print(float_g)
print()

#의미 없는 소수점 제거
float_h = 52.0
float_i = "{:g}".format(float_h)

print(float_h)
print(float_i)
print()

#대소문자로 바꾸기

a = "Hello Python Programming"
print(a.upper())
print(a.lower())
print()

#문자열 공백 제거하기

input_a = """
    안녕하세요  
문자열의 함수를 알아봅시다
"""

print(input_a)
print(input_a.strip())
print()

# isoo

print("TrainA10".isalnum())
print("TrainA10".isalpha())
print("TrainA10".isdigit())
print("TrainA10".islower())
print()

#문자열 찾기

find_a = "안녕안녕하세요".find("안녕")
print(find_a)

rfind_a = "안녕안녕하세요".rfind("안녕")
print(rfind_a)
print()

#in 연산자

print("안녕" in "안녕하세요")
print("안녕" in "잘주무세요")

#split

split_a = "10 20 30 40 50".split(" ")
print(split_a)