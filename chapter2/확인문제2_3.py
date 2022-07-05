#확인문제 4번

str_input = input("숫자 입력 : ")
num_input = float(str_input)

print()
print(num_input, "inch")
print((num_input * 2.54), "cm")

#확인문제 5번

pi = 3.141592
rad_input = input("원의 반지름을 입력하시오 : ")
rad_output = float(rad_input)
print()
print("반지름 : ", rad_output)
print("원의 둘레 : ", 2 * pi * rad_output)
print("원의 넓이 : ", pi * (rad_output**2))

#확인문제 6번

a = input("문자열 입력 : ")
b = input("문자열 입력 : ")

print(a, b)
c = b
b = a 
a = c
print(a, b)

#확인문제 6번 더쉽게

a = input("문자열 입력 : ")
b = input("문자열 입력 : ")

print(a, b)
a , b = b , a
print(a, b)