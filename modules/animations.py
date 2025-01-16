'''
    >>> Відповідяє за створення анімації - класс Animation
    >>> Програє анімації під час гри
'''
# імпортуємо модуль pygame , os
import pygame, os
#імпртуємо модуль modules.data як m_data
import modules.data as m_data
import modules.main_window as main_window
import time
def play_animation():
    while True:
        # print('play')

        list_to_delete = []
        
        for count in range(len(m_data.list_animations)):
            if m_data.list_animations[count]():
                list_to_delete.append(m_data.list_animations[count])
        
        for count in list_to_delete:
            del m_data.list_animations[-(count+1)]
        time.sleep(0.1)
# клас для роботи з зображенням
class Animation():
    # ініціалізуємо зображення
    def __init__(self, width: int, height: int, x: int, y: int, name = '', progression: str = "None", rotate = 0,count_animations = 1,end = 'repeat',max_time= 0): 
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
        self.images = []
        self.count_animations = count_animations
        self.different = 1
        # вказуємо чи можемо ми редагувати зображення
        self.edit_image = True
        self.image = None
        self.count = 0
        self.max_time = max_time
        self.time = max_time
        self.end = end
        # оновлюємо наше зображення
        self.update_image()
        m_data.list_animations.append(lambda:self.animate())
    def animate(self):
        
        if self.time <= 0:
            self.time = self.max_time
            self.count += self.different
        else:
            self.time -= 1
        if self.count == self.count_animations-1:
            if self.end == 'static':
                return True
            elif self.end == 'repeat':
                self.count = 0
            else:
                self.different = -1
        elif self.count <= 0:
            self.different = 1
    # создаємо метод який оновлює наше зображення
    def update_image(self):
        try:
            # завантажуємо зображення з вказаного нам шляху
            self.image = pygame.image.load(os.path.abspath(f"{__file__}/../../animations/{self.name}/{self.name}_0.png"))
            self.image = pygame.transform.rotate(self.image, self.rotate)
            
            if self.edit_image:
                # змінюємо розмір зображення 
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                self.image = pygame.transform.rotate(self.image, self.rotate)
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
                if self.rotate == 0 or self.image.get_width() != int(self.height*multiplier_x) or self.image.get_height() != int(self.width*multiplier_y):
                    print(self.image.get_width(), int(width), 'or', self.image.get_height(), int(height),self.name)
                    # завантажуємо картинку
                    self.images = []
                    try:
                        for count in range(100):
                            print(0)
                            self.image =  pygame.image.load(os.path.abspath(f"{__file__}/../../animations/{self.name}/{self.name}_{count}.png"))
                            print(1)
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
                                self.image = pygame.transform.scale(self.image, (self.height*multiplier_x, self.width*multiplier_y))
                                # задаємо інший розмір квадрату
                                self.rect = pygame.Rect(x,y,height, width)
                                # малює прозорість зображення
                            self.images.append(self.image)
                    except:
                        self.count_animations = len(self.images)
            # відображення зображення на екрані
            screen.blit(self.images[self.count], (x, y))
            
        except Exception as error:
            print('hhaaa',error)