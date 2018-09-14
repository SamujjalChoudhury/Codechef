case = int(input())
for test in range(case):
    horse = int(input())
    power = list(map(int, input().split()[:horse]))
    power.sort()
    result=[]
    for i in range(len(power)):
        if (1+i) == len(power):
            break
        result.append(power[i+1]-power[i])
    result.sort()
    print(result[0])
