# def f13(n):
#     cnt = 1
#     n /= 10
#     while (n > 0):
#         cnt += 1
#         n //= 10
#     print(cnt)

def f13(n):
    while n // 10 > 0:
        n //= 10
    return n


print(f13(9175))
print(f13(34))
print(f13(0))