num=int(input())
for i in range(1,num+1):
    m=list(map(int,input().split()))
    if max(m)==1:
        print("OUT")
    else:
        print("IN")
