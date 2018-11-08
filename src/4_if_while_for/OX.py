panel = [['_']*3] * 3
game_over = False


def display():
    for row in panel:
        print(" ".join(row))


def who_win():
    """Check if there is a winner."""
    """check rows"""
    for i in range(3):
        if panel[i][0] == panel[i][1] and panel[i][0] == panel[i][2]:
            game_over = True
            return panel[i][0]

    """check columns"""
    for i in range(3):
        if panel[0][i] == panel[1][i] and panel[0][i] == panel[2][i]:
            game_over = True
            return panel[i][0]

    """Check Diagnal"""
    if panel[0][0] == panel[1][1] and panel[0][0] == panel[2][2]:
        game_over = True
        return panel[0][0]
    if panel[2][0] == panel[1][1] and panel[0][0] == panel[2][0]:
        game_over = True
        return panel[0][0]

    return ""


def fill():
    x = input("your placement ?")
    coor = x.split(',')
    print(coor)
    panel[int(coor[0])][int(coor[1])] = symbol


symbol = 'O'
winner = ''

while not game_over:
    if symbol == 'O':
        symbol = 'X'
    else:
        symbol = 'O'

    display()
    print("Now is " + symbol+"\'s turn")
    fill()
    winner = who_win()

print("winner is" + winner)
