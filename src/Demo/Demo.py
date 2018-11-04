import csv
import os
import random
import socket
import time


# installation parameters
tile_group = 7
group_row = 27
group_col = 27

# connection parameters
host = '127.0.0.1'
port = 10002
demoSocket = socket.socket()
demoSocket.connect((host, port))


def col_color(col=0, color=0):
    """Generate msg to change all tiles in a col."""
    tile_list = []
    for i in range(tile_group):
        for j in range(group_row):
            tile_list.append("{}-{}-{}".format(i, col, j))
    msg = ','.join(tile_list) + "=" + str(color)
    return msg


def demo_col_rolling():
    """Demo col rolling."""
    for i in range(group_col):
        result = ''
        while result != 'OK':
            demoSocket.send(col_color(i, 0).encode())
            result = demoSocket.recv(1024).decode()
            print("Received from server: "+result)

        # pause for 1 second
        time.sleep(1)


def reset():
    """Reset all tiles to 255"""
    for i in range(group_col):
        result = ''
        while result != 'OK':
            demoSocket.send(col_color(i, 255).encode())
            result = demoSocket.recv(1024).decode()
            print("Received from server: "+result)


def demo_noise():
    """Randomize all pixels."""
    msg_list = []
    for i in range(tile_group):
        for j in range(group_col):
            for k in range(group_row):
                msg_list.append(
                    '{}-{}-{}={}'.format(
                        i, j, k, random.randint(0, 255))
                )

    msg = '&'.join(msg_list)
    demoSocket.send(msg.encode())
    data = demoSocket.recv(1024).decode()
    print("Previously Received from server: "+data)


def demo_noise_loop():
    """Randomize all pixels one by one for testing."""
    for i in range(tile_group):
        for j in range(group_col):
            for k in range(group_row):
                result = ''
                while result != 'OK':
                    demoSocket.send(
                        '{}-{}-{}={}'.format(
                            i, j, k, random.randint(0, 255)
                        ).encode()
                    )
                    result = demoSocket.recv(1024).decode()
                    # print("Received from server: " + result)


'''
def demo_load_image():
    """Load image to display."""
    from PIL import Image
    img = Image.open("example.jpg")
    pix = img.load()
    img_width, img_height = img.size
    for i in range(tile_group):
        for j in range(group_row):
            for k in range(group_col):
                pass
'''


def load_csv():
    """Load csv file for tiles color"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    p = os.path.join(script_dir, "example.csv")
    with open(p, 'r') as fp:
        csv_reader = csv.reader(fp)
        for i, row in enumerate(csv_reader):
            row_val = []
            for j, val in enumerate(row):
                row_val.append("{}-{}-{}={}".format(
                    i//group_row,
                    j,
                    i-(i//group_row)*group_row,
                    val))
            result = ''
            while result != 'OK':
                demoSocket.send('&'.join(row_val).encode())
                result = demoSocket.recv(1024).decode()


def cmd_interpreter(cmd):
    """Interpret commands"""
    if cmd == "demo1":
        demo_col_rolling()
    elif cmd == "demo2":
        demo_2()
    elif cmd == "noise":
        demo_noise()
    elif cmd == "noise_loop":
        demo_noise_loop()
    elif cmd == "csv":
        load_csv()
    elif cmd == "reset":
        reset()
    else:
        demoSocket.send(cmd.encode())
        data = demoSocket.recv(1024).decode()
        print('Received from server: ' + data)

    return True


def demo_2():
    """Change one pixel"""
    msg = "1-1-1=2"
    demoSocket.send(msg.encode())
    data = demoSocket.recv(1024).decode()
    print('Received from server: ' + data)


def main():
    demoSocket.send("test".encode())
    data = demoSocket.recv(1024).decode()
    print('Received from server: ' + data)

    while True:
        command = ""
        while command == "":
            command = input(" -> ")

        # terminate connection if cmd == q
        if command == "q":
            demoSocket.send('q'.encode())
            demoSocket.close()
            break

        cmd_interpreter(command)


if __name__ == '__main__':
    main()
