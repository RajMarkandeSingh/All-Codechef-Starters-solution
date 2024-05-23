for i in range(int(input())):
    a,b=map(int,input().split())
    val=float((6-(a+b))/6)
    if val==0:
        print(0)
    else:
        print(round(val,6))
