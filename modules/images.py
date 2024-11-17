import pygame, os 
import modules.data as m_data

class Image():
    def __init__(self, width: int, height: int, x: int, y: int, name = '', progression: str= "menu"):
        self.width = width
        self.height = height
        self.x = x
        self.y = y 
        self.name = name 
        self.progression = progression
        self.image = None 
        self.update_image()
        
    def update_image(self):
        try:
            self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{self.name}.png"))
            print(self.name)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
            print(self.name)

            if self in m_data.list_blits:
                pass
            else:
                m_data.list_blits[self.progression].append(self)
        except:
            print("Error: image",self.name)

    def blit(self, screen):
    
        screen.blit(self.image, (self.x, self.y))
    

background = Image(width = 1280, height = 851, x = 0, y = 0, name = "background")
playing_field = Image(width = 1280, height = 832, x = 0, y = 0, name = "playing_field", progression = "pre-game")
right_ship = Image(width = 388, height = 318, x = 903, y = 243, name = "right_ship")
left_ship = Image(width = 381, height = 316, x = 10, y = 260, name = "left_ship")
hat = Image(width = 187, height = 150, x= 370, y = 252, name = "hat")
