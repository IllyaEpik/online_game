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
        self.opasity = 255
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
            self.image = pygame.transform.rotate(self.image, self.rotate)
            
            if self.edit_image:
                # змінюємо розмір зображення 
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.image = pygame.transform.rotate(self.image, self.rotate)
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
    # метод для відображення на екрані
    def blit(self,screen,x,y,width,height,multiplier_x,multiplier_y):
        # перевіряємо отриману ширину і висоту
        try:
            if self.image.get_width() != int(width) or self.image.get_height() != int(height):
                print(self.image.get_width(), width, self.image.get_height(), height)
                # завантажуємо картинку
                self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{self.name}.png"))
                # перевертаємо картинку
                self.image = pygame.transform.rotate(self.image, self.rotate)
                # перевіряємо оберт екрану
                if self.rotate % 180 == 0:
                    # змінює масштаб
                    self.image = pygame.transform.scale(self.image, (width, height))
                    # задаємо розмір квадрату 
                    self.rect = pygame.Rect(x,y,width,height)
                    # малює прозорість зображення
                    self.image.set_alpha(self.opasity)
                else:
                    # задаємо інший масштаб картинки
                    self.image = pygame.transform.scale(self.image, (self.height * multiplier_x, self.width * multiplier_y))
                    # задаємо інший розмір квадрату
                    self.rect = pygame.Rect(x,y,self.height * multiplier_x, self.width * multiplier_y)
                    # малює прозорість зображення
                    self.image.set_alpha(self.opasity)
            # відображення зображення на екрані
            screen.blit(self.image, (x, y))
        except:
            print('hhaaa')
# задаємо параметри для фону 
background = Image(width = 1280, height = 851, x = 0, y = 0, name = "background")
# задаємо параметри для фону магазину
background_shop = Image(width = 1280, height = 832, x = 0, y = 0, name = "background_shop",progression='shop')
background_achievements = Image(width = 1280, height = 832, x = 0, y = 0, name = "background_shop",progression='achievements')
# задаємо параметри для грального поля
playing_field = Image(width = 1280, height = 832, x = 0, y = 0, name = "playing_field", progression = "pre-game")
# задаємо параметри для поля гри
play_field = Image(width = 1280, height = 835, x = 0, y = 0, name = "play_field", progression = "game")
# задаємо параметри для екрану програшу
lose = Image(width = 1280, height = 852, x = 0, y = 0, name = "lose", progression = "lose", edit = False)
# задаємо параметри для екрану перемоги
win = Image(width = 1280, height = 852, x = 0, y = 0, name = "win", progression = "win", edit = False)
# задаємо параметри для іконок ракет
rockets_icon = Image(width = 130, height = 130, x = 50, y = 180, name = "weapons/rockets_icon", progression = "shop")
# задаємо параметри для серця
hearts = Image(width = 130, height = 130, x = 50, y = 410, name = "weapons/hearts", progression = "shop")
# задаємо параметри для екрану досягнень
background_achievements = Image(width = 1280, height = 851, x = 0, y = 0, name = "achievements", progression = "achievements")
# задаємо параметри для протиповітряної охорони
air_defence = Image(55.7,55.7,-999,-99,'weapons/Air_Defence',progression='None')