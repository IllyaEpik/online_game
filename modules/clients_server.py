import modules.data as m_data 
import modules.ships as m_ships
import modules.images as m_images
import modules.buttons as m_buttons
import modules.transform as m_transform
import modules.achievements as m_achievements
import socket,random,os

# создамо функцію для відправкм даних на сервер
def send(data:bytes):
    # відправляємо дані серверу
    # if m_data.client_server == "server":
        # server1[0].sendall(data)
        # m_server.send(data)
    # else:
    try:
        client.sendall(data+[';'.encode()][0])
    except:
        client.sendall(f"{data};".encode())

hostname = socket.gethostname()
# Повертає IP адрессу по імені хосту
ip = socket.gethostbyname(hostname)
client_server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
# socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
def activate():
    global client
    print('lod')
    if not m_data.revenge:
        # шифруємо поле гри
        ships = f"field_nickname:{m_buttons.nickname.TEXT}:"
        for ship in m_data.all_ships:
            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
        if m_data.client_server == "server":
            client_server.bind(("0.0.0.0", 8800))
            # Функція listen активує очікування підключення користувача
            client_server.listen()
            # Підтверджуємо з'єднання від клієнту
            client = client_server.accept()[0]
            m_data.connected = True 
            for c in range(1000):
                print('HELLO server')
        if m_data.client_server == "client":
            # підключаємо кліента до сервера
            client = client_server
            client.connect((m_data.ip, 8800))
            for c in range(1000):
                print('HELLO client')
            
            print("it is cool", m_data.ip)
        # визиваємо функцію для відправки даних на сервер
        # send(f"".encode())
        for count in range(1000):
            print('good')
        m_data.connected = True 
        m_data.revenge = True
        send(ships.encode())
        while not m_data.end:
            # Отримання данних кліенту та декодування їх
            client_data = client.recv(1024).decode()
            print(client_data)
            
            raw_data = client_data.split(";")
            text1 = ''
            for client_data in raw_data:
                if client_data:
                    text1 = ''
                    # Перетворення даних на список розділяючи символом :
                    data = client_data.split(":")
                    # Якщо списку всіх даних перше значення field,
                    if 'iDontHave' in data[0]:
                        m_data.turn = True
                    if "field_nickname" in data[0]:
                        m_buttons.your_nickname.TEXT = m_buttons.nickname.TEXT
                        print(m_buttons.enemy_nickname.TEXT, data[1])
                        m_buttons.enemy_nickname.TEXT = data[1]
                        print(m_buttons.enemy_nickname.TEXT, data[1])
                        # то друге значення зі списку буде розділен за пробілами
                        data = data[2].split(" ")
                        # Для кожного корабля у списку всіх даних
                        for ship in data:
                            # Розділення кожного корабля по комі
                            splited_data = ship.split(",")
                            # Якщо розділенні данні кораблів пусті,
                            if splited_data != [""]:
                                try:
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
                                except:
                                    pass

                        for row in m_data.enemy_field:
                            print(row)
                                
                        print(data)
                        print("nickname" in data[0],"nickname", data[0])
                    # Перевірка, чи отримана команда "attack"
                    elif "buff" in data[0]:
                        m_data.buffs.append(data[1].split(','))
                    elif "remove_buff" in data[0]:
                        m_data.buffs.remove(data[1].split(','))
                    elif 'Anti_fire' in data[0]:
                        for row in range(10):
                            if 8 in m_data.enemy_field[row]:
                                for cell in range(10):
                                    if m_data.enemy_field[row][cell] == 8:
                                        m_data.enemy_field[row][cell] = 6
                        for explosion in m_data.list_explosions:
                            if explosion[0].name == 'fire' and explosion[0].x > 724:
                                explosion[0].name = 'explosion'
                                explosion[0].update_image()
                    elif "attack" in data[0]:
                        list_attacks = data[1].split(" ")
                        for attack in list_attacks:
                            try:
                                pos = attack.split(",")
                                pos = [int(pos[0]), int(pos[1]),pos[2]]
                                # Отримуємо позицію атаки
                                # Перевірка, чи атака була промахом
                                if pos[2] == "miss":
                                    # Передаємо хід гравцю
                                    m_data.turn = True
                                    # Позначаємо промах на полі
                                    m_data.my_field[pos[0]][pos[1]] = 7
                                    print("MISS")
                                # Інакше
                                elif pos[2] == "fire":
                                    m_data.my_field[pos[0]][pos[1]] = 8
                                else:
                                    # Позначаємо влучання на полі
                                    m_data.my_field[pos[0]][pos[1]] = 6
                                # Створюємо обект класа картинки, власне картинку, для відображення результату атаки
                                image = m_images.Image(
                                    progression = "game",
                                    name = pos[2],
                                    x = 59+55.7*pos[1],
                                    y = 115+55.7*pos[0],
                                    width= 55.7,
                                    height=55.7
                                )
                                m_data.list_explosions.append([image,pos[0],pos[1]])
                            except Exception as error:
                                print(error)
                    elif "pass" in data[0]:
                        m_data.turn = True
                    if 'fire' in data[0]:
                        
                        try:
                            raw_data1 = data[1].split(' ')
                            # with open(os.path.abspath(__file__+'/../../data/output.txt')) as file:
                            #     text1 += file.read()
                            # with open(os.path.abspath(__file__+'/../../data/output.txt'),'w') as file:
                            #     file.write(text1+'\nfire: '+f"{raw_data1}")
                            for cells in raw_data1:
                                if cells:
                                    cells1 = cells.split(',')
                                    m_data.enemy_field[int(cells1[0])][int(cells1[1])] = 8
                                    image = m_images.Image(
                                            progression = "game",
                                            name = 'fire',
                                            x = 725+55.7*int(cells1[1]),
                                            y = 115+55.7*int(cells1[0]),
                                            width= 55.7,
                                            height=55.7
                                    )
                                    m_data.list_explosions.append([image,int(cells1[0]),int(cells1[1])])
                                    for ship in m_data.enemy_ships:
                                        ship.check_enemy()
                        except Exception as error:
                            with open(os.path.abspath(__file__+'/../../data/output.txt')) as file:
                                text1 += file.read()
                            with open(os.path.abspath(__file__+'/../../data/output.txt'),'w') as file:
                                file.write(text1+'\n'+str(error))
                                            
                    # Перевірка, чи відбувся вибух
                    if "explosion" in data[0]:
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
                                
                                
                    
                        del data[0]
                    # Якщо відбуваеться програш
                    elif "lose" in data[0]:
                        # То стан гри змінюеться на виграш
                        m_transform.color = (255,25,25)
                        m_transform.type_transform = 0
                        m_data.progression = "lose"
                        m_achievements.achievement('Pants on Fire')
                        del data[0]
                    # Додаємо отримані дані від клієнта до списку даних противника
                    m_data.enemy_data.append(client_data)
                    print(client_data)