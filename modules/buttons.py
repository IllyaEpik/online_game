import pygame
from modules.images import Image
import modules.data as m_data

class Button(Image):
    def __init__(self, fun = None, width = 100, height = 100, x= 0, y= 0, name = "", progression = "menu", text : str ="Button" ):
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        self.WIDTH_BUT = width
        self.HEIGHT_BUT = height
        self.X = x
        self.Y = y
        self.function = fun
        self.X_text = 497
        self.Y_text = 350
        self.COLOR = (0, 0, 0)
        self.FONT = pygame.font.SysFont("OldEnglishText", 65)
        self.TEXT = text 
        self.rect = pygame.Rect(x,y,width,height)

    def button_start(self, event):
        if self.rect.collidepoint(event.pos):
            m_data.id = input.TEXT.split(" ")[1]
            m_data.progression =  "pre-game"
            print(m_data.id)
    def blit(self, screen):
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
input = Input(width = 551, height = 165, x = 366 , y = 531, name = "button_start")
button_start = Button(width = 402 , height = 120, x = 435, y = 343, name = "button_start", text= "Start Game")