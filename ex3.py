a = [1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
result = []
for x in a:
    if x < 5 in a:
        result.append(x)
print(result)
