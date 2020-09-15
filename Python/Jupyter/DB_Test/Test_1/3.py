# from copy import copy, deepcopy
import copy

# L = [[1, 2, 3], [4, 5, 6]]
# A = L
# S = copy.copy(L)
# D = copy.deepcopy(L)

# L[0][1] = 10
# print("L is ", L)
# print("A is ", A)
# print("S is ", S)
# print("D is ", D)

# a = [1, [1, 2, 3]]
# b = copy.copy(a)    # shallow copy 발생
# print(b)    # [1, [1, 2, 3]] 출력
# a[0] = 100
# print(b)    # [100, [1, 2, 3]] 출력,
# print(a)    # [1, [1, 2, 3]] 출력, shallow copy 가 발생해 복사된 리스트는 별도의 객체이므로 item을 수정하면 복사본만 수정된다. (immutable 객체의 경우)

a = [1, 2, 3, 4]
b = copy.copy(a)     # shallow copy
print(b)    # [1, 2, 3, 4]
b[2] = 100   # b의 item 변경
print(b)    # [1, 2, 100, 4]
print(a)    # [1, 2, 100, 4], a의 item도 수정됨!!