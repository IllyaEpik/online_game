import modules.data as m_data 
import socket, io,threading, pygame

# client_screen = Screen().run()
clock = pygame.time.Clock()
client = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
def activate():
    
    # with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client:
    client.connect((m_data.ip, 8800))
    ships = "field:"
    for ship in m_data.all_ships:
        ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
    send(ships.encode())
    # [['1',9,6], ['2',1,1]]# "'1',9,6 '2',1,1"

def send(data):
    client.sendall(data)