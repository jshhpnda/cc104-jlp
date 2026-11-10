def bs(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        n = (lo + hi) // 2
        if a[n] == x:
            return n
        if a[n] < x:
            lo = n + 1
        else: 
            hi = n - 1
        return -1
    print(bs([2, 4, 6, 8, 10], 8))