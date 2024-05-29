def sum_of_modes(s):
    n = len(s)
    ans = n * (n + 1) // 2
    cnt = {0: 1}
    ac,bc =0,0
    for c in s:
        if c == '0':
            ac+= 1
        else:
            bc += 1
        val=ac-bc
        if val in cnt:
            ans += cnt[val]
            cnt[val] += 1
        else:
            cnt[val] = 1
    return ans
for i in range(int(input())):
    n=int(input())
    s=input()
    print(sum_of_modes(s))
