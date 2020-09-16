def f15(lst):
    return sum([i for i, j in enumerate(lst) if j % 2 == 1])


result = f15([1, 2, 3, 4, 5])
print(result)
