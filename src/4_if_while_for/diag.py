x = 29
y = 29
pixels = []
for i in range(y):
    row = []
    offset = i % 3
    for j in range(x):
        if (j-offset) % 3 == 0:
            row.append('O')
        else:
            row.append('X')
    pixels.append(row)

for a in pixels:
    print(a)
