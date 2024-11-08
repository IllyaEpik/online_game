import pygame
from modules.images import Image


class Button(Image):
    def __init__(self, fun = None, width = 100, height = 100, x= 0, y= 0, name = "", progression = "menu"):
        Image.__init__(self, width=width, height=height, x=x, y=y, name=name, progression=progression)
        self.WIDTH_BUT = width
        self.HEIGHT_BUT = height
        self.X = x
        self.Y = y
        self.function = fun
    
        # self.X_text = 499
        # self.Y_text = 228
        # self.COLOR = (97, 152, 255)
        # self.FONT = pygame.font.SysFont("Inter", 65)
        # self.TEXT = "Create server"
        # print(self.FONT.size('create server'))
        # self.screen = screen
    def blit(self, screen):
        Image.blit(screen=screen, self = self)
    # def create_button(self, screen):
    #     pygame.draw.rect(screen,
    #                      self.COLOR , 
    #                      pygame.Rect(self.X, self.Y,self.WIDTH_BUT,self.HEIGHT_BUT))
    #     screen.blit(self.FONT.render(self.TEXT,True,(255, 255, 255)), (self.X_text, self.Y_text))

# button = Button()

button_nickname = Button(width = 551, height = 165, x = 366 , y = 531, name = "button_start")
button_start = Button(width = 402 , height = 120, x = 435, y = 343, name = "button_start")