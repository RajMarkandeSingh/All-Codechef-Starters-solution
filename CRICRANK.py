for i in range(int(input())):
    a,b,c=map(int,input().split())
    x,y,z=map(int,input().split())
    c1=0
    c2=0
    if a>x:
        c1+=1
    else:
        c2+=1
    if b>y:
        c1+=1
    else:
        c2+=1
    if c>z:
        c1+=1
    else:
        c2+=1
    if c1>c2:
        print("A")
    else:
        print("B")
