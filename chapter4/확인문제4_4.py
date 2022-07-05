##2진수 변환
print("{:b}".format(10))
print(int("1010", 2))
print()

##8진수 변환
print("{:o}".format(10))
print(int("12", 8))
print()

##16진수 변환
print("{:x}".format(10))
print(int("a", 16))
print()

#2번
output = [number for number in range(1,101) 
if "{:b}".format(number).count('0') is 1] ##count(str)이어야함. 괄호안에 int들어가면 안됨


for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))