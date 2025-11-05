left = [1, 7, 27, 36]
right = [3, 6, 15, 39]

# combine
combine = left + right

# bubble sort
n = len(combine)
for i in range(n):
    for j in range(0, n - i - 1):
        if combine[j] > combine[j + 1]:
            combine[j], combine[j + 1] = combine[j + 1], combine[j]

print(combine)
