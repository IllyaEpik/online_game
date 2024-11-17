import pygame , socket, random
from modules.images import Image
import modules.data as m_data
from modules.ships import Ship 

class Button(Image):
    def __init__(self, fun = None, width = 100, height = 100, x= 0, y= 0, name = "", progression = "menu", text: str ="Button", size = 65):
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        self.WIDTH_BUT = width
        self.HEIGHT_BUT = height
        self.X = x
        self.Y = y
        self.function = fun
        self.X_text = 497
        self.Y_text = 350
        self.COLOR = (0, 0, 0)
        self.FONT = pygame.font.SysFont("OldEnglishText", size)
        self.TEXT = text  
        self.rect = pygame.Rect(x,y,width,height)

    def button_start(self, event):
        if self.rect.collidepoint(event.pos):
            m_data.ip = input.TEXT.split(" ")[1]
            m_data.progression =  "pre-game"
            print(m_data.ip)
    def blit(self, screen):
        if self.name != "":
            Image.blit(screen=screen, self = self)
        size = self.FONT.size(self.TEXT)
        y = self.y + self.height/2-size[1]/2
        x = self.x + self.width/2-size[0]/2
        screen.blit(self.FONT.render(self.TEXT,True,(0,0,0)), (x, y))

# button = Button()
class Input(Image):
    def __init__(self, width: int, height: int,x = 0,y = 0, name = "", progression = "menu", color = (0,0,0), text = "id: "):
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
        print(self.enter)
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
    def randomship():
        count_ships = 0 
        while True:
            row = random.randint(0, 9)
            cell = random.randint(0, 9)
            if m_data.my_field[row][cell] ==  0:
                ship = Ship(x = 0, y = 0, cell = cell, row = row)
                count_ships += 1
                m_data.my_field[row][cell] = 1
            if count_ships == 4:
                break
            
        count_ships = 0
        while True:
            row = random.randint(0, 9)
            cell = random.randint(0, 9)
            try:
                if m_data.my_field[row][cell] ==  0: 
                    if m_data.my_field[row][cell+1] ==  0: 
                        m_data.my_field[row][cell] = 2
                        m_data.my_field[row][cell+1] = 2
                        ship = Ship(x = 0, y = 0, cell = cell, row = row, name= "2")
                        count_ships += 1
            except:
                pass
            if count_ships == 3:
                break

        count_ships = 0
        while True:
            row = random.randint(0, 9)
            cell = random.randint(0, 9)
            try:
                if m_data.my_field[row][cell] ==  0:
                    if m_data.my_field[row][cell+1] ==  0:
                        if m_data.my_field[row][cell+2] ==  0:
                            m_data.my_field[row][cell+2] = 3
                            m_data.my_field[row][cell+1] = 3
                            m_data.my_field[row][cell] = 3
                            ship = Ship(x = 0, y = 0, cell = cell, row = row, name= "3")
                            count_ships += 1
            except:
                print("deniska sosiska")
            if count_ships == 2:
                break
        
        count_ships = 0
        while True:
            row = random.randint(0, 9)
            cell = random.randint(0, 9)
            try:
                if m_data.my_field[row][cell] ==  0:
                    if m_data.my_field[row][cell+1] ==  0:
                        if m_data.my_field[row][cell+2] ==  0:
                            if m_data.my_field[row][cell+3] ==  0:
                                m_data.my_field[row][cell+3] = 4
                                m_data.my_field[row][cell+2] = 4
                                m_data.my_field[row][cell+1] = 4
                                m_data.my_field[row][cell] = 4
                                ship = Ship(x = 0, y = 0, cell = cell, row = row, name= "4")
                                count_ships += 1
            except:
                pass
            if count_ships == 1:
                break




input = Input(width = 551, height = 165, x = 366 , y = 531, name = "button_start")
button_start = Button(width = 402 , height = 120, x = 435, y = 343, name = "button_start", text= "Start Game")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
ip = Button(x = 981, y = 59, width = 281, height = 84, name = "button_start", text = ip, size = 50)
text_ip = Button(x = 981, y = 10, width = 281, height = 45, text = "user ip", size = 50)
m_data.list_blits["menu"].append(text_ip)