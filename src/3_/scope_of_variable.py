# This is a global variable
a = 0

if a == 0:
    # This is still a global variable
    b = 1


def my_function(c):
    # this is a local variable
    d = 3
    a = 99999
    print("a is ", a)
    print("c is ", c)
    print("d is ", d)


# Now we call the function, passing the value 7 as the first and only parameter
print("========Start of Function Call==========")
my_function(7)
print("========End of Function Call==========")

# a and b still exist
print('a is ', a)
print('b is ', b)

print('-' * 20)

# c and d don't exist anymore -- these statements will give us name errors!
print("c is ", c)
print("d is ", d)
