from functools import reduce

# lst = [1, -3, 2, 0, -5, 6]

# print(list(map(lambda x: x ** 2, lst)))
# print(list(map(lambda x: x * 2, lst)))
# print(list(filter(lambda x: x > 2, lst)))
# print(list(filter(lambda x: x % 2, lst)))
# print(reduce(lambda x, y: x + y, lst))

print(reduce(lambda x, y: y + x, "hello"))
print(type(reduce(lambda x, y: y + x, "hello")))
print(list.reverse("hello"))
print(list(reversed("hello")))
print(type(list(reversed("hello"))))
