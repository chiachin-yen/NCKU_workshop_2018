def is_prime(x):
    factors = []
    for i in range(1, int(x/2)):
        if x % i == 0:
            factors.append(i)
    if len(factors) == 1:
        return True
    else:
        return False


num = int(input("Number to check:"))
if is_prime(num):
    print(num, "is prime.")
else:
    print(num, "is not prime.")