a = 1
b = 1


for i in range(199):
    num = a + b
    a = b
    b = num
    print(num, b/a)
