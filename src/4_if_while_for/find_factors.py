def list_all_factor(x):
    factors = []
    for i in range(1, int(x/2)+1):
        if x % i == 0:
            factors.append(i)

    return factors


num = input("number to find factors: ")
print(list_all_factor(int(num)))
