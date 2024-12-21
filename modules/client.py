import modules.data as m_data 
import modules.server as m_server
import modules.ships as m_ships
import modules.images as m_images
import socket

# создамо функцію для відправкм даних на сервер
def send(data):
    # відправляємо дані серверу
    if m_data.client_server == "server":
        m_server.send(data)
    else:
        client.sendall(data)


client = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
def activate():
    global client
    print('lod')
    if not m_data.revenge:
        # создаємо клієнта
        print('hello')
        print('hi')
        # шифруємо поле гри
        ships = "field:"
        for ship in m_data.all_ships:
            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
        print('just')
        # підключаємо кліента до сервера
        client.connect((m_data.ip, 8800))
        print("it is cool", m_data.ip)
        # визиваємо функцію для відправки даних на сервер
        send(ships.encode())
        print("it's cool")
        m_data.revenge = True
        while not m_data.end:
            # Отримання данних кліенту та декодування їх
            client_data = client.recv(1024).decode()
            print(client_data)
            # Перетворення даних на список розділяючи символом :
            data = client_data.split(":")
            # Якщо списку всіх даних перше значення field,
            if data[0] == "field":
                # то друге значення зі списку буде розділен за пробілами
                data = data[1].split(" ")
                # Для кожного корабля у списку всіх даних
                for ship in data:
                    # Розділення кожного корабля по комі
                    splited_data = ship.split(",")
                    # Якщо розділенні данні кораблів пусті,
                    if splited_data != [""]:
                        print('create ship')
                        print(splited_data)
                        # то створюеться екземпляр класу корабля з переданими параметрами
                        ship = m_ships.Ship(x = 724,y = 115,
                                    field_cor = (724,115),
                                    name  = splited_data[0],
                                    row = int(splited_data[1]),
                                    cell = int(splited_data[2]),
                                    rotate = int(splited_data[3]),
                                    add = False)
                        
                        # Для кожного корабля первірка
                        for count in range(int(ship.name[0])):
                            # Якщо корабль не було повернуто
                            if ship.rotate % 180 == 0:
                                # Додаємо його частини в поле противника по рядку
                                m_data.enemy_field[ship.row][ship.cell+count] = int(ship.name[0])
                            # Інакше
                            else:
                                # Додаємо його частини в поле противника по стовпцю
                                m_data.enemy_field[ship.row+count][ship.cell] = int(ship.name[0])
                        
                        # Додаємо корабель до списку кораблів противника
                        m_data.enemy_ships.append(ship)

                for row in m_data.enemy_field:
                    print(row)

            # Перевірка, чи отримана команда "attack"
            elif data[0] == "attack":
                print("attack_get")
                # Отримуємо позицію атаки
                pos = data[1].split(" ")[0].split(",")
                pos = [int(pos[0]), int(pos[1])]
                # Перевірка, чи атака була промахом
                if data[1].split(" ")[-1] == "miss":
                    # Передаємо хід гравцю
                    m_data.turn = True
                    # Позначаємо промах на полі
                    m_data.my_field[pos[0]][pos[1]] = 7
                # Інакше
                else:
                    # Позначаємо влучання на полі
                    m_data.my_field[pos[0]][pos[1]] = 6
                    # for ship in m_data.all_ships:
                    #     yes_no = 0
                    #     cells = []
                    #     if ship in m_data.enemy_ships:
                    #         pass
                    #     else:
                    #         for count in range(int(ship.name[0])):
                    #             # Перевіряємо горизонтальне або вертикальне розміщення корабля
                    #             if ship.rotate % 180 == 0 and m_data.my_field[ship.row][ship.cell + count] != int(ship.name[0]):
                    #                 cells.append([ship.row, ship.cell + count])
                    #                 yes_no += 1
                    #             elif ship.rotate % 180 != 0 and m_data.my_field[ship.row + count][ship.cell] != int(ship.name[0]):
                    #                 cells.append([ship.row + count, ship.cell])
                    #                 yes_no += 1
                    #         if yes_no == int(ship.name):
                    #             pass
                # Створюємо обект класа картинки, власне картинку, для відображення результату атаки
                image = m_images.Image(
                    progression = "game",
                    name = data[1].split(" ")[-1],
                    x = 59+55.7*pos[1],
                    y = 115+55.7*pos[0],
                    width= 55.7,
                    height=55.7
                )
            # Перевірка, чи відбувся вибух
            elif data[0] == "explosion":
                # Отримуємо позицію вибуху
                pos = data[1].split(",")
                print(pos)
                # try:
                if len(pos[0]) > 1:
                    pos[0] = pos[0][0]
                if len(pos[1]) > 1:
                    pos[1] = pos[1][0]
                pos = [int(pos[0]), int(pos[1])]
                # except:
                # Перебираемо всі кораблі
                for ship in m_data.all_ships:
                    # Якщо це корабль противника пропускаємо
                    if ship in m_data.enemy_ships:
                        pass
                    # Якщо координати вибуху збігаються з позицією корабля,
                    elif ship.row == pos[0] and ship.cell == pos[1]:
                        # то відбуваеться вибух
                        ship.explosion = True
                        
            

            # Якщо відбуваеться програш
            elif data[0] == "lose":
                # То стан гри змінюеться на виграш
                m_data.progression = "lose"
            # Додаємо отримані дані від клієнта до списку даних противника
            m_data.enemy_data.append(client_data)
            print(client_data)
    