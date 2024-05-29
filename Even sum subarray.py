def generate_continuous_subarrays(arr):
    n = len(arr)
    subs = []
    
    for st in range(n):
        for e in range(st, n):
            sub = arr[st:e+1]
            subs.append(sub)
    
    return subs

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = 0
    val = generate_continuous_subarrays(l)
    for i in range(len(val)):
        print(val[i])
        if sum(val[i]) % 2 == 0:
            v = len(val[i])
            if v > m:
                m = v
    print(m)
