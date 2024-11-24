import socket
import modules.data as m_data
import threading 
import modules.ships as m_ships
# from .main_window import Screen

# server_screen = Screen().run()
# server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
# ip = "127.0.0.1"
# ip = '46.118.25.208'
print(ip)
print(hostname)
def activate():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server:
        server.bind((f"{ip}", 8800))
        server.listen()
        client = server.accept()
        print("Acept_Client")
        client_data = client[0].recv(1024).decode()
        print('1231212312312123')
        print(client_data)
        data = client_data.split(":")
        print('GOOD')
        if data[0] == "field":
            print('GOOD1')
            data = data[1].split(" ")
            for ship in data:
                splited_data = ship.split(",")
                print('create ship')
                print(splited_data)
                m_ships.Ship(x = 724,y = 115,
                             field_cor = (724,115),
                             name  = splited_data[0],
                             row = int(splited_data[1]),
                             cell = int(splited_data[2]),
                             rotate = int(splited_data[3]))
        m_data.enemy_data.append(client_data)
        
# 127.0.0.1
# activate()