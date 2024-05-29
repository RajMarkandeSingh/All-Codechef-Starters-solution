for _ in range(int(input())):
    s = input()
    l, r, u, d = 1, 1, 1, 1
    if s[0] == '0':
        l = 0
    if s[1] == '0':
        r = 0
    if s[2] == '0':
        u = 0
    if s[3] == '0':
        d = 0
    print((l*10 + r*10 + 1) * (u*10 + d*10 + 1))
