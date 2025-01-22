'''
    >>> Працює з підключенням клієнта та сервера - змінна client_server
'''
# імпортуємо необхідні модулі
import modules.data as m_data 
import modules.ships as m_ships
import modules.images as m_images
import modules.buttons as m_buttons
import modules.transform as m_transform
import modules.achievements as m_achievements
import modules.audio as m_audio
import socket,random,os,time
import modules.animations as m_animations
# створюємо функцію для відправкм даних на сервер
def send(data:bytes):
    '''
        >>> Відправляє закодовані данні
    '''
    # відправляємо дані серверу
    try:
        # відпровляємо закодовані данні
        client.sendall([';'.encode()][0]+data+[';'.encode()][0])
    except:
        # відпровляємо закодовані данні
        client.sendall(f";{data};".encode())
# отримує ім'я хоста 
hostname = socket.gethostname()
# Повертає IP адрессу по імені хосту 
ip = socket.gethostbyname(hostname)

# створюємо сокет клієнту
client_server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
# функція для активації
count = 0
def activate():
        '''
            >>> Під'єднуємо клієнта і сервера
        '''
    # робимо змінну глобальною
        global client,count
    # try:
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
            # перевіряємо чи клієнт знаходиться в клієнті
            if m_data.client_server == "client":
                # підключаємо кліента до сервера
                client = client_server
                # під'єднуємо клієнта по ip і порту
                client.connect((m_data.ip, 8800))
                
            # надаємо підключенню значення True
            m_data.connected = True 
            # надаємо ходу супротивника значення True
            m_data.revenge = True
            # визиваємо функцію для відправки даних на сервер
            send(ships.encode())
            # перевіряємо чи не закінчена гра
            client_data = ''
            while not m_data.end:
                # Отримання данних кліенту та декодування їх
                client_data = client.recv(1024).decode()
                # розділяємо рядки сиволом ";"

                raw_data = client_data.split(";")
                # створюємо змінну текст зі значенням str
                text1 = ''
                list_to_del = []
                # перевіряємо ряди 
                for counter in range(len(raw_data)):
                    # перевіряємо клієнт дату
                    if raw_data[counter]:
                        # створюємо змінну текст зі значенням str
                        text1 = ''
                        # Перетворення данних на список розділяючи символом :
                        data = raw_data[counter].split(":")
                        # перевіряємо наявність ім'я на полі
                        if "field_nickname" in data[0]:
                            list_to_del.append(counter)
                            # текст нікнейму такий самий як твій нікнейм
                            m_buttons.your_nickname.TEXT = m_buttons.nickname.TEXT
                            # текст нікнейму супротивника дорівнює значенню в даті
                            m_buttons.enemy_nickname.TEXT = data[1]
                            
                            # друге значення зі списку буде розділен за пробілами
                            data = data[2].split(" ")
                            # Для кожного корабля у списку данних
                            for ship in data:
                                # Розділення кожного корабля по комі
                                splited_data = ship.split(",")
                                # Якщо розділенні данні кораблів не пусті
                                if splited_data != [""]:
                                    try:
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
                        # Перевіряємо чи є "buff" в даті
                        elif "buff" in data[0]:
                            # додаємо "buff" в дату
                            m_data.buffs.append(data[1].split(','))
                            list_to_del.append(counter)
                        # Перевіряємо чи є "remove_buff" в даті
                        elif "remove_buff" in data[0]:
                            # видаляємо "buff" з дати
                            m_data.buffs.remove(data[1].split(','))
                            list_to_del+=[counter]
                        # Перевіряємо чи є "Anti_fire" в даті
                        elif 'Anti_fire' in data[0]:
                            list_to_del.append(counter)
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
                                    volume = 0.5
                                    try:
                                        pos[3]
                                        if pos[3] == '1':
                                            volume = float(pos[3])
                                        else:
                                            pass
                                    except Exception as error:
                                        
                                        pass
                                    pos = [int(pos[0]), int(pos[1]),pos[2]]

                                    # Створюємо обект класа картинки, для відображення результату атаки, та передаємо параметри 
                                    clas = m_animations.Animation
                                    # Перевірка, чи атака була промахом
                                    if pos[2] == "miss":
                                        # Передаємо хід гравцю
                                        m_data.turn = True
                                        # Позначаємо промах на полі
                                        m_data.my_field[pos[0]][pos[1]] = 7
                                        clas = m_images.Image
                                        pass
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
                                    pass
                            m_audio.explosion.play(volume)
                            list_to_del.append(counter)
                        # записуємо "pass" в дату
                        elif "pass" in data[0]:
                            # передаємо хід 
                            m_data.turn = True
                            list_to_del.append(counter)
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
                                        image = m_animations.Animation(
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
                            list_to_del.append(counter)
                                                
                        # Перевірка, чи відбувся вибух
                        if "explosion" in data[0]:
                            # в дату додає знак ","
                            pos = data[1].split(",")
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
                                    
                                    
                            list_to_del.append(counter)
                            # дата видаляється
                            
                        # якщо відбуваеться програш
                        elif "lose" in data[0]:
                            # змінюємо колір трансформації
                            m_transform.color = (255,25,25)
                            #задаємо кількість типів трансформації
                            m_transform.type_transform = 0
                            m_data.read_data['loses'] = 1 + int(m_data.read_data['loses'])
                            with open(m_data.path+m_data.type+'data.txt', "w") as file:
                                # записуємо нікнейм, ip, звук і клієнт_сервер
                                file.write(f"{m_buttons.nickname.TEXT}\n{m_data.ip}\n{not m_audio.track.stoped}\n{m_data.client_server}\n{m_data.read_data['wins']}\n{m_data.read_data['loses']}")
                            if m_data.read_data['loses'] > 2:
                                m_achievements.achievement('Losing Streak')
                            # стан гри змінюеться на програш
                            m_data.progression = "lose"
                            # додається нове досягнення
                            m_achievements.achievement('Pants on Fire')
                            list_to_del.append(counter)
                            # дата видаляється
                try:
                    for counts in list_to_del:
                        del raw_data[-(counts+1)]
                    client_data = ";".join(raw_data)
                    pass
                except Exception as error:
                    pass