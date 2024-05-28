for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    val=sum(l)
    print("YES" if val%2==0 else "NO")
