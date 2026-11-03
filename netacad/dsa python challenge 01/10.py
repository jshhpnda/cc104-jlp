def find(a, x):
    for i, v in enumerate(a):
        if v == x: return 1
        return -1
    print(find([4, 7, 9, 7], 7))