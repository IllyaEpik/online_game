import modules.data as m_data 
import socket, pygame

# создамо функцію для відправкм даних на сервер
def send(data):
    # відправляємо дані серверу
    client.sendall(data)

def activate():
    global client
    try:
        # создаємо клієнта
        client = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        # шифруємо поле гри
        ships = "field:"
        for ship in m_data.all_ships:
            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
        # підключаємо кліента до сервера
        client.connect((m_data.ip, 8800))
        # визиваємо функцію для відправки даних на сервер
        send(ships.encode())
    except:
        # переходимо до серверу
        activate()