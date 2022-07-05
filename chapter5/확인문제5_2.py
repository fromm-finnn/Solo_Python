#1번! - 평탄화

def flatten(data):
    output = []
    print(output)
    for data in data:
        if type(data) == list:
            print(output)
            output += flatten(data)
        else :
            output.append(data)
    return output 
    

example = [[1,2,3],[4,[5,6]],7,[8,9]]
print("원본:", example)
print("변환:", flatten(example))

#2번!
min_sit = 2
max_sit = 10
total = 100
memo = {}

def div(remain,sit):
    key = str((remain, sit))
    #종료조건
    if key in memo:
        return memo[key]
    if remain == 0:
        return 1            #유효하므로 수를 세기 위해 1을 리턴
    if remain < 0:
        return 0            #무효이므로 0을 리턴
    
    #재귀 처리
    count = 0
    for i in range(sit, max_sit+1):
        count += div(remain-i, i)

    #메모 처리
    memo[key] = count
    return count

print(div(total,min_sit))