# імпортуємо модуль pygame , os
import pygame, os
#імпртуємо модуль modules.data як m_data
import modules.data as m_data
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
        self.edit_image = edit
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
                # повертаємо наше зображення 
                self.image = pygame.transform.rotate(self.image, self.rotate) 
            
            # пепевіряємо чи є наше зораження в  списку в якому все відображаться на екрані
            if self in m_data.list_blits[self.progression]:
                pass
            else:
                # ми додаємо в цей список наше зображення
                m_data.list_blits[self.progression].append(self)
        except:
            # якщо сталась помилка при завантаженні зображення - ми пишемемо її
            print("Error: image",self.name)
    # создаємо метод який відображє наше зображення
    def blit(self, screen):
        # відображаємо наше зображення
        screen.blit(self.image, (self.x, self.y))
    
# создаємо задній фон за меню
background = Image(width = 1280, height = 851, x = 0, y = 0, name = "background")
# создаємо фон для етапу розсташування кораблів
playing_field = Image(width = 1280, height = 832, x = 0, y = 0, name = "playing_field", progression = "pre-game")

right_ship = Image(width = 388, height = 318, x = 903, y = 243, name = "right_ship")
left_ship = Image(width = 381, height = 316, x = 10, y = 260, name = "left_ship")
hat = Image(width = 187, height = 150, x= 370, y = 252, name = "hat")
# создаємо фон для самої гри
play_field = Image(width = 1280, height = 851, x = 0, y = 0, name = "play_field", progression = "game", edit = False)