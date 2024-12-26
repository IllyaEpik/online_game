# імпортуємо модуль pygame , os
import pygame, os
#імпртуємо модуль modules.data як m_data
import modules.data as m_data
import modules.main_window as main_window
# клас для роботи з зображенням
class Image():
    # ініціалізуємо зображення
    def __init__(self, width: int, height: int, x: int, y: int, name = '', progression: str = "menu", rotate = 0, edit = True): 
        # переносимо параметри в змінні
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.name = name 
        self.progression = progression
        self.rotate = rotate
        # создаємо змінну self.image
        self.image = None 
        # вказуємо чи можемо ми редагувати зображення
        self.edit_image = True
        # оновлюємо наше зображення
        self.update_image()
    # создаємо метод який оновлює наше зображення
    def update_image(self):
        try:
            # завантажуємо зображення з вказаного нам шляху
            self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{self.name}.png"))
            
            
            if self.edit_image:
                # змінюємо розмір зображення 
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
            
            # пепевіряємо чи є наше зораження в  списку в якому все відображаться на екрані
            if self in m_data.list_blits[self.progression]:
                pass
            else:
                # ми додаємо в цей список наше зображення
                m_data.list_blits[self.progression].append(self)
        except :
            # якщо сталась помилка при завантаженні зображення - ми пишемемо її
            print("Error: image",self.name)
    # создаємо метод який відображє наше зображення
    # def blit(self, screen):
        
    #     # відображаємо наше зображення
    #     screen.blit(self.image, (self.x, self.y))
    def blit(self,screen,x,y,width,height,multiplier_x,multiplier_y):
        if self.image.get_width() != width or self.image.get_height() != height:
            self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{self.name}.png"))
            self.image = pygame.transform.scale(self.image, (width, height))
            self.rect = pygame.Rect(x,y,width,height)
            # self.update_image()
        screen.blit(self.image, (x, y))
# создаємо задній фон за меню
background = Image(width = 1280, height = 851, x = 0, y = 0, name = "background")
# создаємо фон для етапу розсташування кораблів
playing_field = Image(width = 1280, height = 832, x = 0, y = 0, name = "playing_field", progression = "pre-game")
# создаємо фон для самої гри
play_field = Image(width = 1280, height = 851, x = 0, y = 0, name = "play_field", progression = "game", edit = False)
lose = Image(width = 1280, height = 851, x = 0, y = 0, name = "lose", progression = "lose", edit = False)
win = Image(width = 1280, height = 851, x = 0, y = 0, name = "win", progression = "win", edit = False)

your_turn = Image(width= 272, height= 66, x= 133, y= 712, name= "your_step", progression= "", edit= False)
opponent_turn = Image(width= 350, height= 66, x= 772, y= 712, name= "opponent_step", progression= "", edit= False)

your_turn_gray = Image(width= 272, height= 66, x= 133, y= 712, name= "your_step_gray", progression= "", edit= False)
opponent_turn_gray = Image(width= 350, height= 66, x= 772, y= 712, name= "opponent_step_gray", progression= "", edit= False)