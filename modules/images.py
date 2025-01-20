'''
    >>> Працює з зображеннями - клас Image
    >>> Оновлюємо зображення - метод update_image
    >>> Відображує картинки на екрані - метод blit
'''
# імпортуємо модуль pygame , os
import pygame, os
#імпртуємо модуль modules.data як m_data
import modules.data as m_data
import modules.main_window as main_window
# клас для роботи з зображенням
class Image():
    '''
        >>> Задаємо параметри до зображення
    '''
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
        self.row = None
        self.cell = None
        # создаємо змінну self.image
        self.image = None
        # self.select_image = None
        # self.main_image = None
        # self.current_select = 0
        self.last_name = None
        # вказуємо чи можемо ми редагувати зображення
        self.edit_image = True
        # оновлюємо наше зображення
        self.update_image()
        if self.progression in m_data.list_blits:
            if self in m_data.list_blits[self.progression]:
                pass
            else:
                # ми додаємо в цей список наше зображення
                m_data.list_blits[self.progression].append(self)
    # создаємо метод який оновлює наше зображення
    def update_image(self):
        '''
            >>> Завантажує зображення за вказаним шляхом
            >>> Змінює розмір зображення
        '''
        try:
            # завантажуємо зображення з вказаного нам шляху
            self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{self.name}.png"))
            self.image = pygame.transform.rotate(self.image, self.rotate)
            
            if self.edit_image:
                # змінюємо розмір зображення 
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.image = pygame.transform.rotate(self.image, self.rotate)
            # пепевіряємо чи є наше зораження в  списку в якому все відображаться на екрані
            
        except :
            # якщо сталась помилка при завантаженні зображення - ми пишемемо її
            pass
    # создаємо метод який відображє наше зображення
    # def blit(self, screen):

    #     # відображаємо наше зображення
    #     screen.blit(self.image, (self.x, self.y))
    # метод для відображення на екрані
    def blit(self,screen,x,y,width,height,multiplier_x,multiplier_y):
        '''
            >>> Відображуємо картинку на екрані
        '''
        # перевіряємо отриману ширину і висоту
        # s = pygame.time.get_ticks()
        # self.image = self.main_image
        # if self.current_select:
        #     self.image = self.
        try:
            if self.name != self.last_name or self.image.get_width() != int(width) or self.image.get_height() != int(height) :
                if self.rotate == 0 or self.image.get_width() != int(self.height*multiplier_x) or self.image.get_height() != int(self.width*multiplier_y) or self.name != self.last_name:
                    
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
                        # self.image.set_alpha(self.opasity)
                    else:
                        # задаємо інший масштаб картинки
                        self.image = pygame.transform.scale(self.image, (self.height*multiplier_x, self.width*multiplier_y))
                        # задаємо інший розмір квадрату
                        self.rect = pygame.Rect(x,y,height, width)
                        # малює прозорість зображення
                        # self.image.set_alpha(self.opasity)
                    self.last_name = self.name
            # відображення зображення на екрані
            screen.blit(self.image, (x, y))
        except:
            pass
        # e = pygame.time.get_ticks()
        # if e-s:
# задаємо параметри для фону 
background = Image(width = 1280, height = 832, x = 0, y = 0, name = "background")
# задаємо параметри для фону магазину
background_shop = Image(width = 1280, height = 832, x = 0, y = 0, name = "background_shop",progression='shop')
background_achievements = Image(width = 1280, height = 832, x = 0, y = 0, name = "background_achievements",progression='achievements')
background_keys_and_sounds = Image(progression='keys',width=1280,height= 832,name="background_keys_and_sounds",x=0,y=0)
m_data.list_blits['sounds'].append(background_keys_and_sounds)
# задаємо параметри для грального поля
playing_field = Image(width = 1280, height = 832, x = 0, y = 0, name = "playing_field", progression = "pre-game")
# задаємо параметри для поля гри
play_field = Image(width = 1280, height = 832, x = 0, y = 0, name = "play_field", progression = "game")
# задаємо параметри для екрану програшу
lose = Image(width = 1280, height = 832, x = 0, y = 0, name = "lose", progression = "lose", edit = False)
# задаємо параметри для екрану перемоги
win = Image(width = 1280, height = 832, x = 0, y = 0, name = "win", progression = "win", edit = False)
# задаємо параметри для екрану досягнень
background_achievements = Image(width = 1280, height = 832, x = 0, y = 0, name = "achievements", progression = "achievements")
background_achievements = Image(width = 1280, height = 832, x = 0, y = 0, name = "background_controls", progression = "controls")
# задаємо параметри для протиповітряної охорони
air_defence = Image(55.7,55.7,-999,-99,'weapons/Air_Defence',progression='None')
target = Image(50,50,-99,-5798,'target',progression='capybara')