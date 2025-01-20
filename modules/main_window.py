'''
    >>> Створює головне вікно - класс Screen
'''
# імпортуємо модуль pygame
import pygame, threading, os,random
# ініціалізуємо pygame
pygame.init()
# імпортуємо наші модулі 
import modules.data as m_data
import modules.controls as m_controls
import modules.buttons as m_buttons
import modules.images as m_images
import modules.clients_server as m_client
import modules.ships as m_ships
import modules.attack as m_attack
import modules.transform as m_transform
import modules.audio as m_audio
import modules.achievements as m_achievements
import modules.animations as m_animations
threading.Thread(target=m_animations.play_animation,daemon=True).start()
# клас для налаштування головного вікна
class Screen():
    '''
        >>> Налаштовує головне вікно
    '''
    # ініціалізуємо screen
    def __init__(self):
        size = pygame.display.Info()
        # створюємо таймер
        self.clock = pygame.time.Clock()
        # вказуємо ширину
        self.WIDTH= size.current_w * 0.75
        # вказуємо висоту
        self.HEIGHT = size.current_h * 0.75
        # створюємо екран
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT),pygame.RESIZABLE)
        self.counter = 0

        # задаємо назву нашому екрану
        pygame.display.set_caption('online game')
        
        icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon.png"))
        pygame.display.set_icon(icon)
    # функція запуску
    def run(self):
        '''
            >>> Запускає гру
        '''
        # m_data.progression = 'lose'
        # запускаємо гру
        game = True
        self.counter += 1
        
        # налаштування розміра дісплея
        size = pygame.display.Info()
        # поки гра триває
        while game:
            size1 = self.screen.get_size()
            WIDTH = size1[0]
            HEIGHT= size1[1]
            multiplier_x = (WIDTH / 100) / (1280 / 100)
            multiplier_y = (HEIGHT / 100) / (832 / 100)
            # цикл всіх подій
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
                        for sprite in m_data.list_blits[m_data.progression]:
                            # print(sprite.name)
                            try:
                                # if sprite.fun != '':
                                sprite.button_start(event)
                            except:
                                pass
                        if m_data.progression in "winlose":
                            # m_buttons.revenge.button_start(event)
                            if m_buttons.out.button_start(event):
                                game = False
                                m_data.end=True
                                try:
                                    # відключаємо клієнта
                                    m_client.client.close()
                                except:
                                    pass 
                        if m_data.progression == 'sounds':
                            print(event.pos)
                            if event.pos[0]< 800*multiplier_x:
                                yes = 0
                                for control in m_controls.list_music:
                                    # print(control[0].rect.collidepoint(event.pos),control[0].rect.x,control[0].rect.y,control[0].rect.width,control[0].rect.height,control[2])
                                    if control[0].rect.collidepoint(event.pos):
                                        control[1] = 1
                                        control[0].COLOR = (50,50,255)
                                        control[0].second_color = (0,0,0)
                                        m_controls.music_edit('soundtracks')
                                        yes = 1
                                    else:
                                        control[1] = 0
                                        control[0].COLOR = (0,0,0)
                                        control[0].second_color = (255,255,255)
                                if not yes:
                                    m_controls.music_edit(None)
                                
                            else:
                                for control in m_controls.list_music:
                                    if control[1]:
                                        for key in m_controls.list_musics:
                                            control = key
                                            if control[0].rect.collidepoint(event.pos):
                                                control[1] = 1
                                                control[0].COLOR = (50,50,255)
                                                control[0].second_color = (0,0,0)
                                                m_audio.track.stop()
                                                m_audio.track = m_audio.Audio('soundtracks/'+key[0].TEXT)
                                                m_audio.track.play()
                                                with open(m_data.path+m_data.type+'music.txt', "w") as file:
                                                    file.write(key[0].TEXT)
                                            else:
                                                control[1] = 0
                                                control[0].COLOR = (0,0,0)
                                                control[0].second_color = (255,255,255)
                                        break
                        if m_data.progression == 'keys':
                            print(event.pos)
                            if event.pos[0]< 800*multiplier_x:
                                yes = 0
                                for control in m_controls.list_controls:
                                    # print(control[0].rect.collidepoint(event.pos),control[0].rect.x,control[0].rect.y,control[0].rect.width,control[0].rect.height,control[2])
                                    if control[0].rect.collidepoint(event.pos):
                                        control[1] = 1
                                        control[0].COLOR = (50,50,255)
                                        control[0].second_color = (0,0,0)
                                        m_controls.text_edit(control[2])
                                        yes = 1
                                    else:
                                        control[1] = 0
                                        control[0].COLOR = (0,0,0)
                                        control[0].second_color = (255,255,255)
                                if not yes:
                                    m_controls.text_edit(None)
                                
                            else:
                                for control in m_controls.list_controls:
                                    if control[1]:
                                        for key in m_controls.list_keys:
                                            control = key
                                            if control[0].rect.collidepoint(event.pos):
                                                control[1] = 1
                                                control[0].COLOR = (50,50,255)
                                                control[0].second_color = (0,0,0)
                                            else:
                                                control[1] = 0
                                                control[0].COLOR = (0,0,0)
                                                control[0].second_color = (255,255,255)
                                        break
                        # якщо прогресс дорівнює меню то
                        if m_data.progression == "menu":
                            # вибір місця написання
                            m_buttons.input.activate(event) 
                            m_buttons.nickname.activate(event)
                        # якщо прогресс дорівнює пре-грі то
                        elif m_data.progression == 'achievements':
                            # m_buttons.achievements_.button_start(event)
                            for achievement in m_data.list_achievements_view:
                                m_data.list_achievements_view[achievement].button_start(event)
                        if m_data.progression == "pre-game":
                            # m_buttons.music2.button_start(event)
                            # # преходить в гру
                            # m_buttons.play.button_start(event)
                            # автоматична розтановка кораблів
                            m_buttons.auto.randomship(event.pos)
                            # поворот кораблів
                            # m_buttons.rotate.button_start(event)

                            # цикл всіх кораблів
                            for ship in m_data.all_ships:
                                # виділення кораблів
                                ship.activate(event, multiplier_x, multiplier_y)
                        # якщо прогресс дорівнює грі то
                        if m_data.progression == "game":
                            if m_data.connected:
                                m_buttons.shop.button_start(event)
                            # m_buttons.music2.button_start(event)
                            # вибір місця атаки
                            m_attack.attack(event.pos,multiplier_x,multiplier_y)
                            # m_buttons.shop.button_start(event)
                            
                        elif m_data.progression == 'shop':
                            # m_buttons.shop_.button_start(event)
                            # m_buttons.buy.button_start(event)
                            
                            for weapon in m_buttons.list_weapons:
                                weapon.button_start(event=event)
                    # якщо будь-яка клавіша натиснута то
                    else:
                        m_transform.type_transform = None
                        m_transform.size = 0
                if event.type == pygame.KEYUP:
                    print(event.key, m_controls.controls['fire attack'])
                    if m_data.progression == 'game' and str(event.key) in m_controls.controls['fire attack']:
                        m_data.fire_attack = False
                        print('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
                if event.type == pygame.KEYDOWN:
                    print(m_controls.controls['rotate ship'],type(m_controls.controls['rotate ship']))
                    
                    if m_data.progression == "menu":
                        # додає символи в event
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
                    elif m_data.progression == 'keys':
                        # print('yes')
                        for control in m_controls.list_controls:
                            if control[1]:
                                # print('yes2')
                                for key in m_controls.list_keys:
                                    if key[1]:
                                        # print('yes3')
                                        m_controls.controls[control[2]][key[2]] = event.key
                                        # print('yes4',event.key)
                                        m_controls.text_edit(control[2])
                                        l_controls = ''
                                        controls = m_controls.controls
                                        for control in controls:
                                            l_controls += f'{controls[control][0]},{controls[control][1]},{controls[control][2]},{controls[control][3]}\n'
                                        with open(m_data.path+m_data.type+'controls'+'.txt', "w") as file:
                                            file.write(l_controls)
                    elif m_data.progression == 'pre-game' and str(event.key) in m_controls.controls['rotate ship']:
                        for ship in m_data.all_ships:
                            # якщо корабль виділен
                            if ship.select:
                                # поворот корабля   
                                ship.rotate_ship()
                    elif m_data.progression == 'game':
                        # rect = pygame.Rect((725+55.7*cell) * multiplier_x, 
                        #             (115+55.7*row) * multiplier_y,
                        #             55.7 * multiplier_x,
                        #             55.7 * multiplier_y)
                        if str(event.key) in m_controls.controls['fire attack']:
                            m_data.fire_attack = True
                            print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhos')
                        if str(event.key) in m_controls.controls['random attack']:
                            yes = 0
                            for row in m_data.enemy_field:
                                for cell in row:
                                    if str(cell) in '012345':
                                        yes = True
                                        break
                            if yes:
                                while True:
                                    row = random.randint(0,9)
                                    cell = random.randint(0,9)
                                    if str(m_data.enemy_field[row][cell]) in '012345':
                                        print(row,cell,m_data.enemy_field[row][cell])
                                        m_attack.attack([(726+55.7*cell)*multiplier_x,(115+55.7*row)*multiplier_y],multiplier_x,multiplier_y)
                                        break

            # if m_data.progression == 'game':
            #     m_data.fire_attack = False
            #     for key in pygame.key.get_pressed():
                    
            #         if key in m_controls.controls['fire attack']:
            #             m_data.fire_attack = True
            m_buttons.coins.TEXT = f"{m_data.coins}"
            m_buttons.coins_.TEXT = f"{m_data.coins}"

            # цикл відображення всього що є в списку
            for sprite in m_data.list_blits[m_data.progression]:
                # відображення елементу
                sprite.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
            if m_data.progression == 'sounds':
                for key in m_controls.list_musics:
                    sprite = key[0]

                    sprite.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
            if m_data.progression == 'keys':
                
                for key in m_controls.list_keys:
                    sprite = key[0]

                    sprite.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
            if m_audio.track.stoped:
                if m_data.progression == "menu":
                    pygame.draw.line(self.screen,(255,50,50),
                                    (m_buttons.music.x*multiplier_x,m_buttons.music.y*multiplier_y,),
                                    (m_buttons.music.x*multiplier_x + m_buttons.music.width*multiplier_x,m_buttons.music.y*multiplier_y + m_buttons.music.height*multiplier_y),10)
                elif 'game' in m_data.progression :
                    pygame.draw.line(self.screen,(255,50,50),
                                    (m_buttons.music2.x*multiplier_x,m_buttons.music2.y*multiplier_y,),
                                    (m_buttons.music2.x*multiplier_x + m_buttons.music2.width*multiplier_x,m_buttons.music2.y*multiplier_y + m_buttons.music2.height*multiplier_y),10)
            # якщо знаходимось не в меню то
            if m_data.list_achievements != []:
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
                        ship.name = '4ticket'
                        # ship.update_image()
                        # ship.name = '4'
                    # саме відображення кораблів
                    ship.blit(self.screen,ship.x*multiplier_x,ship.y*multiplier_y,ship.width*multiplier_x,ship.height*multiplier_y,multiplier_x,multiplier_y)
            if m_data.progression == "game":
                for rocket in m_data.list_rockets:
                    try:
                        if rocket[0].name != 'weapons/line_rocket':
                            x = (725+55.7*rocket[2]) * multiplier_x
                            sprite = rocket[0]
                            sprite.blit(self.screen,
                                        sprite.x*multiplier_x,
                                        sprite.y*multiplier_y,
                                        sprite.width*multiplier_x,
                                        sprite.height*multiplier_y,
                                        multiplier_x,multiplier_y)
                            if rocket[0].x*multiplier_x + rocket[0].width*multiplier_x > x:
                                rocket[3]()
                                m_data.list_rockets.remove(rocket)
                        else:
                            
                            sprite = rocket[0]
                            sprite.blit(self.screen,
                                        sprite.x*multiplier_x,
                                        sprite.y*multiplier_y,
                                        sprite.width*multiplier_x,
                                        sprite.height*multiplier_y,
                                        multiplier_x,multiplier_y)
                            for count in range(10):
                                x = (725+55.7*count) * multiplier_x
                                if rocket[0].x*multiplier_x + rocket[0].width*multiplier_x > x:
                                    last = 0
                                    if str(m_data.enemy_field[rocket[1]][count]) in '1234' or count == 9:
                                        last = 1
                                    rocket[2](rocket[1],count,last)
                                    if last:
                                        m_data.list_rockets.remove(rocket)
                                        m_data.attack = None
                                        break
                    except Exception as error:
                        pass

                count = 0
                list_to_delete = []
                for buff in m_data.my_buffs:
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

                for sprite in m_data.list_explosions:
                    sprite = sprite[0]
                    sprite.blit(self.screen,
                                sprite.x*multiplier_x,
                                sprite.y*multiplier_y,
                                sprite.width*multiplier_x,
                                sprite.height*multiplier_y,
                                multiplier_x,multiplier_y)
                if m_data.time_for_radar:
                    for sprite in m_data.list_for_radar:
                        pygame.draw.circle(self.screen,(50,255,50),((sprite.x+sprite.width/2)*multiplier_x,(sprite.y+sprite.height/2)*multiplier_y),10,25)
            
                if m_data.connected:
                    if m_data.turn:
                        m_buttons.opponent_turn.COLOR = (0, 0, 255)
                        # m_buttons.your_turn.COLOR = ()
                    else:
                        m_buttons.opponent_turn.COLOR = (255, 0, 0)
                        # m_buttons.your_turn.COLOR = (140, 140, 140)
                    # if m_data.turn:
                    #     m_buttons.opponent_turn.COLOR = (140, 140, 140)
                    #     m_buttons.your_turn.COLOR = (0, 0, 255)
                    # else:
                    #     m_buttons.opponent_turn.COLOR = (255, 0, 0)
                    #     m_buttons.your_turn.COLOR = (140, 140, 140)
                    sprite = m_buttons.shop
                    m_buttons.shop.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    # sprite = m_buttons.your_turn
                    # m_buttons.your_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    sprite = m_buttons.opponent_turn
                    m_buttons.opponent_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                else:
                    wait = m_buttons.wait
                    wait.blit(self.screen,wait.x*multiplier_x,wait.y*multiplier_y,wait.width*multiplier_x,wait.height*multiplier_y,multiplier_x,multiplier_y)

            elif m_data.progression == 'achievements':
                square = pygame.Surface((m_buttons.description_.rect.width,m_buttons.description_.rect.height))
                square.fill((0,0,0))
                square.set_alpha(100)
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
            pygame.mouse.set_visible(False)
            x,y = pygame.mouse.get_pos()
            m_images.target.blit(self.screen,x-25*multiplier_x,y-25*multiplier_y,50*multiplier_x,50*multiplier_y,multiplier_x,multiplier_y)
            # оновлення екрану 
            m_transform.transform(self,multiplier_x,multiplier_y)
            # фпс
            self.clock.tick(60)
# створення екземпляру классу
screen = Screen()