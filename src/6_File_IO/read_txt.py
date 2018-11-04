"""Read Files in the same dir"""

with open("sample.txt", 'r', encoding='utf-8') as fp:
    file_content = fp.readlines()
    for row in file_content:
        print(row[0])
