# імпортуємо необхідні модулі
import modules.data as m_data 
import modules.ships as m_ships
import modules.images as m_images
import modules.buttons as m_buttons
import modules.transform as m_transform
import modules.achievements as m_achievements
import socket,random,os
import modules.animations as m_animations
# створюємо функцію для відправкм даних на сервер
def send(data:bytes):
    # відправляємо дані серверу
    # if m_data.client_server == "server":
        # server1[0].sendall(data)
        # m_server.send(data)
    # else:
    try:
        # відпровляємо закодовані данні
        client.sendall(data+[';'.encode()][0])
    except:
        # відпровляємо закодовані данні
        client.sendall(f"{data};".encode())
# отримує ім'я хоста 
hostname = socket.gethostname()
# Повертає IP адрессу по імені хосту 
ip = socket.gethostbyname(hostname)
print(ip)
# import http.client
# conn = http.client.HTTPConnection('ifconfig.me')
# conn.request('GET','/')
# print(conn)
# conn = conn.getresponse('ip')
# print(conn)
# import requests

# def get_external_ip():
#     try:
#         response = requests.get("https://api.ipify.org?format=json") # или https://ifconfig.me/ip
#         response.raise_for_status() # Проверка на ошибки HTTP
#         ip_data = response.json()
#         return ip_data['ip']
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка при получении внешнего IP: {e}")
#         return None

# external_ip = get_external_ip()
# if external_ip:
#     print(f"Внешний IP-адрес: {external_ip}")
# ip = external_ip
# створюємо сокет клієнту
client_server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
# socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
# функція для активації
count = 0
def activate():
    # робимо змінну глобальною
    global client,count
    try:

        # перевіряємо чи не відбувається хід супротивника
        if not m_data.revenge:
            # виводимо ім'я на поле
            ships = f"field_nickname:{m_buttons.nickname.TEXT}:"
            # перевіряємо всі кораблі
            for ship in m_data.all_ships:
                # додаємо функції для кораблів
                ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
            # перевіряємо чи клієнт на сервері
            if m_data.client_server == "server":
                # зв'язує клієнта з ip і портом
                client_server.bind(('0.0.0.0', 8800))
                # Функція listen активує очікування підключення користувача
                client_server.listen()
                m_data.turn = random.randint(0,1)
                if not m_data.turn:
                    ships+=';pass:'
                # Підтверджуємо з'єднання від клієнту
                client = client_server.accept()[0]
                # перевіряємо з'єднання
                m_data.connected = True 
                # цикл для повторів классу range
                for c in range(1000):
                    print('HELLO server')
            # перевіряємо чи клієнт знаходиться в клієнті
            if m_data.client_server == "client":
                # підключаємо кліента до сервера
                client = client_server
                # під'єднуємо клієнта по ip і порту
                client.connect((m_data.ip, 8800))
                # цикл для повторів классу range
                for c in range(1000):
                    print('HELLO client')
                
                print("it is cool", m_data.ip)
            # визиваємо функцію для відправки даних на сервер
            # send(f"".encode())
            # цикл для повторів классу range
            for count in range(1000):
                print('good')
            # надаємо підключенню значення True
            m_data.connected = True 
            # надаємо ходу супротивника значення True
            m_data.revenge = True
            # відправляємо закодані данні 
            send(ships.encode())
            # перевіряємо чи не закінчена гра
            while not m_data.end:
                try:
                    # Отримання данних кліенту та декодування їх
                    client_data = client.recv(1024).decode()
                    print(client_data)
                    # розділяємо рядки сиволом ";"
                    raw_data = client_data.split(";")
                    # створюємо змінну текст зі значенням str
                    text1 = ''
                    # перевіряємо ряди 
                    for client_data in raw_data:
                        # перевіряємо клієнт дату
                        if client_data:
                            # створюємо змінну текст зі значенням str
                            text1 = ''
                            # Перетворення данних на список розділяючи символом :
                            data = client_data.split(":")
                            # якщо в даті нічого не маємо
                            # перевіряємо наявність ім'я на полі
                            if "field_nickname" in data[0]:
                                # текст нікнейму такий самий як твій нікнейм
                                m_buttons.your_nickname.TEXT = m_buttons.nickname.TEXT
                                print(m_buttons.enemy_nickname.TEXT, data[1])
                                # текст нікнейму супротивника дорівнює значенню в даті
                                m_buttons.enemy_nickname.TEXT = data[1]
                                print(m_buttons.enemy_nickname.TEXT, data[1])
                                # друге значення зі списку буде розділен за пробілами
                                data = data[2].split(" ")
                                # Для кожного корабля у списку данних
                                for ship in data:
                                    # Розділення кожного корабля по комі
                                    splited_data = ship.split(",")
                                    # Якщо розділенні данні кораблів не пусті
                                    if splited_data != [""]:
                                        try:
                                            print('create ship')
                                            print(splited_data)
                                            # створюеться екземпляр класу корабля з переданими параметрами
                                            ship = m_ships.Ship(x = 724,y = 115,
                                                        field_cor = (724,115),
                                                        name  = splited_data[0],
                                                        row = int(splited_data[1]),
                                                        cell = int(splited_data[2]),
                                                        rotate = int(splited_data[3]),
                                                        add = False)
                                            
                                            # Для кожного корабля первірка
                                            for count in range(int(ship.name[0])):
                                                # Якщо корабль було повернуто
                                                if ship.rotate % 180 == 0:
                                                    # Додаємо його частини в поле противника по рядку
                                                    m_data.enemy_field[ship.row][ship.cell+count] = int(ship.name[0])
                                                else:
                                                    # Додаємо його частини в поле противника по стовпцю
                                                    m_data.enemy_field[ship.row+count][ship.cell] = int(ship.name[0])
                                            
                                            # Додаємо корабель до списку кораблів противника
                                            m_data.enemy_ships.append(ship)
                                        except:
                                            pass
                                # для рядів на ворожнечому полі
                                for row in m_data.enemy_field:
                                    print(row)
                                        
                                print(data)
                                print("nickname" in data[0],"nickname", data[0])
                            # Перевіряємо чи є "buff" в даті
                            elif "buff" in data[0]:
                                # додаємо "buff" в дату
                                m_data.buffs.append(data[1].split(','))
                            # Перевіряємо чи є "remove_buff" в даті
                            elif "remove_buff" in data[0]:
                                # видаляємо "buff" з дати
                                m_data.buffs.remove(data[1].split(','))
                            # Перевіряємо чи є "Anti_fire" в даті
                            elif 'Anti_fire' in data[0]:
                                # для повторів рядів
                                for row in range(10):
                                    # якщо 8 в ряду поля супротивника
                                    if 8 in m_data.enemy_field[row]:
                                        # для повторів клітинок 
                                        for cell in range(10):
                                            # перевіряємо кількість рядів і клітинок
                                            if m_data.enemy_field[row][cell] == 8:
                                                # змінюємо кількість рядів і клітинок
                                                m_data.enemy_field[row][cell] = 6
                                # вибух у списку вибуху                  
                                for explosion in m_data.list_explosions:
                                    # перевіряє чи вибух перетворюється на вогонь
                                    if explosion[0].name == 'fire' and explosion[0].x > 724:
                                        # записує 'explosion' в вибух
                                        explosion[0].name = 'explosion'
                                        # відновлює картинку вибуху
                                        explosion[0].update_image()
                            # записуємо атаку в дату
                            elif "attack" in data[0]:
                                # додає до пробіл до списку атак 
                                list_attacks = data[1].split(" ")
                                # для атак в списку атак
                                for attack in list_attacks:
                                    try:
                                        # додаємо "," до атаки
                                        pos = attack.split(",")
                                        # записуємо функції до змінних
                                        pos = [int(pos[0]), int(pos[1]),pos[2]]
                                        # Створюємо обект класа картинки, для відображення результату атаки, та передаємо параметри 
                                        # Перевірка, чи атака була промахом
                                        clas = m_animations.Animation
                                        if pos[2] == "miss":
                                            # Передаємо хід гравцю
                                            m_data.turn = True
                                            # Позначаємо промах на полі
                                            m_data.my_field[pos[0]][pos[1]] = 7
                                            clas = m_images.Image
                                            print("MISS")
                                        # перевіряємо чи корабель горить
                                        elif pos[2] == "fire":
                                            # Позначаємо промах на полі
                                            m_data.my_field[pos[0]][pos[1]] = 8
                                        else:
                                            # Позначаємо влучання на полі
                                            m_data.my_field[pos[0]][pos[1]] = 6
                                        image = clas(
                                            progression = "Noke",
                                            name = pos[2],
                                            x = 59+55.7*pos[1],
                                            y = 115+55.7*pos[0],
                                            width= 55.7,
                                            height=55.7,
                                        )
                                        # додаємо картинку до списку вибуху
                                        m_data.list_explosions.append([image,pos[0],pos[1]])
                                    except Exception as error:
                                        print(error)
                            # записуємо "pass" в дату
                            elif "pass" in data[0]:
                                # передаємо хід 
                                m_data.turn = True
                            # перевіряємо наявність "fire" в даті
                            if 'fire' in data[0]:
                                
                                try:
                                    # додає пробіл до ряду в даті
                                    raw_data1 = data[1].split(' ')
                                    # для клітинок в ряду
                                    for cells in raw_data1:
                                        # чи є в клітинках щось
                                        if cells:
                                            # додаємо "," до клітинки
                                            cells1 = cells.split(',')
                                            # позначаємо промах для ворожнечого поля
                                            m_data.enemy_field[int(cells1[0])][int(cells1[1])] = 8
                                            # Створюємо обект класа картинки, для відображення вогню, та передаємо параметри 
                                            image = m_images.Image(
                                                    progression = "game",
                                                    name = 'fire',
                                                    x = 725+55.7*int(cells1[1]),
                                                    y = 115+55.7*int(cells1[0]),
                                                    width= 55.7,
                                                    height=55.7
                                            )
                                            # додаємо картинку до списку вибуху
                                            m_data.list_explosions.append([image,int(cells1[0]),int(cells1[1])])
                                            # дя кораблів в ворожих кораблях
                                            for ship in m_data.enemy_ships:
                                                # перевіряємо кораблі ворога
                                                ship.check_enemy()
                                except Exception as error:
                                    # безпечно відкриває output/txt
                                    with open(os.path.abspath(__file__+'/../../data/output.txt')) as file:
                                        # до тексту додаємо файл для читання
                                        text1 += file.read()
                                    # безпечно відкриває output/txt 
                                    with open(os.path.abspath(__file__+'/../../data/output.txt'),'w') as file:
                                        # відкриває файл для написання
                                        file.write(text1+'\n'+str(error))
                                                    
                            # Перевірка, чи відбувся вибух
                            if "explosion" in data[0]:
                                # в дату додає знак ","
                                pos = data[1].split(",")
                                print(pos)
                                # try:
                                # перевіряє довжин
                                if len(pos[0]) > 1:
                                    # залишає значення позиції таким самим
                                    pos[0] = pos[0][0]
                                # перевіряє довжину
                                if len(pos[1]) > 1:
                                    # змінює значення позиції
                                    pos[1] = pos[1][0]
                                # записуємо функції до змінних
                                pos = [int(pos[0]), int(pos[1])]
                                # except:
                                # Перебираемо всі кораблі
                                for ship in m_data.all_ships:
                                    # Якщо це корабль противника пропускаємо
                                    if ship in m_data.enemy_ships:
                                        pass
                                    # якщо координати вибуху збігаються з позицією корабля
                                    elif ship.row == pos[0] and ship.cell == pos[1]:
                                        # то відбуваеться вибух
                                        ship.explosion = True
                                        
                                        
                                # дата видаляється
                                del data[0]
                            # якщо відбуваеться програш
                            elif "lose" in data[0]:
                                # змінюємо колір трансформації
                                m_transform.color = (255,25,25)
                                #задаємо кількість типів трансформації
                                m_transform.type_transform = 0
                                # стан гри змінюеться на програш
                                m_data.progression = "lose"
                                # додається нове досягнення
                                m_achievements.achievement('Pants on Fire')
                                # дата видаляється
                                del data[0]
                            # Додаємо отримані дані від клієнта до списку даних противника
                            m_data.enemy_data.append(client_data)
                except:
                    print('error:connect')
    except:
        # до числа додаємо 1
        count += 1
        # активовуємо
        activate()