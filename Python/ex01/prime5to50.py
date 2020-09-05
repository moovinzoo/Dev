# Check if former devided by latter
def is_former_divisor_of_latter(n, m):
    return (n % m == 0)

# Check if it is prime number, only works in [5,50]
def is_prime(n):
    cnt = 0
    for i in range(2, n):
        if (is_former_divisor_of_latter(n, i)):
            cnt += 1
    return (cnt == 0)

# from 5 to 50
for i in range(5, 51):
    if is_prime(i):
        print('%d is a prime number' %i)
