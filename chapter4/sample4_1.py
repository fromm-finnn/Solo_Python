#리스트

array = [273, 32, 103, "문자열", True, False]
print(array)
print()

array[0] = "변경"
print(array)
print()

print(array[3][0])
print()

array_b = [[1,2,3],[4,5,6],[7,8,9]]
print(array_b[1][1])
print()

#리스트 연산자

list_a = [1,2,3]
list_b = [4,5,6]

print("# 리스트")
print("list_a =", list_a)
print("list_b =", list_b)
print()

print("#리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 =", list_a * 3)
print()

print("#길이 구하기")
print("len(list_a) = ", len(list_a))
print()

#리스트에 요소 추가하기

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(0,10)
print(list_a)
print()

list_a = [1,2,3]
list_a.extend([4,5,6])
print(list_a)
print()

#리스트 연결 연산자와 요소 추가의 차이

list_a = [0,1,2,3,4,5]
print("# 리스트의 요소 하나 제거하기")

del list_a[1]
print("del list_a[1] : ", list_a)

list_a.pop(2)
print("pop(2):", list_a)
print()

list_b = [0,1,2,3,4,5,6]
del list_b[3:6]
print("del list_b[3:6] :", list_b)
print()

#remove : 값으로 제거하기

list_c = [1,2,1,2]
list_c.remove(2)
print(list_c)
print()

#clear : 전부제거

list_d = [0,1,2,3,4,5]
list_d.clear()
print(list_d)
print()

#in / not in

list_e = [1,48,273,55]
print(273 in list_e)
print(1 not in list_e)
print()

#for 반복문

array = [273,32,103,57,52]

for i in array :
    print(i)

print()

for j in "안녕하세요":
    print("-",j)

print()