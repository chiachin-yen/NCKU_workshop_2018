"""Nested List and more."""

nested_list = [["A", "B", "C"], ["X", "Y", "Z"]]
print(nested_list[0][1])

target = {'list_a': ['a1', 'a2', 'a3'], 'list_b': [
    'b1', 'b2'], 'dict_c': {'c1': ['c1-1', 'c2-2'], 'c2': 'c2-1'}}

# try to access a1
print(target['list_a'][0])
# try to access b1
print(target['list_b'][1])
# try to access c2-1
print(target['dict_c']['c1']['c1-1'])
