def f13(n):
    cnt = 1
    n /= 10
    while (n > 0):
        cnt += 1
        n //= 10
    print(cnt)


f13(9175)
f13(34)
f13(0)