T = int(input())

for t in range(T):
    G = int(input())
    for i in range(G):
        I,N,Q = map(int, input().split())
        if I==Q:
            print(N//2)
        else:
            print((N+1)//2)
