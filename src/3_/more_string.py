"""More about string."""

# Explicitly references the third positional argument
line_1 = "First of the arguments is {2}"

# Implicitly references the first positional argument
line_2 = "Bring me that {}"

# Same as "From {0} to {1}"
line_3 = "From {} to {}"

# References keyword argument 'name'
line_4 = "My name is {name}"

# First element of keyword argument 'players'.
line_5 = "Winner is: {players[0]}"

print(line_1.format("Apple", "Book", "Cat"))
print(line_2.format("Apple", "Book", "Cat"))
print(line_3.format(0, "99"))
print(line_4.format(name='john'))

player_list = ["Player A", "Player B"]
print(line_5.format(players=player_list))
