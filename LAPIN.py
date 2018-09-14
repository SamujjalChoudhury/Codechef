T = int(input())

def odd(s):
    print(s)

for t in range(T):
    s = str(input())
    if len(s)%2==0:
        first = []
        second = []

        for i in range(0, len(s)//2):
            first.append(s[i])
        for i in range((len(s)//2), len(s)):
            second.append(s[i])
        first.sort()
        second.sort()
        if first==second:
            c = 'YES'
        else:
            c = 'NO'
    else:
        first = []
        second = []

        for i in range(0, len(s)//2):
            first.append(s[i])
        for i in range((len(s)+1)//2, len(s)):
            second.append(s[i])
        first.sort()
        second.sort()
        if first==second:
            c = 'YES'
        else:
            c = 'NO'

    print(c)
