nums = [2, 7, 11]
target = 9
seen = set()
for x in nums:
    if target - x in seen:
        print(x)
        break
    seen.add(x)