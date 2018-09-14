a,b =map(int, input().split(' '))
result = (a - b)
if result%10 < 9:
    result = result + 1
else:
    result = result - 1
print(result)
