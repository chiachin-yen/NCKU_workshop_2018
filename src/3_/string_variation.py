the_string = 'Book'
the_list = ['B', 'o', 'o', 'k']

# 本質上不同
print("the_string == the_list ->", the_list == the_string)

# 有些'方法'相同
print("how many o in string", the_string.count('o'))
print("how many o in string", the_list.count('o'))

print("Position of o in string", the_string.index('o'))
print("Position of o in string", the_list.index('o'))

"""
the_string.append('s')
print("Position of o in string", the_string)
"""

# 常用的方法
print('the_string.split(\'o\') is', the_string.split('o'))
print('\'-\'.join(the_string) is', '-'.join(the_string))
print('\'-\'.join(the_list) is', '-'.join(the_list))
