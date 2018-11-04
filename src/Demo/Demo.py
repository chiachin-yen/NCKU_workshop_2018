import socket

tile_group = 7
group_row = 27
group_col = 27


def col_color(col=0, color=0):
    """Change all tiles in a col."""
    tile_list = []
    for i in range(tile_group):
        for j in range(group_row):
            tile_list.append("{}-{}-{}".format(i, col, j))
    msg = ','.join(tile_list) + "=" + str(color)
    return msg


def cmd_interpreter(cmd):

    if cmd == "":
        cmd = ""
    elif cmd == "r":
        cmd = "reset"
    elif cmd == "demo1":
        cmd = col_color(2, 0)
    elif cmd == "demo2":
        pass

    return cmd


def demo_2():
    message = "1-1-1=2"
    demoSocket.send(message.encode())


def main():

    message = ""
    while message == "":
        message = input(" -> ")

    while message != 'q':
        message = cmd_interpreter(message)
        demoSocket.send(message.encode())
        data = demoSocket.recv(1024).decode()

        print('Received from server: ' + data)

        # Get new command
        message = input(" -> ")
        while message == "":
            message = input(" -> ")

    demoSocket.send(message.encode())
    demoSocket.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 10002

    demoSocket = socket.socket()
    demoSocket.connect((host, port))
    main()
