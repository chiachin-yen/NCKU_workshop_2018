i = 10
a = 0
min = 0
max = 100
game_over = False

while not game_over:
	a = input("Guess a number:")
	if int(a) > i:
		print("That number is smaller than ", a, " ,but larger than ", str(min))
		max = a
	elif int(a) < i:
		print("That number is smaller than ", str(max), " ,but larger than ", a)
		min = a
	elif int(a) == i:
		print("You Lose")
		game_over = True
		
print("Game Over")