# імпорт чужих модулів для роботи
import pygame , socket
import threading, random
# імпорт наших модулів
from modules.images import Image
import modules.data as m_data
import modules.client as m_client 
import modules.server as m_server
from modules.ships import Ship,fill_field
# класс з кнопками
class Button(Image):
    # метод з створенням параметрів
    def __init__(self, fun = None, width = 100, height = 100, x= 0, y= 0, name = "", progression = "menu", text: str ="Button", size = 65):
        # задаємо параметри в класс зображень
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        # переносимо параметри в змінні
        self.WIDTH_BUT = width
        self.HEIGHT_BUT = height
        self.X = x
        self.Y = y
        self.function = fun
        self.TEXT = text  
        # створюємо параметри
        self.COLOR = (0, 0, 0)
        self.FONT = pygame.font.SysFont("OldEnglishText", size)
        self.rect = pygame.Rect(x,y,width,height)
    # метод з кнопкою старт
    def button_start(self, event):
        # якщо кнопка натиснута
        if self.rect.collidepoint(event.pos):
            # якщо функція корабль то
            if self.function == "ship":
                # цикл для всіх кораблів
                for ship in m_data.all_ships:
                    # якщо корабль виділен
                    if ship.select:
                        # поворот корабля   
                       ship.rotate_ship()
                        # виділення корабля
                       ship.select  = False
            # інакше функція гра
            elif self.function == "play":

                # змінна да_ні дорівнює правді
                yes_no = True
                # цикл для стандартних клітинок
                for row in m_data.cells:
                    # цикл для клітинок в ряду
                    for cell in m_data.cells[row]:
                        # якщо кораблі не розставлені
                        if cell[0]:
                            # змінна да_ні змінюється на неправду 
                            yes_no =  False
                # якщо всі кораблі розставлені
                if yes_no:
                    # переходимо в гру
                    m_data.progression = "game"
                    # активує клієнта одночасно з роботою кода
                    print('good')
                    threading.Thread(target = m_client.activate).start()
                    print('asd')
                    # активує сервер
                    threading.Thread(target = m_server.activate,daemon=True).start()
            else:
                # записання ip d
                m_data.ip = input.TEXT.split(" ")[1]
                # перехід в пре-гру
                m_data.progression =  "pre-game"
                
                # for row in m_data.my_field:
                #     print(row)
    # метод відображення поверхні на головному окні
    def blit(self, screen):
        # якщо картинка задана 
        if self.name != "":
            # відображення картинки
            Image.blit(screen=screen, self = self)
        # задання розміру для тексту
        size = self.FONT.size(self.TEXT)
        # задаємо y для тексту
        y = self.y + self.height/2-size[1]/2
        # задаємо x для тексту
        x = self.x + self.width/2-size[0]/2
        # відображення тексту на екрані
        screen.blit(self.FONT.render(self.TEXT,True,(0,0,0)), (x, y))

# button = Button()
class Input(Image):
    def __init__(self, width: int, height: int,x = 0,y = 0, name = "", progression = "menu", color = (0,0,0), text = "ip: "):
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        self.COLOR = color
        self.FONT = pygame.font.SysFont("OldEnglishText", 65)
        self.TEXT = text 
        self.RENDER_TEXT = None
        self.enter = False
        self.edit("ok")
        self.rect = pygame.Rect(x,y,width,height)
        self.list = "0123456789."
    def blit(self, screen):
        Image.blit(screen=screen, self = self)
        size = self.FONT.size(self.TEXT)
        # кордината + половина высоты кнопки - половина высоты текста
        y = self.y + self.height/2 - size[1]/2
        x = self.x + self.width/2 - size[0]/2
        screen.blit(self.RENDER_TEXT, (x,y))
    def activate(self, event):
        if self.rect.collidepoint(event.pos):
            self.enter = True
        else:
            self.enter = False
        # print(self.enter)
    def edit(self,event):
        if self.enter:
            key = pygame.key.name(event.key)
            if event.key == pygame.K_BACKSPACE and self.TEXT != "id: ":
                
                # Убирает последний символ текста 
                self.TEXT = self.TEXT[:-1]
            elif key in self.list:
                # Добавляет символ который был нажат пользователем
                self.TEXT += key

        self.RENDER_TEXT = self.FONT.render(self.TEXT, True, self.COLOR)
class Auto(Image):
    def __init__(self, width: int, height: int, x: int, y: int, name='', progression: str = "pre-game"):
        super().__init__(width, height, x, y, name, progression)
        self.rect = pygame.Rect(x,y,width,height)
    def randomship(self, cor):
        # print("Hello")
        if self.rect.collidepoint(cor):
            count = 0
            count_ships = 0  
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
            m_data.all_ships = []
            for row in m_data.cells:
                for cell in m_data.cells[row]:
                    cell[0] =  False
            # for ship in m_data.all_ships:
                
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                if m_data.my_field[row][cell] ==  0:
                    ship = Ship(x = 59, y = 115, cell = cell, row = row, rotate = rotate * 90)
                    count_ships += 1
                    m_data.my_field[row][cell] = 1
                    fill_field(m_data.my_field)
                if count_ships == 4 or count > 1000:
                    break
                
            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try: 

                    if m_data.my_field[row][cell] == 0: 
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1: 
                            ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "2", rotate = rotate * 90)
                            count_ships += 1
                            fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 3 or count > 1000:
                    break

            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try:
                    if m_data.my_field[row][cell] == 0:
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "3", rotate= rotate * 90)
                                count_ships += 1
                                fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 2 or count > 1000:
                    break
            
            count_ships = 0
            while True:
                row = random.randint(0, 9)
                cell = random.randint(0, 9)
                rotate = random.randint(0, 4)
                count += 1
                try:
                    if m_data.my_field[row][cell] ==  0:
                        if m_data.my_field[row][cell+1] == 0 and rotate % 2 == 0 or m_data.my_field[row+1][cell] == 0 and rotate % 2 == 1:
                            if m_data.my_field[row][cell+2] == 0 and rotate % 2 == 0 or m_data.my_field[row+2][cell] == 0 and rotate % 2 == 1:
                                if m_data.my_field[row][cell+3] == 0 and rotate % 2 == 0 or m_data.my_field[row+3][cell] == 0 and rotate % 2 == 1:
                                    ship = Ship(x = 59, y = 115, cell = cell, row = row, name= "4", rotate= rotate * 90)
                                    count_ships += 1
                                    fill_field(m_data.my_field)
                except:
                    pass
                if count_ships == 1 or count > 1000:
                    for row1 in m_data.my_field:
                        print(row1)

                    break
            if count > 1000:
                self.randomship(cor)



input = Input(width = 551, height = 165, x = 366 , y = 531, name = "button_start")
button_start = Button(width = 402 , height = 120, x = 435, y = 343, name = "button_start", text= "Start Game")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
ip = Button(x = 981, y = 59, width = 281, height = 84, name = "button_start", text = ip, size = 50)
text_ip = Button(x = 981, y = 10, width = 281, height = 45, text = "user ip", size = 50)
m_data.list_blits["menu"].append(text_ip)
auto = Auto(width= 170, height= 58, x= 665, y= 610)
rotate = Button(fun= 'ship',  width = 225, height = 58, x= 886, y= 611, name = "", progression= "pre-game", text= "")
play = Button(x = 1000, y = 720, name = "", fun= 'play', width = 170, height = 60)
# m_data.list_blits["pre-game"].append(auto)