import modules.data as m_data 
import socket, io,threading, pygame

# client_screen = Screen().run()
clock = pygame.time.Clock()
def activate():
    global client
    try:
        print('ewqerweq')
        client = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        print('ewqerweq1')

        # with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client:
        ships = "field:"
        print('ewqerweq2')

        for ship in m_data.all_ships:
            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
        print('ewqerweq3')

        print(m_data.ip)
        client.connect((m_data.ip, 8800))
        print('ewqerweq4')

        send(ships.encode())
        print('ewqerweq5')

    except:
        print('')
        activate()
    # [['1',9,6], ['2',1,1]]# "'1',9,6 '2',1,1"

def send(data):
    client.sendall(data)