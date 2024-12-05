import modules.data as m_data 
import socket

# создамо функцію для відправкм даних на сервер
def send(data):
    # відправляємо дані серверу
    client.sendall(data)

def activate():
    global client
    print('lod')
    try:
        # создаємо клієнта
        print('hello')
        client = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        print('hi')
        # шифруємо поле гри
        ships = "field:"
        for ship in m_data.all_ships:
            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
        print('just')
        # підключаємо кліента до сервера
        client.connect((m_data.ip, 8800))
        print("it is cool",m_data.ip)
        # визиваємо функцію для відправки даних на сервер
        send(ships.encode())
        print("it's cool")
    except:
        # переходимо до серверу
        print('hahhaahha')
        activate()
        