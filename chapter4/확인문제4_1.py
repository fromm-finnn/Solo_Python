#2번 

numbers = [273,103,5,32,65,9,72,800,99]

for number in numbers :
    if number >= 100 :
        print("-100 이상의 수 : {}".format(number))

print()

#3번

# for i in numbers :
#     if i % 2 == 0 :
#         print("{}는 짝수입니다".format(i))
#     else:
#         print("{}는 홀수입니다".format(i))

Holzzak = ["짝수", "홀수"]

for i in numbers :
    print("{}는 {}입니다".format(i, Holzzak[i % 2]))

print()

for j in numbers:
    print("{} 는 {}자릿수입니다.".format(j,len(str(j))))

#4번

list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9,],
]

for i in list_of_list:
    for j in i:
        print(j)
print()

#5번 (list 안에서 연산할때 나누기(/)는 float 형태로 나와서 사용 못함)
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[number % 3 - 1 ].append(number)

print(output)


#피라미드 만들기

numbers = [1,2,3,4,5]
for i in numbers :
        print(" " * (5-i) , "*" * ((i*2)-1))












