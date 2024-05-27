for i in range(int(input())):
    a,b,c=map(int,input().split())
    val=[400//a,400//b,400//c]
    if max(val)==val[0]:
        print("ALICE")
    elif max(val)==val[1]:
        print("BOB")
    else:
        print("CHARLIE")
