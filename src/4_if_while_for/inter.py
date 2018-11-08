x = 20
y = 20
pixels = []

for i in range(y):
    row = []
    k = (-1) ** i
    for j in range(x):
        if k*((-1)**j) < 0:
            row.append('O')
        else:
            row.append('X')

    pixels.append(row)

for a in pixels:
    print(a)
