import pygame
# from .main_window import screen

class Button():
    def __init__(self):
        self.WIDTH_BUT = 382
        self.HEIGHT_BUT = 110
        self.X = 449
        self.Y = 200
        self.X_text = 499
        self.Y_text = 228
        self.COLOR = (97, 152, 255)
        self.FONT = pygame.font.SysFont("Inter", 65)
        self.TEXT = "Create server"
        print(self.FONT.size('create server'))
        # self.screen = screen
    def create_button(self, screen):
        pygame.draw.rect(screen,
                         self.COLOR , 
                         pygame.Rect(self.X, self.Y,self.WIDTH_BUT,self.HEIGHT_BUT))
        screen.blit(self.FONT.render(self.TEXT,True,(255, 255, 255)), (self.X_text, self.Y_text))

button = Button()