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

# 1280
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
# задаємо прозорість
# opasity = 255
# задаємо кінець
end = 0
# функція для трансформації екрану
def transform(screen,multiplier_x,multiplier_y):
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
    # elif type_transform == 1:
    #     transform_opasity(screen)
# функція для трансформування екрану в прямокутну форму   
def transform_rect(screen,multiplier_x,multiplier_y):
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

# def transform_opasity(screen):
#     global progression,opasity,type_transform,end
#     size1 = screen.screen.get_size()
#     WIDTH = size1[0]
#     HEIGHT= size1[1]
#     multiplier_x = (WIDTH / 100) / (1280 / 100)
#     multiplier_y = (HEIGHT / 100) / (832 / 100)
#     # цикл відображення всього що є в списку
#     for sprite in m_data.list_blits[progression]:
#         # print(sprite.name)
#         # відображення елементу
#         # print(sprite)
#         # if m_data.progression == 'shop':
#         #     print(sprite.x,sprite.y,sprite.name)
#         sprite.opasity = opasity
#         sprite.blit(screen.screen,
#                         sprite.x*multiplier_x,
#                         sprite.y*multiplier_y,
#                         sprite.width*multiplier_x,
#                         sprite.height*multiplier_y,
#                         multiplier_x,multiplier_y)
#         sprite.opasity = 255
#     if progression == "menu" and m_audio.track.stoped:
#         # pygame.draw.line(screen.screen,(255,50,50,opasity),
#         #                          (m_buttons.music.x*multiplier_x,m_buttons.music.y*multiplier_y,),
#         #                          (m_buttons.music.x*multiplier_x + m_buttons.music.width*multiplier_x,m_buttons.music.y*multiplier_y + m_buttons.music.height*multiplier_y),10)
        
#         line = pygame.Surface((m_buttons.music.width*multiplier_x,m_buttons.music.height*multiplier_y))
#         # background = m_data.list_blits[progression][0]
#         # if background.image.get_width() != width or background.image.get_height() != height:
#         #     background.image = pygame.image.load(os.path.abspath(f"{__file__}/../../images/{background.name}.png"))
#         #     background.image = pygame.transform.rotate(background.image, background.rotate)
#         #     if background.rotate % 180 == 0:
#         #         background.image = pygame.transform.scale(background.image, (width, height))
#         #         background.rect = pygame.Rect(x,y,width,height)
#         #     else:
#         #         background.image = pygame.transform.scale(background.image, (background.height * multiplier_x, background.width * multiplier_y))
#         #         background.rect = pygame.Rect(x,y,background.height * multiplier_x, background.width * multiplier_y)
#             # self.update_image()
#         m_data.list_blits[progression][0].image.set_alpha(255)
#         line.blit(m_data.list_blits[progression][0].image, (-m_buttons.music.x*multiplier_x,-m_buttons.music.y*multiplier_y))
#         line.blit(m_buttons.music.image, (0,0))
#         pygame.draw.line(line,(255,50,50),
#                         (0,0,),
#                         (m_buttons.music.width*multiplier_x,m_buttons.music.height*multiplier_y),10)
#         line.set_alpha(opasity)
#         screen.screen.blit(line,(m_buttons.music.x*multiplier_x,m_buttons.music.y*multiplier_y))
#     # якщо знаходимось не в меню то
#     if m_data.list_achievements != []:
#     # for achievement in m_data.list_achievements:
#         achievement = m_data.list_achievements[0]
#         achievement.move()
#         achievement.blit(screen.screen,multiplier_x,multiplier_y)
#     if progression in "pre-game":
#         # цикл для відображення всіх кораблів
#         for ship in m_data.all_ships:
#             ship.opasity = opasity
#             if ship.jump_cor[2]:
#                 ship.x += ship.jump_cor[0]
#                 ship.y -= ship.jump_cor[1]
#                 if not ship.jump_cor[3]:
#                     ship.jump_cor[0] /= 1.1
#                     ship.jump_cor[1] -= 2.5
#                 elif ship.y == 120:
#                     ship.jump_cor[3] = False
#                     ship.jump_cor[-2] = False
                    
#                     m_achievements.achievement('the bug')
#             if ship.y > screen.screen.get_size()[1]+1000:
#                 ship.y = -100
#                 ship.jump_cor[0] =0
#                 ship.jump_cor[1] = -20
#                 ship.jump_cor[3] = True
#                 ship.x = 805
#             ship.blit(screen.screen,ship.x*multiplier_x,ship.y*multiplier_y,ship.width*multiplier_x,ship.height*multiplier_y,multiplier_x,multiplier_y)
#             ship.opasity = 255
#     if progression == "game":
#         for sprite in m_data.list_blits["game"]:
#             if sprite.name in "miss, explosion":
#                 sprite.opasity = opasity
#                 sprite.blit(screen.screen,
#                         sprite.x*multiplier_x,
#                         sprite.y*multiplier_y,
#                         sprite.width*multiplier_x,
#                         sprite.height*multiplier_y,
#                         multiplier_x,multiplier_y)
#                 sprite.opasity = 255
#         if m_data.connected:
#             if m_data.turn:
#                 m_buttons.opponent_turn.COLOR = (140, 140, 140)
#                 m_buttons.your_turn.COLOR = (0, 0, 255)
#             else:
#                 m_buttons.opponent_turn.COLOR = (255, 0, 0)
#                 m_buttons.your_turn.COLOR = (140, 140, 140)
#             sprite = m_buttons.your_turn
#             sprite.opasity = opasity
#             m_buttons.your_turn.blit(screen.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
#             sprite.opasity = 255
#             sprite = m_buttons.opponent_turn
#             sprite.opasity = opasity
#             m_buttons.opponent_turn.blit(screen.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
#             sprite.opasity = 255
#         else:
#             sprite.opasity = opasity
#             wait = m_buttons.wait
#             wait.blit(screen.screen,wait.x*multiplier_x,wait.y*multiplier_y,wait.width*multiplier_x,wait.height*multiplier_y,multiplier_x,multiplier_y)
#             sprite.opasity = 255
#     elif progression == 'shop':
#         square = pygame.Surface((m_buttons.description.rect.width,m_buttons.description.rect.height))
#         square.fill((255, 255, 255))
#         square.set_alpha(opasity-55)
#         rect = pygame.Rect(0,0,m_buttons.description.rect.width,m_buttons.description.rect.height)
#         m_buttons.stroke(square,rect,(0,0,0),10)
#         screen.screen.blit(square,m_buttons.description.rect)
#         sprite = m_buttons.description
#         sprite.opasity = opasity
#         m_buttons.description.blit(screen.screen,
#                         sprite.x*multiplier_x,
#                         sprite.y*multiplier_y,
#                         sprite.width*multiplier_x,
#                         sprite.height*multiplier_y,
#                         multiplier_x,multiplier_y)
#         sprite.opasity = 255
#     opasity -= 15
#     print(opasity)
#     pygame.display.flip()
#     if opasity < 1:
#         opasity = 255
#         end = 1
#     if end:
#         type_transform = None
#         end = 0