'''
    >>> Відповідяє за створення всіх кнопок - клас Button
    >>> Відповідає за функції при натисканні кнопок - метод button_start 
'''
# імпорт чужих модулів для роботи
import pygame , socket, os
import threading, random
import getpass
# імпорт наших модулів
import modules.audio as m_audio
from modules.images import Image
import modules.transform as m_transform
import modules.data as m_data
import modules.clients_server as m_client 
import modules.achievements as m_achievements
import modules.attack as m_attack
# import modules.server as m_server
from modules.ships import Ship,fill_field
# функція для малювання обведення
def stroke(screen,rect:pygame.Rect,color = (0,0,0),width = 5,multiplier_x = 1,multiplier_y = 1):
    '''
        >>> Малює обведення
    '''
    # малюємо лінії обводки
    pygame.draw.line(screen,color,
                     (int(rect.x*multiplier_x),int(rect.y*multiplier_y)),
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y*multiplier_y)),
                     (int((rect.x+rect.width)*multiplier_x),int((rect.y+rect.height)*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x+rect.width)*multiplier_x),int(rect.y+rect.height)*multiplier_y),
                     (int(rect.x*multiplier_x),int((rect.y+rect.height)*multiplier_y)),int(width*multiplier_x))
    pygame.draw.line(screen,color,
                     (int((rect.x)*multiplier_x),int((rect.y+rect.height)*multiplier_y)),
                     (int(rect.x*multiplier_x),int(rect.y*multiplier_y)),int(width*multiplier_x))

# класс з кнопками
class Button(Image):
    '''
        >>> Додає параметри до класу зображень
    '''
    # метод з створенням параметрів
    def __init__(self, fun = None, width = 100, height = 100, x= 0, y= 0, name = "", progression = "menu", text: str ="", size = 65, color = (0, 0, 0),rotate = 0):
        # задаємо параметри в класс зображень
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression,rotate=rotate)
        # переносимо параметри в змінні
        self.center_text = True
        self.WIDTH_BUT = width
        self.second_color = (255,255,255)
        self.HEIGHT_BUT = height
        self.X = x
        self.Y = y
        self.function = fun
        self.TEXT = text  
        self.render = None
        self.last_text = None
        self.activate = 0
        # створюємо параметри
        self.COLOR = color
        self.FONT = pygame.font.SysFont("algerian", size)
        self.rect = pygame.Rect(x,y,width,height)
        self.size = size 
        self.start_size = size
        self.current_size = self.size
        self.select = False
    def activate(self, event):
        '''
            >>> Відповідає за виділення
        '''
        # умова для обводки
        if self.rect.collidepoint(event.pos):
            # обираємо
            self.select = True
        else:
            # не обираємо
            self.select = False
    # метод з кнопкою старт
    def button_start(self, event):
        '''
            >>> Створює кнопку старт
            >>> Перевіряє чи кнопка натиснута
        '''
        # перевіряємо подію
        if type(event) == pygame.event.Event:
            # ставимо позицію
            pos = event.pos
        else:
            # ставимо позицію
            pos = event
        # якщо кнопка натиснута
        if self.rect.collidepoint(pos):
            if type(self.function) == type("123") and self.function.split(":")[0] == "c_s":
                m_data.client_server = self.function.split(":")[1]
                server.COLOR = (0,0,0)
                client.COLOR = (0,0,0)
                self.COLOR =(40,2,255)
            # якщо функція корабль то
            elif self.function == "ship":
                # цикл для всіх кораблів
                for ship in m_data.all_ships:
                    # якщо корабль виділен
                    if ship.select:
                        # поворот корабля   
                       ship.rotate_ship()
                        # виділення корабля
                       ship.select  = False
            # перевіряє музику
            elif self.function == "music":
                # перевіряє чи зупинена музика
                if m_audio.track.stoped:
                    music3.name = 'pause'
                    # запускаємо музику
                    m_audio.track.play()
                    # self.name = "music"
                else:
                    music3.name = 'play'
                    # зупиняємо музику
                    m_audio.track.stop()
                music3.update_image()
                    # self.name = "music_off"
                # self.update_image()
            # перевіряємо чи відбувся виграш_програш
            elif self.function == "win_lose":
                # змінюємо помсту на True
                m_data.revenge = True
                # програє анімацію переходу
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                # переміщуємося на екран pre-game
                m_data.progression = "pre-game"
                # задаємо розмір кораблю
                size_ship = "1"
                # список для ворожого корабля
                m_data.enemy_ships = []
                # список для всіх кораблів
                m_data.all_ships = []
                # Створення списку, у якому зберігаеться усе наше поле
                m_data.my_field = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

                # Створення списку, у якому зберігаеться усе поле ворога
                m_data.enemy_field = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
                # m_data.turn = 
                # list_count = []
                # m_data.list_blits["game"] = []
                # список для вибухів
                m_data.list_explosions = []
                # play_field = Image(width = 1280, height = 851, x = 0, y = 0, name = "play_field", progression = "game", edit = False)
                # for count in range(len(m_data.list_blits["game"])):
                #     if m_data.list_blits["game"][count].name in "miss, explosion":
                #         list_count += [count]
                # for count in range(len(list_count)):
                #     del m_data.list_blits["game"][list_count[-(count + 1)]]
                # цикл для рахунку
                for count in range(10):
                    # наслідуємо клас Ship 
                    ship = Ship(x=59, y=115, name=size_ship)
                    # виділяємо корабель
                    ship.select = True
                    # розташовуємо кораблі за x та y
                    ship.place((684, 220))
                    # прибираємо виділення корабля
                    ship.select = False
                    # превіряємо чи число дорівнює 3
                    if count == 3:
                        # розмір корабля змінюємо на 2
                        size_ship = "2"
                    # превіряємо чи число дорівнює 6
                    if count == 6:
                        # розмір корабля змінюємо на 3
                        size_ship = "3"
                    # превіряємо чи число дорівнює 8
                    if count == 8:
                        # розмір корабля змінюємо на 4
                        size_ship = "4"
            # робимо перевірку
            elif self.function == "check":
                # повертаємо True 
                return True
            # перевіряємо покупку
            elif self.function == "buy":
                print('hallo')
                try:
                    # якщо не атакуємо
                    
                        # перевіряємо чи достатньо монет для покупки
                        if m_data.cost_data[m_data.select_weapon] <= m_data.coins:
                            # віднімаємо суму покупки
                            
                            # додаємо досягнення
                            m_achievements.achievement('Arm yourself')
                            # звук покупки
                            m_audio.buying.play()
                            # перевіряємо чи обран енергетик
                            if 'Energetic' == m_data.select_weapon:
                                m_data.list_Bought['Energetic'] = True
                                print('YOU LOST')
                                m_data.coins -= m_data.cost_data[m_data.select_weapon]
                                # додаємо енергетик в ефекти
                                m_data.buffs.append(['Energetic'])
                                # m_client.send('buff:Energetic')
                            # перевіряємо чи обран вогнегасник
                            elif "Anti_fire"== m_data.select_weapon:
                                print("YOU LOST1")
                                m_data.list_Bought['Anti_fire'] = True
                                print('bosssssssssssssssssssssssssssssssssotron3000')
                                m_data.coins -= m_data.cost_data[m_data.select_weapon]
                                # додаємо пропуск
                                add = ';pass'
                                # цикл для ефекту в ефектах
                                for buff in m_data.buffs:
                                    # перевіряємо чи енергетик в ефектах
                                    if buff[0] == 'Energetic':
                                        # змінна для додавання
                                        add = ''
                                # в клієнта відправляємо вогнегасник та додаємо add
                                m_client.send('Anti_fire:'+add)
                                # перевіряємо додане
                                if add:
                                    # забороняємо хід
                                    m_data.turn = False
                                # цикл для ряду
                                for row in range(10):
                                    # перевіряємо чи є чотирипалубний корабель на полі
                                    if 8 in m_data.my_field[row]:
                                        # цикл для клітинок
                                        for cell in range(10):
                                            # перевіряє чи корабель на полі є чотирипалубним
                                            if m_data.my_field[row][cell] == 8:
                                                # ставимо трипалубний корабель на поле
                                                m_data.my_field[row][cell] = 6
                                # цикл для вибуху в списку вибухів 
                                for explosion in m_data.list_explosions:
                                    # перевіряє чи горить корабель
                                    if explosion[0].name == 'fire' and explosion[0].x < 725:
                                        # до вибуху додає назву вибуху
                                        explosion[0].name = 'explosion'
                                        # оновлює картинку
                                        explosion[0].update_image()
                                # програє анімацію переходу
                                m_transform.type_transform = random.randint(0,m_transform.count_types)
                                # переміщює на вікно гри
                                m_data.progression = "game"                     
                            else:
                                print(m_data.coins)
                                # обирає атаку
                                m_data.attack = m_data.select_weapon
                                # програє анімацію переходу
                                m_transform.type_transform = random.randint(0,m_transform.count_types)
                                # переміщює на вікно гри
                                m_data.progression = "game"
                except Exception as error:
                    print(error)
            # перевіряємо магазин
            elif self.function == 'shop':
                # програє анімацію переходу
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                # перевіряє чи ми знаходимося в вікні магазину
                if m_data.progression == 'shop':
                    # переміщює на вікно гри
                    m_data.progression = "game"
                    # нічого не обираємо
                    m_data.select_weapon = None
                else:
                    # переходимо в магазин
                    m_data.progression = 'shop'
                    # додаємо досягнення
                    m_achievements.achievement("New Opportunities")
            elif self.function == 'controls':
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                # перевіряємо досягнення
                if m_data.progression == 'controls':
                    # переходимо в меню
                    m_data.progression = "menu"
                else:
                    # переходимо в досягнення
                    m_data.progression = 'controls'
            # перевіряємо досягнення
            elif self.function == 'achievements':
                # програє анімацію переходу
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                # перевіряємо досягнення
                if m_data.progression == 'achievements':
                    # переходимо в меню
                    m_data.progression = "menu"
                else:
                    # переходимо в досягнення
                    m_data.progression = 'achievements'

            elif self.function and self.function.split(":")[0] == 'change':
                # програє анімацію переходу
                m_transform.type_transform = random.randint(0,m_transform.count_types)
                # перевіряємо досягнення
                m_data.progression = self.function.split(":")[1]
            # переходимо в гру
            elif self.function == "play":
                # задаємо початкову кількість монет
                m_data.coins = 0
                # змінна да_ні дорівнює правді
                yes_no = True
                print(m_data.cells)
                # цикл для стандартних клітинок
                for row in m_data.cells:
                    # цикл для клітинок в ряду
                    for cell in m_data.cells[row]:
                        # якщо кораблі не розставлені
                        if cell[0]:
                            print(cell)
                            # змінна да_ні змінюється на неправду 
                            yes_no =  False
                # якщо всі кораблі розставлені
                if yes_no:
                    # цикл для корабля в усіх кораблях
                    for ship in m_data.all_ships:
                        # не обираємо корабель
                        ship.select = False
                        # оновлюємо картинку
                        ship.update_image()
                    # програє анімацію переходу
                    m_transform.type_transform = random.randint(0,m_transform.count_types)
                    # переходимо в гру
                    m_data.progression = "game"
                    # icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon_peaceful.png"))
                    # pygame.display.set_icon(icon)
                    #перевіряємо помсту
                    if not m_data.revenge:
                        # if m_data.client_server == "client" or not m_data.client_server:
                        # активує клієнта одночасно з роботою кода
                        threading.Thread(target = m_client.activate,daemon=True).start()
                        # if m_data.client_server == "server" or not m_data.client_server:
                            # активує сервер
                            # threading.Thread(target = m_server.activate,daemon=True).start()
                    else:
                        print(m_data.all_ships)
                        # додаємо текст до нікнейму
                        ships = f"field_nickname:{nickname.TEXT}:"
                        # цикл для корабля в усіх кораблях
                        for ship in m_data.all_ships:
                            # до корабля додаємо назву, ряд, клітинку і поворот
                            ships += f"{ship.name},{ship.row},{ship.cell},{ship.rotate} "
                        # відправляємо закодовані данні в клієнта
                        m_client.send(ships.encode()) 
            # задаємо досягнення
            elif self.function and 'set_achievement' in self.function:
                # додаємо опис до досягнень
                description_.TEXT = (self.name.split('/')[1]+': '+m_data.achievements_data[self.function.split('/')[1]]['description']).split(' ') +['                ', '           ']
                # multiplers = [
                #     # додаємо параметри
                #     self.rect.width/self.width,
                #     self.rect.height/self.height
                # ]
                # # перевіряємо мультиплеер
                # if multiplers[0] > multiplers[1]:
                #     # до опису додаємо шрифт та розмір
                #     description_.FONT = pygame.font.SysFont("algerian", int((description_.size*multiplers[1])))
                # else:
                #     # до опису додаємо шрифт та розмір
                #     description_.FONT = pygame.font.SysFont("algerian", int((description_.size*multiplers[0])))
                # додаємо '/' до назви обраної зброї
                m_data.select_weapon = self.name.split('/')[1]
                # додаємо шрифт та розмір до опису
                size = description_.FONT.size(" ".join(description_.TEXT))
                # перевіряємо розмір тексту
                if size[0] < description_.rect.width:
                    # додаємо текст до опису
                    description_.TEXT = [" ".join(description_.TEXT)]
                # віднімаємо довжину опису
                elif len(description_.TEXT)-2:
                    # список для тексту 
                    list_text = []
                    # змінна для тексту
                    text = ''
                    # цикл для тексту в описі
                    for text_for in description_.TEXT:
                        # задає розмір і шрифт тексту
                        size = description_.FONT.size(text+text_for)
                        # превіряє розмір тексту
                        if size[0] < description_.rect.width:
                            # до тексту додаємо текст для
                            text += text_for + ' '
                        # превіряє розмір тексту
                        elif size[0] > description_.rect.width:
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                            # до тексту для додаємо ' '
                            text = text_for + ' '
                        # перевіряємо чи текст опису дорівнює тексту для
                        elif description_.TEXT[-1] == text_for + ' ':
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                    # перевіряємо текст в списку
                    if text_for in list_text[-1]:
                        pass
                    else:
                        # задає розмір і шрифт тексту
                        size = description_.FONT.size(text+text_for)
                        # превіряє розмір тексту
                        if size[0] < description_.rect.width:
                            # до тексту додаємо текст для
                            text += text_for
                        # превіряє розмір тексту
                        elif size[0] > description_.rect.width:
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                            # до списку з текстом додаємо текст для
                            list_text.append(text_for)
                        # превіряє розмір тексту
                        elif description_.TEXT[-1] == text_for:
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                    # опис повинен дорівнювати тексту в списку
                    description_.TEXT = list_text
            # превіряємо функцію і зброю в функціях
            elif self.function and 'weapons' in self.function:
                # buff
                # розділяємо строки з описом за допомогою '/'
                description.TEXT = m_data.weapon_data[self.function.split('/')[1]][self.function.split('/')[2]].split(' ') +['                ', '           ']
                # розділяємо строки з обраною зброєю за допомогою '/'
                m_data.select_weapon = self.function.split('/')[2]
                # список для мультиплееру
                multiplers = [
                    # додаємо параметри
                    self.rect.width/self.width,
                    self.rect.height/self.height
                ]
                # перевіряємо мультиплеер
                if multiplers[0] > multiplers[1]:
                    # до опису додаємо шрифт та розмір
                    description.FONT = pygame.font.SysFont("algerian", int((40*multiplers[1])))
                else:
                    # до опису додаємо шрифт та розмір
                    description.FONT = pygame.font.SysFont("algerian", int((40*multiplers[0])))
                # додаємо текст опису до шрифту і розміру опису
                size = description.FONT.size(" ".join(description.TEXT))
                # перевіряємо розмір опису
                if size[0] < description.width*multiplers[0]:
                    # до опису додаємо " "
                    description.TEXT = [" ".join(description.TEXT)]
                # віднімаємо два символи від опису
                elif len(description.TEXT)-2:
                    # список для тексту
                    list_text = []
                    # змінна для тексту
                    text = ''
                    # цикл для тексту в описі
                    for text_for in description.TEXT:
                        # задаємо розмір і шрифт до тексту
                        size = description.FONT.size(text+text_for)
                        # перевіряємо розмір опису
                        if size[0] < description.width*multiplers[0]:
                            # до тексту додаємо текст для і ' '
                            text += text_for + ' '
                        # перевіряємо розмір опису
                        elif size[0] > description.width*multiplers[0]:
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                            # до тексту для додаємо ' '
                            text = text_for + ' '
                        # перевіряємо розмір опису
                        elif description.TEXT[-1] == text_for + ' ':
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                    # перевіряємо текст в списку з текстом
                    if text_for in list_text[-1]:
                        pass
                    else:
                        # додаємо шрифт і розмір до тексту
                        size = description.FONT.size(text+text_for)
                        # перевіряємо розмір опису
                        if size[0] < description.width*multiplers[0]:
                            # до тексту додаємо текст для
                            text += text_for
                        # перевіряємо розмір опису
                        elif size[0] > description.width*multiplers[0]:
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                            # до списку з текстом додаємо текст для
                            list_text.append(text_for)
                        # перевіряємо розмір опису
                        elif description.TEXT[-1] == text_for:
                            # до списку з текстом додаємо текст
                            list_text.append(text)
                    # розділяємо строки з описом за допомогою '/'
                    description.TEXT = [self.function.split('/')[2]+': '] +  list_text
            # превіряємо чи ми в 'start_game'
            elif self.function == 'start_game':
                # превіряємо текст нікнейму
                if m_data.client_server and nickname.TEXT:
                    # записуємо ip 
                    ip = input.TEXT.split(": ")
                    # видаляємо ip
                    del ip[0]
                    # додаємо ": " до ip
                    ip = ": ".join(ip)
                    # записуємо ip
                    m_data.ip = ip
                    # перевіряємо ip
                    if m_data.ip == "":
                        # ip клієнта повинно дорівнювати ip
                        m_data.ip = m_client.ip
                    # безпечно відкриваємо data.txt
                    with open(m_data.path+m_data.type+'data.txt', "w") as file:
                        # записуємо нікнейм, ip, звук і клієнт_сервер
                        file.write(f"{nickname.TEXT}\n{m_data.ip}\n{not m_audio.track.stoped}\n{m_data.client_server}\n{m_data.read_data['wins']}\n{m_data.read_data['loses']}")
                    
                    # програє анімацію переходу
                    m_transform.type_transform = random.randint(0,m_transform.count_types)
                    # переходить в pre-game
                    m_data.progression = "pre-game"
    # метод відображення поверхні на головному окні
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає картинку на екрані
        '''
        # якщо картинка задана 
        self.rect = pygame.Rect(x,y,width,height)
        # ім'я не повинно дорівнювати ""
        if self.name != "":
            # відображення картинки 
            Image.blit(self, screen,x,y,width,height,multiplier_x,multiplier_y)
        # перевіряєо шрифт і розмірмо мультиплеер та розмір
        if multiplier_x > multiplier_y and self.current_size !=int((self.size*multiplier_y)):
            # додаємо шрифт і розмір
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_y)))
            # задаємо поточний розмір
            self.current_size= int((self.size*(multiplier_y/2)))
            # self.size = int((self.size*multiplier_y))
        # поточний розмір не дорівнює розміру мультиплеера
        elif self.current_size != int((self.size*multiplier_x)) and multiplier_x <= multiplier_y:
            # додаємо шрифт і розмір
            self.FONT = pygame.font.SysFont("algerian", int((self.size*(multiplier_x))))
            # поточний розмір дорівнює розміру мультиплеера
            self.current_size = int((self.size*multiplier_x))
        # перевіряємо тип тексту
        if type(self.TEXT) == type(""):
            # додаємо розмір і шрифт до тексту
            size = self.FONT.size(self.TEXT) 
            # задаємо y для тексту
            y = y + height/2-size[1]/2
            # задаємо центральний текст
            if self.center_text:
                # змінюємо x
                x = x + width/2-size[0]/2
            else:
                # додаємо 20 до x
                x += 20
            # if self.TEXT != self.last_text:
                # screen.blit(self.FONT.render(self.TEXT,True,self.COLOR), (x, y))
            # перевіряємо другий колір
            if self.second_color:
                # робимо анімацію удару
                render_stroke = self.FONT.render(self.TEXT,True,self.second_color)
                # цикл для ряду
                for row in range(3):
                    # цикл для клітинки
                    for cell in range(3):
                        # виводимо анімацію удару на екран
                        screen.blit(render_stroke, (x+row-1, y+cell-1))
            # додаємо параметри до удару
            render = self.FONT.render(self.TEXT,True,self.COLOR)
            # задаємо прозорість удару
            render.set_alpha(self.opasity)
            # відображуємо на екрані
            screen.blit(render, (x, y))
            # зберігаємо текст до прошлого тексту
            self.last_text = self.TEXT
            # else:
            #     screen.blit(self.render, (x, y))
            # screen.blit(self.FONT.render(self.TEXT,True,self.COLOR), (x, y))
        # превіряємо текст
        elif type(self.TEXT) == type([]):
            # кількість дорівнює 0 
            count = 0
            # while True:
            # цикл для перевірки тексту
            for text in self.TEXT:
                # перевіряємо мультиплеери
                if multiplier_x > multiplier_y:
                    # додаємо шрифт і розмір до тексту
                    self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_y)))
                else:
                    # додаємо шрифт і розмір до тексту
                    self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_x)))
                # додаємо до висоти тексту шрифт і розмір 
                height = self.FONT.size(text)[1]
                # додаємо шрифт і розмір до тексту
                size = self.FONT.size(text) 
                # задаємо y
                y = (self.rect.y+height*count) * multiplier_y+10
                # задаємо x 
                x = (self.rect.x)*multiplier_x+10
                # задаємо параметри до render
                render = self.FONT.render(text,True,self.COLOR)
                # задаємо прозорість 
                render.set_alpha(self.opasity)
                # відображуємо на екрані
                screen.blit(render, (self.rect.x+10, y))
                # до кількості додаємо 1
                count += 1
        # y = y + height/2-size[1]/2
        # # задаємо x для тексту 
        # x = x + width/2-size[0]/2
        # # відображення тексту на екрані
        # size = self.FONT.size(self.TEXT)

        # size[0] = multiplier_x * size[0]
        # size[1] = multiplier_y * size[1]
        # задаємо y для тексту

# button = Button()
# клас для додавання параметрів до картинки
class Input(Image):
    '''
        >>> Додає параметри до картинки
    '''
    # функція для ініціалізації картинки
    def __init__(self, width: int, height: int,x = 0,y = 0, name = "", progression = "menu", color = (0,0,0), text = "ip: ", list = "0123456789."):
        # задаємо параметри
        self.start_width = width 
        self.start_height = height 
        # ініціалізуємо картини
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        # задаємо параметри
        self.COLOR = color
        self.FONT = pygame.font.SysFont("algerian", 65)
        self.TEXT = text 
        self.RENDER_TEXT = None
        self.enter = False
        self.edit("ok")
        self.rect = pygame.Rect(x,y,width,height)
        self.list = list
        self.size = 65 
        self.current_size = self.size
    # функція для відображення картинки на екрані
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає картинку на екрані
        '''
        # ім'я не дорівнює ""
        if self.name != "":
            # відображення картинки
            Image.blit(self, screen,x,y,width,height,multiplier_x,multiplier_y)
        # s = pygame.time.get_ticks()
        # задаємо параметри
        self.rect = pygame.Rect(x,y,width,height)
        # перевіряємо наявність чогось в списку
        if self.list == 'any':
            # задаємо x 
            self.x = 42
        # перевіряємо мультиплеер і поточний розмір
        if multiplier_x > multiplier_y and self.current_size !=int((self.size*multiplier_y)):
            # змінюємо шрифт і розмір
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_y)))
            # змінюємо розмір для поточного розміру
            self.current_size= int((self.size*multiplier_y))
            # self.size = int((self.size*multiplier_y))
        # перевіряємо мультиплеер і поточний розмір
        elif self.current_size != int((self.size*multiplier_x)) and multiplier_x <= multiplier_y:
            # змінюємо шрифт і розмір
            self.FONT = pygame.font.SysFont("algerian", int((self.size*multiplier_x)))
            # змінюємо розмір для поточного розміру
            self.current_size = int((self.size*multiplier_x))
        # додаємо шрифт і розмір до тексту
        size = self.FONT.size(self.TEXT)
        # задаємо y для тексту
        y = y + height/2-size[1]/2
        # задаємо x для тексту
        x = x + width/2-size[0]/2
        # задаємо колір до удару
        render = self.FONT.render(self.TEXT,True,self.COLOR)
        # задаємо прозорість до удару
        render.set_alpha(self.opasity)
        # відображаємо на екрані
        screen.blit(render, (x, y))
        # анімація переходу
        self.rect = pygame.Rect(x,y,width,height)
    # метод для виділення поля ввода
    def activate(self, event):
        '''
            >>> Відповідає за виділення поля ввода
        '''
        # робимо обводку 
        if self.rect.collidepoint(event.pos):
            # дозволяємо вводити
            self.enter = True
        else:
            # забороняємо вводити
            self.enter = False
    # метод для редагування тексту
    def edit(self,event):
        '''
            >>> Редагує текст
        '''
        # перевіряє введений текст
        if self.enter:
            # записує назву
            key = pygame.key.name(event.key)
            # перевіряє ip
            if event.key == pygame.K_BACKSPACE and self.TEXT != "ip: ":
                # прибирає останній символ текста 
                self.TEXT = self.TEXT[:-1]
            # перевіряє ключі в списках
            elif key in self.list or self.list != "0123456789." and len(key) == 1:
                # до тексту додаємо текст
                self.TEXT += key
        # додаємо параметри до тексту удару
        self.RENDER_TEXT = self.FONT.render(self.TEXT, True, self.COLOR)
# клас для випадкової розстановки кораблів
class Auto(Image):
    '''
        >>> Випадково розставляє кораблі
    '''
    # функція для ініціалізації
    def __init__(self, width: int, height: int, x: int, y: int, name='', progression: str = "pre-game"):
        # батьківський клас для ініціалізації
        super().__init__(width, height, x, y, name, progression)
        #анімація переходу
        self.rect = pygame.Rect(x,y,width,height)
        # додаємо self до списку pre-game
        m_data.list_blits["pre-game"].append(self)
    # метод для відображення кнопки на екрані
    def blit(self, screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображає кнопку на екрані
        '''
        # анімація переходу
        self.rect = pygame.Rect(x,y,width,height)
        # pygame.draw.rect(screen,(255,25,25),self.rect)
    # метод для випадкової розстановки кораблів
    def randomship(self, cor):
        '''
            >>> Випадково розставляє кораблі
        '''
        # перевіряє обводку
        if self.rect.collidepoint(cor):
            # задаємо кількість 0
            count = 0
            # задаємо кількість кораблів 0
            count_ships = 0  
            # список для данних на нашому полі
            m_data.my_field = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            # список для всіх кораблів
            m_data.all_ships = []
            # цикл для ряду в клітинках
            for row in m_data.cells:
                # цикл для клітинки в клітинках
                for cell in m_data.cells[row]:
                    # задаємо False для клітинки
                    print(cell,type(cell))
                    cell[0] =  False
            # for ship in m_data.all_ships:
            # поки True
            while True:
                # рандом для ряду
                row = random.randint(0, 9)
                # рандом для клітинки
                cell = random.randint(0, 9)
                # рандомний поворот
                rotate = random.randint(0, 4)
                # до кількості додаємо 1
                count += 1
                # перевірка кораблів на полі
                if m_data.my_field[row][cell] ==  0:
                    # наслідуємо клас Ship і задаємо необхідні параметри
                    ship = Ship(x = 59, y = 115, cell = cell, row = row, rotate = rotate * 90)
                    # до кількості кораблів додаємо 1
                    count_ships += 1
                    # додаємо корабель на поле
                    m_data.my_field[row][cell] = 1
                    # заповнення поля
                    fill_field(m_data.my_field)
                # перевіряємо кількість кораблів 
                if count_ships == 4 or count > 1000:
                    # перерва
                    break
            # кількість кораблів дорівнює 0
            count_ships = 0
            # поки True
            while True:
                # рандом для ряду
                row = random.randint(0, 9)
                # рандом для клітинки
                cell = random.randint(0, 9)
                # рандомний поворот
                rotate = random.randint(0, 4)
                # до кількості додаємо 1
                count += 1
                try: 
                    # перевіряємо кораблі на полі
                    if m_data.my_field[row][cell] == 0: 
                        # перевіряє розташування та поворот корабля на полі
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1: 
                            # наслідуємо клас Ship і задаємо необхідні параметри
                            ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "2", rotate = rotate * 90)
                            # до кількості кораблів додаємо 1
                            count_ships += 1
                            # заповнення поля
                            fill_field(m_data.my_field)
                except:
                    pass
                # перевіряє кількість кораблів
                if count_ships == 3 or count > 1000:
                    # перерва
                    break
            # кількість кораблів дорівнює 0
            count_ships = 0
            # поки True
            while True:
                # рандом для ряду
                row = random.randint(0, 9)
                # рандом для клітинки
                cell = random.randint(0, 9)
                # рандомний поворот
                rotate = random.randint(0, 4)
                # до кількості додаємо 1
                count += 1
                try:
                    # перевіряємо кораблі на полі
                    if m_data.my_field[row][cell] == 0:
                        # перевіряє розташування та поворот корабля на полі
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            # перевіряє розташування та поворот корабля на полі
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                # наслідуємо клас Ship і задаємо необхідні параметри
                                ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "3", rotate= rotate * 90)
                                # до кількості кораблів додаємо 1
                                count_ships += 1
                                # заповнення поля
                                fill_field(m_data.my_field)
                except:
                    pass
                # перевіряє кількість кораблів
                if count_ships == 2 or count > 1000:
                    # перерва
                    break
            # кількість кораблів дорівнює 0
            count_ships = 0
            # поки True
            while True:
                # рандом для ряду
                row = random.randint(0, 9)
                # рандом для клітинки
                cell = random.randint(0, 9)
                # рандомний поворот
                rotate = random.randint(0, 4)
                # до кількості додаємо 1
                count += 1
                try:
                    # перевіряємо кораблі на полі
                    if m_data.my_field[row][cell] ==  0:
                        # перевіряє розташування та поворот корабля на полі
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            # перевіряє розташування та поворот корабля на полі 
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                # перевіряє розташування та поворот корабля на полі
                                if m_data.my_field[row][cell+3] == 0 and rotate % 2 == 0 or m_data.my_field[row+3][cell] == 0 and rotate % 2 == 1:
                                    # наслідуємо клас Ship і задаємо необхідні параметри
                                    ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "4", rotate= rotate * 90)
                                    # до кількості кораблів додаємо 1
                                    count_ships += 1
                                    # заповнення поля
                                    fill_field(m_data.my_field)
                except:
                    pass
                # перевіряє кількість кораблів
                if count_ships == 1 or count > 1000:
                    # зупинка
                    break
            # перевірка кількості
            if count > 1000:
                # рандомна розстановка кораблів
                self.randomship(cor)
# отримуємо ім'я хоста
hostname = socket.gethostname()
# отримуємо ip
ip = socket.gethostbyname(hostname)
# змінна для ip1
ip1 = ""
# отримуємо нікнейм
nick = getpass.getuser()
# перевіряємо записаний нікнейм
if m_data.read_data["nickname"] != "":
    # запом'ятовує нікнейм
    nick = m_data.read_data["nickname"]
# перевіряє наявність "." в записаному ip
if "." in m_data.read_data["ip"]:
    # додаємо ip в ip1
    ip1 = m_data.read_data["ip"]
# наслідуємо клас Button і задаємо необхідні параметри
button_start = Button(width = 402 , height = 120, x = 435, y = 370, name = "", text= "start",fun='start_game')
# m_data.list_blits["menu"].append(button_start)
# наслідуємо клас Input і задаємо необхідні параметри
input = Input(width = 496, height = 148, x = 387 , y = 568, name = "button_start", text = f"ip: {ip1}")
# наслідуємо клас Input і задаємо необхідні параметри
nickname = Input(x= 42, y= 43, width= 281, height= 84, name = "button_start", text = nick, list = "any")
# наслідуємо клас Button і задаємо необхідні параметри
ip = Button(x = 981, y = 59, width = 281, height = 84, name = "button_start", text = m_client.ip, size = 50)
# цикл для об'єктів в нікнеймі і ip
for object in [nickname, ip]:
    # додаємо розмір до тексту
    size = object.FONT.size(object.TEXT)
    # перевіряємо ширину
    if object.width - size[0] - 10 < 0:
        # задаємо ширину
        width = -(object.width - size[0] - 10)
        # задаємо x
        object.x -= width
        # задаємо ширину
        object.width += width
        # оновлюємо картинку
        object.update_image()
# наслідуємо клас Button і задаємо необхідні параметри
text_ip = Button(x = ip.x, y = 10, width = ip.width, height = 45, text = "user ip", size = 50)
# до списку відображення меню додаємо текст ip
m_data.list_blits["menu"].append(text_ip)
# наслідуємо клас Auto і задаємо необхідні параметри
auto = Auto(width= 179, height= 79, x= 794, y= 587)
# наслідуємо клас Button і задаємо необхідні параметри
rotate = Button(fun= 'ship',  width = 222, height = 68, x= 1000, y= 600, name = "", progression= "pre-game", text= "")
# наслідуємо клас Button і задаємо необхідні параметри
play = Button(x = 900, y = 720, name = "", fun= 'play', width = 200, height = 65, text = "",progression='pre-game')
# наслідуємо клас Button і задаємо необхідні параметри
revenge = Button(height = 90, width = 372, x = 28, y = 600, text = "", progression = "win", fun= "win_lose")
# наслідуємо клас Button і задаємо необхідні параметри
out = Button(height = 80, width = 518, x = 0, y = 712, progression = "win", text = "", fun = "check")
# m_data.list_blits["pre-game"].extend([rotate,play])
# revenge = Button(height = 90, width = 372, x = 28, y = 600, text = "", progression = "lose", fun= "win_lose")
# out = Button(height = 80, width = 518, x = 0, y = 712, progression = "lose", text = "", fun = "check")
# наслідуємо клас Button і задаємо необхідні параметри
music =Button(width = 76, height = 72, x = nickname.width + 50, y = 45, text = "", fun = "music", name =  "music")
# наслідуємо клас Button і задаємо необхідні параметри
music2 =Button(width = 76, height = 72, x = 632, y = 22, text = "", fun = "music", name =  "music",progression='pre-game')
music3 =Button(width = 76, height = 72, x = 830, y = 30, text = "", fun = "music", name =  "pause",progression='sounds')
if m_audio.track.stoped:
    music3.name = 'play'
    music3.update_image()
# plus = Button('+',50,50,1200,50,'','sounds','+',70,(255,255,255))
# plus.second_color = [0,0,0]

# до списку відображення гри додаємо музику
m_data.list_blits['game'].append(music2)
# наслідуємо клас Button і задаємо необхідні параметри
client = Button(width= 281, height= 100, name= "button_start", text= "client", x= 42, y= 600, fun= "c_s:client")  
# наслідуємо клас Button і задаємо необхідні параметри
shop = Button(width= 281, height= 90, name= "button_start", text= "shop", x= 387+60, y= 725, fun= "shop",progression="NONE")
# наслідуємо клас Button і задаємо необхідні параметри
shop_ = Button(width= 321, height= 145, name= "", text= "", x= 0, y= 0, fun= "shop",progression='shop', size = 40)
# наслідуємо клас Button і задаємо необхідні параметри
achievements = Button(width= 500, height= 90, name= "button_start", text= "achievements", x= 42, y= 725, fun= "achievements",progression="menu")
# наслідуємо клас Button і задаємо необхідні параметри
achievements_ = Button(width= 281, height= 90, name= "button_start", text= "back to menu", x= 960, y= 15, fun= "achievements",progression='achievements', size = 40)
# наслідуємо клас Button і задаємо необхідні параметри
server = Button(width= 281, height= 100, name= "button_start", text= "server", x= 981, y= 600, fun= "c_s:server")
# наслідуємо клас Button і задаємо необхідні параметри
controls = Button(width= 500, height= 100, name= "button_start", text= "controls", x= 981-500+281, y= 725, fun= "controls")
# наслідуємо клас Button і задаємо необхідні параметри
controls_ = Button(width= 75, height= 75, name= "", text= "", x= 10, y= 10, fun= "controls",progression='controls')
# наслідуємо клас Button і задаємо необхідні параметри
back = Button(width= 75, height= 75, name= "", text= "", x= 10, y= 10, fun= "change:controls",progression='keys')
# m_data.list_blits['keys'].append(controls_)
# до списку відображення музики додаємо повернення назад
m_data.list_blits['sounds'].append(back)
# наслідуємо клас Button і задаємо необхідні параметри
keys = Button(width= 233, height= 186, name= "", text= "", x= 787, y= 316, fun= "change:keys",progression='controls')
# наслідуємо клас Button і задаємо необхідні параметри
sounds = Button(width= 233, height= 186, name= "", text= "", x= 260, y= 316, fun= "change:sounds",progression='controls')
# наслідуємо клас Button і задаємо необхідні параметри
wait = Button(width= 1280, x = 0, y = 712, height= 59, text = "wait", progression= "noke")
# наслідуємо клас Button і задаємо необхідні параметри
enemy_nickname = Button(y = 10, x = 1000, width= 200, height= 40, size = 40)
# наслідуємо клас Button і задаємо необхідні параметри
your_nickname = Button(y = 10, x = 20, width= 200, height= 40, size = 40)
# наслідуємо клас Button і задаємо необхідні параметри
coins = Button(y = 30, x = 950, width= 300, height= 90, size = 40, progression= "shop", text = "0", name = "")
# наслідуємо клас Button і задаємо необхідні параметри
coins_ = Button(y = 688, x = 75, width= 230, height= 120, size = 40, progression= "game", text = "0", name = "")
# coin = Button(y = 50, x = 970, width= 50, height= 50, size = 0, progression= "shop", text = "", name = "duplone")
# наслідуємо клас Button і задаємо необхідні параметри
description = Button(y = 175, x = 950, width= 300, height= 533, size = 20, progression= "shop", text = "select item")
# наслідуємо клас Button і задаємо необхідні параметри
description_ = Button(y = 150, x = 950, width= 300, height= 533, size = 20, progression= "achievements", text = "select achievement",color=(50,200,50))
# наслідуємо клас Button і задаємо необхідні параметри
buy = Button(y = 696, x = 957, width= 321, height= 145, size = 40, progression= "shop", text = "", name = "",fun='buy')
# m_data.list_blits["shop"].append(description)
# наслідуємо клас Button і задаємо необхідні параметри
homing_rocket = Button(y = 235, x = 15, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/homing_rocket")
# наслідуємо клас Button і задаємо необхідні параметри
line_rocket= Button(y = 235, x = 167, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/line_rocket")
# наслідуємо клас Button і задаємо необхідні параметри
fire_rocket = Button(y = 235, x = 319, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/fire_rocket")
# наслідуємо клас Button і задаємо необхідні параметри
rocket_3x3 = Button(y = 235, x = 469, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/rockets/rocket_3x3")
# наслідуємо клас Button і задаємо необхідні параметри
Anti_fire = Button(y = 514, x = 15, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Anti_fire")
# наслідуємо клас Button і задаємо необхідні параметри
radar = Button(y = 514, x = 167, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/radar")
# наслідуємо клас Button і задаємо необхідні параметри
Energetic = Button(y = 514, x = 319, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Energetic")
# наслідуємо клас Button і задаємо необхідні параметри
Air_Defence = Button(y = 514, x = 469, width= 140, height= 140, progression= "shop", text = "", name = "", fun = "weapons/buff/Air_Defence")
# список для зброї
list_weapons = [homing_rocket,rocket_3x3,line_rocket,fire_rocket,Energetic,radar,Air_Defence,Anti_fire]
# наслідуємо клас Button і задаємо необхідні параметри
key = Button(x=200,y=40,width=424,height=107,text='bind the key', progression='keys',size=100)
# наслідуємо клас Button і задаємо необхідні параметри
sound = Button(x=200,y=40,width=526,height=80,text='change sounds', progression='sounds',size=100)
# до списку відображення магазину додаємо список зброї
m_data.list_blits['shop'] += list_weapons+[coins,buy,description]
# перевіряємо підключення серверу
if m_data.client_server == "server":
    # задаємо колір серверу
    server.COLOR =(40,2,255)
# перевіряємо підключення клієнту
if m_data.client_server == "client":
    # задаємо колір клієнту
    client.COLOR =(40,2,255)
# your_turn = Button(width= 272, height= 66, x= 133, y= 712, text= "your step", progression= "", color=(0, 0, 255),size=50)
# наслідуємо клас Button і задаємо необхідні параметри
opponent_turn = Button(width= 350, height= 66, x= 800, y= 712, text= "turn", progression= "", color = (255, 0, 0),size=50)
# до списку відображення гри додаємо твій нікнейм
m_data.list_blits["game"].append(your_nickname)
# до списку відображення гри додаємо нікнейм суперника
m_data.list_blits["game"].append(enemy_nickname)
# до списку відображення програшу додаємо помсту і вихід
m_data.list_blits["lose"].extend([revenge, out])
# цикл для досягнень_кода в досягненнях_дати
for achievement_code in m_data.achievements_data:
    # список прегляду доягнень, наслідування класу Button і задання необхідних параметрів 
    m_data.list_achievements_view[achievement_code] = Button(fun=f"set_achievements/{achievement_code}",width=50,height=50,x=0,y=0,name=f"achievements/{achievement_code}",progression='NONE',text='')
