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
print(ip)
print(hostname)
def activate():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server:
        server.bind((f"{ip}", 8800))
        server.listen()
        client = server.accept()
        print("Acept_Client")
        client_data = client[0].recv(1024).decode()
        data = client_data[-1].split(":")
        if data[0] == "field":
            data = data[1].split(" ")
            for ship in data: 
                splited_data = ship.split(",")
                m_ships.Ship(x = 724,y = 166,
                             field_cor = (724,166),
                             name  = splited_data[0],
                             row = splited_data[1],
                             cell = splited_data[2],
                             rotate = splited_data[3])
        m_data.enemy_data.append(client_data)
        
# 127.0.0.1
# activate()