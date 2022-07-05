#딕셔너리 선언

dict_a = {
    "name" : "어벤져스 엔드게임",
    "type" : "히어로 무비"
}

dict_b = {
    "director" : ["안소니 루소", "조 루소"],
    "cast" : ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"]
}

print(dict_a)
print(dict_a["name"])
print(dict_a["type"])
print()

print(dict_b)
print(dict_b["director"])
print()

#딕셔너리 요소 접근
print("*딕셔너리 요소에 접근하기*")
print()

##선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

##출력
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
print()

##값 변경
dictionary["name"] = "8D 건조망고"
print("name:", dictionary["name"])
print()

##자료 추가
dictionary["price"] = 5000
print(dictionary)
print()

##한개만 출력
print(dictionary["ingredient"][0])
print()

##제거
del dictionary["ingredient"]
print(dictionary)
print()

#딕셔너리 내부에 키가 있는지 확인하기
print("딕셔너리 내부에 키가 있는지 확인하기")
print()

##선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

##사용자로부터 입력
key = input("> 접근하고자 하는 키: ")

##출력
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")
print()

#get()함수
print("get()함수")
print()

##선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

##존재하지 않는 키에 접근
value = dictionary.get("존재하지 않는 키")
print("값:", value)

##None 확인
if value == None:
    print("존재하지 않는 키에 접근했습니다.")
print()

#for 반복문과 딕셔너리
print("for 반복문과 딕셔너리")
print()

##선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

##for 반복문 사용
for key in dictionary:
    print(key, ":", dictionary[key])