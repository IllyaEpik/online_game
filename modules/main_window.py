# імпортуємо модуль pygame
import pygame, threading, os
# ініціалізуємо pygame
pygame.init()
# імпортуємо наші модулі 
import modules.data as m_data
import modules.buttons as m_buttons
import modules.images as m_images
import modules.clients_server as m_client
import modules.ships as m_ships
import modules.attack as m_attack
import modules.transform as m_transform
import modules.audio as m_audio
import modules.achievements as m_achievements
# m_achievements.achievement('Glory to Air Defense')
# m_achievements.achievement('Big Spender')
# m_achievements.achievement('Pants on Fire')
# 
class Screen():
    # ініціалізуємо screen
    def __init__(self):
        size = pygame.display.Info()
        # создаємо таймер
        self.clock = pygame.time.Clock()
        # вказуємо ширину
        self.WIDTH= size.current_w * 0.75
        # вказуємо висоту
        self.HEIGHT = size.current_h * 0.75
        # создаємо екран
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT),pygame.RESIZABLE)
        self.counter = 0

        # задаємо назву нашому екрану
        pygame.display.set_caption('online game')
        
        icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon_peaceful.png"))
        pygame.display.set_icon(icon)
    # функція запуску
    def run(self):
        # m_data.progression = 'lose'
        # задаємо правдиве значення грі
        game = True
        self.counter += 1
        
        # цикл поки гра активна
        size = pygame.display.Info()
        # m_data.progression = 'shop'
        while game:
            size1 = self.screen.get_size()
            WIDTH = size1[0]
            HEIGHT= size1[1]
            multiplier_x = (WIDTH / 100) / (1280 / 100)
            multiplier_y = (HEIGHT / 100) / (832 / 100)
            # print(width2)
            # print(size,size1)
            # цикл всіх подій
            # if self.counter == 5:
            for event in pygame.event.get():
                # якщо вікно зачинено то 

                if event.type == pygame.QUIT:
                    # значення гри неправда
                    game = False
                    m_data.end=True
                    try:
                        # відключаємо клієнта
                        m_client.client.close()
                    except:
                        pass 
                # коли кнопка миші натиснута
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if m_transform.type_transform == None:
                        if m_data.progression in "winlose":
                            m_buttons.revenge.button_start(event)
                            if m_buttons.out.button_start(event):
                                game = False
                                m_data.end=True
                                try:
                                    # відключаємо клієнта
                                    m_client.client.close()
                                except:
                                    pass 
                        # якщо прогресс дорівнює меню то
                        if m_data.progression == "menu":
                            # вибір місця написання
                            m_buttons.input.activate(event) 
                            m_buttons.nickname.activate(event)
                            m_buttons.music.button_start(event)
                            m_buttons.client.button_start(event)
                            m_buttons.server.button_start(event)
                            m_buttons.achievements.button_start(event)
                            # перехід в пре-гру етап
                            m_buttons.button_start.button_start(event)
                        # якщо прогресс дорівнює пре-грі то
                        elif m_data.progression == 'achievements':
                            m_buttons.achievements_.button_start(event)
                            for achievement in m_data.list_achievements_view:
                                m_data.list_achievements_view[achievement].button_start(event)
                        if m_data.progression == "pre-game":
                            # преходить в гру
                            m_buttons.play.button_start(event)
                            # автоматична розтановка кораблів
                            m_buttons.auto.randomship(event.pos)
                            # поворот кораблів
                            m_buttons.rotate.button_start(event)

                            # цикл всіх кораблів
                            for ship in m_data.all_ships:
                                # виділення кораблів
                                ship.activate(event, multiplier_x, multiplier_y)
                        # якщо прогресс дорівнює грі то
                        if m_data.progression == "game":
                            # вибір місця атаки
                            m_attack.attack(event.pos,multiplier_x,multiplier_y)
                            m_buttons.shop.button_start(event)
                            
                        elif m_data.progression == 'shop':
                            m_buttons.shop_.button_start(event)
                            m_buttons.buy.button_start(event)
                            
                            for weapon in m_buttons.list_weapons:
                                weapon.button_start(event=event)
                    # якщо будь-яка клавіша натиснута то
                    else:
                        m_transform.type_transform = None
                        m_transform.size = 0
                if event.type == pygame.KEYDOWN and m_data.progression == "menu":
                    # додає символи до input
                    m_buttons.input.edit(event)
                    m_buttons.nickname.edit(event)
                    for object in [m_buttons.nickname]:
                        size = object.FONT.size(object.TEXT)
                        # if object.width < size[0] - 10:
                        width = -(object.start_width - size[0] - 10)
                        object.width = width + object.start_width
                        if object.width < object.start_width:
                            object.width = object.start_width
                        object.update_image()
                        
                        m_buttons.music.rect = pygame.Rect(m_buttons.music.x, m_buttons.music.y,m_buttons.music.width,m_buttons.music.height)
                        m_buttons.music.x = m_buttons.nickname.width + 50
                        # else:
                            # object.width = object.start_width
                            # object.update_image()
            m_buttons.coins.TEXT = f"{m_data.coins}"
            # цикл відображення всього що є в списку
            s = pygame.time.get_ticks()
            for sprite in m_data.list_blits[m_data.progression]:
                # print(sprite.name)
                # відображення елементу
                # print(sprite)
                # if m_data.progression == 'shop':
                #     print(sprite.x,sprite.y,sprite.name)
                sprite.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
            
            e = pygame.time.get_ticks()
            if m_data.progression == "menu" and m_audio.track.stoped:
                pygame.draw.line(self.screen,(255,50,50),
                                 (m_buttons.music.x*multiplier_x,m_buttons.music.y*multiplier_y,),
                                 (m_buttons.music.x*multiplier_x + m_buttons.music.width*multiplier_x,m_buttons.music.y*multiplier_y + m_buttons.music.height*multiplier_y),10)
            # якщо знаходимось не в меню то
            if m_data.list_achievements != []:
            # for achievement in m_data.list_achievements:
                achievement = m_data.list_achievements[0]
                achievement.move()
                achievement.blit(self.screen,multiplier_x,multiplier_y)
            if m_data.progression in "pre-game":
                # цикл для відображення всіх кораблів
                for ship in m_data.all_ships:
                    if ship.jump_cor[2]:
                        ship.x += ship.jump_cor[0]
                        ship.y -= ship.jump_cor[1]
                        if not ship.jump_cor[3]:
                            ship.jump_cor[0] /= 1.1
                            ship.jump_cor[1] -= 2.5
                        elif ship.y == 120:
                            ship.jump_cor[3] = False
                            ship.jump_cor[-2] = False
                            
                            m_achievements.achievement('the bug')
                    if ship.y > self.screen.get_size()[1]+1000:
                        ship.y = -100
                        ship.jump_cor[0] =0
                        ship.jump_cor[1] = -20
                        ship.jump_cor[3] = True
                        ship.x = 805
                        # print('hoho')
                    # саме відображення кораблів
                    # print(sprite.x,sprite.y,sprite.width,sprite.height,multiplier_x,multiplier_y,ship.name)
                    # print(sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y,ship.name)
                    ship.blit(self.screen,ship.x*multiplier_x,ship.y*multiplier_y,ship.width*multiplier_x,ship.height*multiplier_y,multiplier_x,multiplier_y)
            start_time,end_time = 0,0
            if m_data.progression == "game":
                count = 0
                list_to_delete = []
                for buff in m_data.my_buffs:
                    # 59, 115
                    # try:
                    
                    if buff[0] == 'Air_Defence':
                        if str(m_data.my_field[buff[1]][buff[2]]) in '05':
                            m_images.air_defence.blit(self.screen,
                                                    (59+buff[2]*55.7)*multiplier_x,
                                                    (115+buff[1]*55.7)*multiplier_y,m_images.air_defence.width*multiplier_x,m_images.air_defence.height*multiplier_y,multiplier_x,multiplier_y
                                                    )
                        else:
                            list_to_delete.append(count)
                    count +=1
                for delete in list_to_delete:
                    del m_data.my_buffs[delete]
                    # except:
                    #     pass
                start_time = pygame.time.get_ticks()

                for sprite in m_data.list_explosions:
                    sprite = sprite[0]
                    sprite.blit(self.screen,
                                sprite.x*multiplier_x,
                                sprite.y*multiplier_y,
                                sprite.width*multiplier_x,
                                sprite.height*multiplier_y,
                                multiplier_x,multiplier_y)
                end_time = pygame.time.get_ticks()
                # print(end_time-start_time,'attack',len(m_data.list_explosions))
                if m_data.time_for_radar:
                    for sprite in m_data.list_for_radar:
                        pygame.draw.circle(self.screen,(50,255,50),((sprite.x+sprite.width/2)*multiplier_x,(sprite.y+sprite.height/2)*multiplier_y),10,25)
            
                if m_data.connected:
                    if m_data.turn:
                        m_buttons.opponent_turn.COLOR = (140, 140, 140)
                        m_buttons.your_turn.COLOR = (0, 0, 255)
                        # sprite = m_buttons.opponent_turn_gray
                        # m_buttons.opponent_turn_gray.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    else:
                        m_buttons.opponent_turn.COLOR = (255, 0, 0)
                        m_buttons.your_turn.COLOR = (140, 140, 140)
                        # sprite = m_buttons.your_turn_gray
                        # m_buttons.your_turn_gray.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    sprite = m_buttons.shop
                    m_buttons.shop.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    sprite = m_buttons.your_turn
                    m_buttons.your_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    sprite = m_buttons.opponent_turn
                    m_buttons.opponent_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                else:
                    wait = m_buttons.wait
                    wait.blit(self.screen,wait.x*multiplier_x,wait.y*multiplier_y,wait.width*multiplier_x,wait.height*multiplier_y,multiplier_x,multiplier_y)
            elif m_data.progression == 'shop':
                square = pygame.Surface((m_buttons.description.rect.width,m_buttons.description.rect.height))
                square.fill((255, 255, 255))
                square.set_alpha(200)
                self.screen.blit(square,m_buttons.description.rect)
                m_buttons.stroke(self.screen,m_buttons.description.rect,(0,0,0),5)
                sprite = m_buttons.description
                m_buttons.description.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
            elif m_data.progression == 'achievements':
                square = pygame.Surface((m_buttons.description_.rect.width,m_buttons.description_.rect.height))
                square.fill((255, 255, 255))
                square.set_alpha(200)
                self.screen.blit(square,m_buttons.description_.rect)
                m_buttons.stroke(self.screen,m_buttons.description_.rect,(0,0,0),5)
                sprite = m_buttons.description_
                m_buttons.description_.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
                x,y =50,50
                for achievement_code in m_data.achievements_data:
                    achievement = m_data.achievements_data[achievement_code]
                    
                    if achievement['has'] == 'True':
                        m_data.list_achievements_view[achievement_code].blit(self.screen,
                                 x*multiplier_x,
                                 y*multiplier_y,
                                 150*multiplier_x,
                                 150*multiplier_y,
                                 multiplier_x,multiplier_y)
                        x += 200
                        if x == 850:
                            x = 50
                            y += 200
            # оновлення екрану 
            m_transform.transform(self,multiplier_x,multiplier_y)
            # фпс
            self.clock.tick(60)
            print(int(self.clock.get_fps()),e-s,len(m_data.list_blits[m_data.progression]),end_time-start_time)
# створення екземпляру классу
screen = Screen()