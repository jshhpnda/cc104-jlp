def linear_search(items, target):
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1

print(linear_search([10, 4, 12, 8], 12))  # Output: 2