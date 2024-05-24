for i in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    c=0
    for i in l:
        val=max(i-1,m-i)
        c+=val
    print(c)
