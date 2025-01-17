'''
    >>> Відповідає за перехід між екранами - фунція transform
    >>> Відповідає за анімацію переходу між екранами - функція transform_rect
'''
# імпортуємо рандомайзер
import random
# робимо імпорт pygame
import pygame
# з файлу button імпортуємо кнопку
import modules.buttons as m_buttons
# з дати імпортуємо дату
import modules.data as m_data
# з файлу звука імортуємо аудіо
import modules.audio as m_audio 
# з файлу доягнень імпортуємо досягнення
import modules.achievements as m_achievements
# змінна трансформації зі значенням нічого
type_transform = None

# задаємо ширину
width = 1280
# задаємо висоту
height = 832
# задаємо колір переходу 
color = (0,0,0)
# задаємо розмір переходу
size = 0
# створюємо змінну переходу
progression = None
# задаємо число типів переходів
count_types = 0
# задаємо кінець
end = 0
# функція для трансформації екрану
def transform(screen,multiplier_x,multiplier_y):
    '''
        >>> Трансформує екран
    '''
    # робимо змінні глобальними
    global type_transform,color,progression
    # умова якщо екран нікуди не переходить
    if type_transform == None:
        # задаємо перехід
        progression = m_data.progression
        # задаємо випадковий колір
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        # перевертаємо дісплей
        pygame.display.flip()
    # інакше змінна трансформації набуває значення 0
    elif type_transform == 0:
        # трансформуємо в прямокутну форму
        transform_rect(screen.screen,multiplier_x,multiplier_y)
# функція для трансформування екрану в прямокутну форму   
def transform_rect(screen,multiplier_x,multiplier_y):
    '''
        >>> Змінює розмір прямокутника під час анімації переходу
    '''
    # робить змінні глобальними
    global size,type_transform,color
    # додає до розміру 25
    size += 25
    # зміна розміру прямокутника при переході
    rect = pygame.Rect((640 - size/2*1.53846153846)*multiplier_x, (416 - size/2)*multiplier_y, size*multiplier_x*1.53846153846,size*multiplier_y)
    # надаємо параметри для ходу
    m_buttons.stroke(screen,rect,
                     color,10)
    # оновлюємо перехід екрану
    pygame.display.update(rect)
    # перевіряємо розмір
    if size > 832:
        # змінюємо значення трансформації на нічого
        type_transform = None
        # змінюємо розмір на 0
        size = 0
