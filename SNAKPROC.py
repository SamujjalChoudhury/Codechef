test = int(input())

for j in range(test):
    temp = int(input())
    txt = str(input())
    flag = 0
    for i in range(temp):
        if txt[i] == 'H':
            if(flag == 0):
                flag = 1
            else:
                flag = 1
                break
        elif txt[i] == 'T':
            if(flag==1):
                flag = 0
            else:
                flag = 1
                break
    if flag==0:
        print("Valid")
    else:
        print("Invalid")
