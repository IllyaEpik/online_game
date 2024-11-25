import modules.data as m_data 
import socket, io,threading, pygame

# client_screen = Screen().run()
clock = pygame.time.Clock()
def activate():
    global client
    try:
        client = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        ships = "field:"
        for ship in m_data.all_ships:
            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
        client.connect((m_data.ip, 8800))
        send(ships.encode())
    except:
        activate()
    # [['1',9,6], ['2',1,1]]# "'1',9,6 '2',1,1"

def send(data):
    print("attack")
    client.sendall(data)