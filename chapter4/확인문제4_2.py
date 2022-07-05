#1번
dict_a = {}
dict_b = {"name":"구름"}

print("dict_a :",dict_a)
print("dict_b :",dict_b)
print()

print("dict_a랑 dic_b 바꾸기")
print()
dict_a["name"] = "구름"
del dict_b["name"]

print("dict_a :",dict_a)
print("dict_b :",dict_b)
print()

#2번
pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 3},
    {"name" : "아지", "age" : 1},
    {"name" : "호랑이", "age" : 1}
]

print("# 우리 동네 애완 동물들")

for i in pets :
    print(i["name"], str(i["age"])+"살") # *age랑 살 사이에 빈칸 없에기 / 방법1
    print("{} {}살".format(i["name"], i["age"])) # 방법2

print()

#3번
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}



for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
print()

#4번
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트",
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for item in character[key]:
            print("{} :".format(item), character[key][item])
    elif type(character[key]) is list:
        for skill in character[key]:
            print("skill : {}".format(skill))
    else :
        print("{} :".format(key), character[key])
