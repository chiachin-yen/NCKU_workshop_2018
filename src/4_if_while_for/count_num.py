counts = 0
i = 1

while i < 10000:
    if '1' in str(i):
        counts += 1
    i += 1

print(counts)
