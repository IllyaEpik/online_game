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
import modules.controls as m_controls
threading.Thread(target=m_audio.edit_soundtrack,daemon=True).start()
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
        # завантажуємо іконку гравця
        icon = pygame.image.load(os.path.abspath(__file__ + "/../../images/icon.png"))
        pygame.display.set_icon(icon)
    # функція запуску
    def run(self):
        '''
            >>> Запускає гру
        '''
        # запускаємо гру
        game = True
        # до кількості додаємо 1
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
                # якщо вікно гри зачинено то 
                if event.type == pygame.QUIT:
                    # гра закінчується
                    game = False
                    # гра закінчилася
                    m_data.end=True
                    try:
                        # відключаємо клієнта
                        m_client.client.close()
                    except:
                        pass 
                elif event.type == pygame.MOUSEWHEEL:
                    if m_controls.y_wheel + event.y * 5 < -125:
                        m_controls.y_wheel += event.y * 5
                    print(m_controls.y_wheel)
                # коли кнопка миші наиснута
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    print(event.button)
                    # перехід
                    if m_transform.type_transform == None:
                        # цикл для спрайту в списку ефектів
                        for sprite in m_data.list_blits[m_data.progression]:
                            # print(sprite.name)
                            try:
                                # if sprite.fun != '':
                                # кнопка старт
                                sprite.button_start(event)
                            except:
                                pass
                        if m_controls.off_change_button.rect.collidepoint(event.pos):
                            if m_data.is_change:
                                m_data.is_change = False
                                m_controls.off_change_button.TEXT = 'On Change'
                            else:
                                m_data.is_change = True
                                m_controls.off_change_button.TEXT = 'Off Change'
                            
                        # перевірка виграшу і програшу
                        elif m_data.progression in "winlose":
                            # m_buttons.revenge.button_start(event)
                            # перевірка натискання поза кнопкою старт
                            if m_buttons.out.button_start(event):
                                # гра не починається
                                game = False
                                # гра не почалася
                                m_data.end=True
                                try:
                                    # відключаємо клієнта
                                    m_client.client.close()
                                except:
                                    pass 
                        # перевірка музики
                        elif m_data.progression == 'sounds':
                            t = pygame.time.get_ticks()
                            # натискання мишки
                            m_controls.fun(pygame.mouse.get_pos(),multiplier_x,multiplier_y,[825*multiplier_x, 100*multiplier_y])
                            print(event.pos)
                            # перевірка x
                            if event.pos[0]< 800*multiplier_x:
                                yes = 0
                                # цикл для контролю в списку музики
                                for control in m_controls.list_music:
                                    # print(control[0].rect.collidepoint(event.pos),control[0].rect.x,control[0].rect.y,control[0].rect.width,control[0].rect.height,control[2])
                                    # перевірка обводки контроля
                                    if control[0].rect.collidepoint(event.pos):
                                        control[1] = 1
                                        control[0].COLOR = (50,50,255)
                                        control[0].second_color = (0,0,0)
                                        # зміна треку
                                        m_controls.music_edit('soundtracks',multiplier_x)
                                        # трек змінен
                                        yes = 1
                                    else:
                                        control[1] = 0
                                        control[0].COLOR = (0,0,0)
                                        control[0].second_color = (255,255,255)
                                # якщо трек не змінен
                                if not yes:
                                    # музика не змінюється
                                    m_controls.music_edit(None,multiplier_x)
                            else:

                                # цикл для контролю в списку музики
                                for control in m_controls.list_music:
                                    # print(control[0].rect)
                                    # pygame.Rect()
                                    # перевірка контролю
                                    if control[2]:
                                        # цикл для ключів в списку музики
                                        for key in m_controls.list_musics:
                                            control = key
                                            # print('sos')
                                            control[1].rect.x += 825*multiplier_x
                                            control[1].rect.y += 100*multiplier_y
                                            control[1].button_start(event.pos)
                                            control[1].rect.x -= 825*multiplier_x
                                            control[1].rect.y -= 100*multiplier_y
                                            rect1 = control[0].rect.copy()
                                            rect1.x += 825*multiplier_x
                                            rect1.y += 100*multiplier_y
                                            pygame.draw.rect(self.screen,(124,123,132),rect1)
                                            # print(control[1].rect,event.pos,control[1].name)
                                            # print(rect1)
                                            # перевірка обводки контролю
                                            if rect1.collidepoint(event.pos):
                                                control[2] = 1
                                                control[0].COLOR = (50,50,255)
                                                control[0].second_color = (0,0,0)
                                                stoped = m_audio.track.stoped
                                                # трек зупиняється
                                                m_audio.track.stop()
                                                # зміна треку
                                                m_audio.track = m_audio.Audio('soundtracks/'+key[0].TEXT)
                                                if not stoped:
                                                    # трек грається
                                                    m_audio.track.play()
                                                else:
                                                    rect = m_buttons.music3.rect
                                                    m_buttons.music3.button_start([rect.x + 1, rect.y + 1])
                                                # безпечно відкриваємо файл з музикою
                                                with open(m_data.path+m_data.type+'music.txt', "w") as file:
                                                    # записуємо текст до ключа
                                                    file.write(key[0].TEXT)
                                            else:
                                                control[2] = 0
                                                control[0].COLOR = (0,0,0)
                                                control[0].second_color = (255,255,255)
                                        # зупинка
                                        break
                        # перевірка ключів
                        elif m_data.progression == 'keys':
                            print(event.pos)
                            # перевірка x
                            if event.pos[0]< 800*multiplier_x:
                                yes = 0
                                # цикл для контролю в списку контролю
                                for control in m_controls.list_controls:
                                    # print(control[0].rect.collidepoint(event.pos),control[0].rect.x,control[0].rect.y,control[0].rect.width,control[0].rect.height,control[2])
                                    # перевірка обводки контролю
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
                                    # текст змінюється на None
                                    m_controls.text_edit(None)
                                
                            else:
                                # цикл для контролю в списку контролю
                                for control in m_controls.list_controls:
                                    # перевірка контролю
                                    if control[1]:
                                        # цикл для ключа в списку ключів
                                        for key in m_controls.list_keys:
                                            control = key
                                            # перевірка обводки контроля
                                            if control[0].rect.collidepoint(event.pos):
                                                control[1] = 1
                                                control[0].COLOR = (50,50,255)
                                                control[0].second_color = (0,0,0)
                                            else:
                                                control[1] = 0
                                                control[0].COLOR = (0,0,0)
                                                control[0].second_color = (255,255,255)
                                        # зупинка
                                        break
                        # якщо прогресс дорівнює меню то
                        elif m_data.progression == "menu":
                            # вибір місця написання
                            m_buttons.input.activate(event) 
                            m_buttons.nickname.activate(event)
                        # прогресс дорівнює досягненням то
                        elif m_data.progression == 'achievements':
                            # m_buttons.achievements_.button_start(event)
                            for achievement in m_data.list_achievements_view:
                                m_data.list_achievements_view[achievement].button_start(event)
                        # якщо прогресс дорівнює пре-грі то    
                        elif m_data.progression == "pre-game":
                            # автоматична розтановка кораблів
                            m_buttons.auto.randomship(event.pos)
                            # цикл всіх кораблів
                            for ship in m_data.all_ships:
                                # виділення кораблів
                                ship.activate(event, multiplier_x, multiplier_y)
                        # якщо прогресс дорівнює грі то
                        elif m_data.progression == "game":
                            # якщо підключено
                            # if m_data.connected:
                                # кнопка магазину і старту
                            m_buttons.shop.button_start(event)
                            # вибір місця атаки
                            m_attack.attack(event.pos,multiplier_x,multiplier_y)
                            # m_buttons.shop.button_start(event)
                        # при находженні в магазині
                        elif m_data.progression == 'shop':
                            # цикл для зброї в списку зброї
                            for weapon in m_buttons.list_weapons:
                                weapon.button_start(event=event)
                    # якщо будь-яка клавіша натиснута то
                    else:
                        m_transform.type_transform = None
                        m_transform.size = 0
                # якщо кнопка вгору натиснута
                if event.type == pygame.KEYUP:
                    print(event.key, m_controls.controls['fire attack'])
                    if m_data.progression == 'game' and str(event.key) in m_controls.controls['fire attack']:
                        m_data.fire_attack = False
                        print('NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
                # якщо кнопка вниз натиснута
                if event.type == pygame.KEYDOWN:
                    print(m_controls.controls['rotate ship'],type(m_controls.controls['rotate ship']))
                    # якщо знаходимося в меню
                    if m_data.progression == "menu":
                        # додає символи в event
                        m_buttons.input.edit(event)
                        #редагуємо нікнейм
                        m_buttons.nickname.edit(event)
                        for object in [m_buttons.nickname]:
                            size = object.FONT.size(object.TEXT)
                            # if object.width < size[0] - 10:
                            width = -(object.start_width - size[0] - 10)
                            object.width = width + object.start_width
                            if object.width < object.start_width:
                                object.width = object.start_width
                            object.update_image()
                            # кнопка з музикою
                            m_buttons.music.rect = pygame.Rect(m_buttons.music.x, m_buttons.music.y,m_buttons.music.width,m_buttons.music.height)
                            m_buttons.music.x = m_buttons.nickname.width + 50
                    # при знаходженні в ключах
                    elif m_data.progression == 'keys':
                        # print('yes')
                        # цикл для контролю в списку контролю
                        for control in m_controls.list_controls:
                            if control[1]:
                                # print('yes2')
                                # цикл для ключів в списку ключів
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
                    # при знаходженні в pre-game і ключа в контролі
                    elif m_data.progression == 'pre-game' and str(event.key) in m_controls.controls['rotate ship']:
                        # цикл для корабля в усіх кораблів
                        for ship in m_data.all_ships:
                            # якщо корабль виділен
                            if ship.select:
                                # поворот корабля   
                                ship.rotate_ship()
                    # при знаходженні в грі
                    elif m_data.progression == 'game':
                        # rect = pygame.Rect((725+55.7*cell) * multiplier_x, 
                        #             (115+55.7*row) * multiplier_y,
                        #             55.7 * multiplier_x,
                        #             55.7 * multiplier_y)
                        # перевірка вогняної атаки
                        if str(event.key) in m_controls.controls['fire attack']:
                            m_data.fire_attack = True
                            print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhos')
                        # перевірка рандомної атаки
                        if str(event.key) in m_controls.controls['random attack']:
                            yes = 0
                            # цикл для кораблів на ворожому полі
                            for row in m_data.enemy_field:
                                for cell in row:
                                    # перевірка кораблів в клітинках
                                    if str(cell) in '012345':
                                        yes = True
                                        # зупинка
                                        break
                            if yes:
                                # поки True
                                while True:
                                    # рандомна розстановка в рядах
                                    row = random.randint(0,9)
                                    # рандомна розстановка в клітинках
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
            # запис монет
            m_buttons.coins.TEXT = f"{m_data.coins}"
            # запис монет
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
            # перевірка музики
            if m_data.progression == 'sounds':
                if int(m_controls.surface_sizes[0]*multiplier_x) != m_controls.music_surface.get_width() or int(m_controls.surface_sizes[1]*multiplier_y) != m_controls.music_surface.get_height(): 
                    m_controls.music_surface = pygame.Surface([m_controls.surface_sizes[0]*multiplier_x, m_controls.surface_sizes[1]*multiplier_y])
                    print("The best capybara")
                m_controls.music_surface.fill((100, 100, 100))
                m_controls.music_surface.set_colorkey((100,100,100))
                # цикл для ключів в списку музики
                for key in m_controls.list_musics:
                    sprite = key[0]
                    sprite.blit(m_controls.music_surface,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y + m_controls.y_wheel,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
                    sprite = key[1]
                    sprite.blit(m_controls.music_surface,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y + m_controls.y_wheel,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
                self.screen.blit(m_controls.music_surface,[825*multiplier_x, 130*multiplier_y])
            # перевірка ключів
            if m_data.progression == 'keys':
                # цикл для ключів в списку ключів
                for key in m_controls.list_keys:
                    sprite = key[0]
                    sprite.blit(self.screen,
                                 sprite.x*multiplier_x,
                                 sprite.y*multiplier_y,
                                 sprite.width*multiplier_x,
                                 sprite.height*multiplier_y,
                                 multiplier_x,multiplier_y)
            # зупинка звуку
            if m_audio.track.stoped:
                # якщо знаходимося в меню
                if m_data.progression == "menu":
                    # малюємо лінії 
                    pygame.draw.line(self.screen,(255,50,50),
                                    (m_buttons.music.x*multiplier_x,m_buttons.music.y*multiplier_y,),
                                    (m_buttons.music.x*multiplier_x + m_buttons.music.width*multiplier_x,m_buttons.music.y*multiplier_y + m_buttons.music.height*multiplier_y),10)
                elif 'game' in m_data.progression :
                    pygame.draw.line(self.screen,(255,50,50),
                                    (m_buttons.music2.x*multiplier_x,m_buttons.music2.y*multiplier_y,),
                                    (m_buttons.music2.x*multiplier_x + m_buttons.music2.width*multiplier_x,m_buttons.music2.y*multiplier_y + m_buttons.music2.height*multiplier_y),10)
            # якщо знаходимось не в списку досягнень то
            if m_data.list_achievements != []:
                # список досягнень
                achievement = m_data.list_achievements[0]
                # рух досягнень
                achievement.move()
                achievement.blit(self.screen,multiplier_x,multiplier_y)
            # якщо знаходимося в pre-game
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
                            # нове досягнення
                            m_achievements.achievement('the bug')
                    # перевірка кораблів на екрані
                    if ship.y > self.screen.get_size()[1]+1000:
                        ship.y = -100
                        ship.jump_cor[0] =0
                        ship.jump_cor[1] = -20
                        ship.jump_cor[3] = True
                        ship.x = 805
                        ship.name = '4ticket'
                        ship.update_image()
                        # ship.name = '4'
                    # саме відображення кораблів
                    ship.blit(self.screen,ship.x*multiplier_x,ship.y*multiplier_y,ship.width*multiplier_x,ship.height*multiplier_y,multiplier_x,multiplier_y)
            # якщо знаходимося в грі то
            if m_data.progression == "game":
                # цикл для ракет в списку ракет
                for rocket in m_data.list_rockets:
                    try:
                        # перевіряємо вид ракети
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
                # кількість 0
                count = 0
                # список для видалень
                list_to_delete = []
                # цикл для ефектів в ефектах
                for buff in m_data.my_buffs:
                    # перевірка ефекту протиповітряної оборони
                    if buff[0] == 'Air_Defence':
                        if str(m_data.my_field[buff[1]][buff[2]]) in '05':
                            m_images.air_defence.blit(self.screen,
                                                    (59+buff[2]*55.7)*multiplier_x,
                                                    (115+buff[1]*55.7)*multiplier_y,m_images.air_defence.width*multiplier_x,m_images.air_defence.height*multiplier_y,multiplier_x,multiplier_y
                                                    )
                        else:
                            list_to_delete.append(count)
                    # до кількості додаємо 1
                    count +=1
                # цикл для видалення з списку видалення
                for delete in list_to_delete:
                    del m_data.my_buffs[delete]
                # цикл для спрайту в списку вибуху
                for sprite in m_data.list_explosions:
                    sprite = sprite[0]
                    # відображення спрайту на екрані
                    sprite.blit(self.screen,
                                sprite.x*multiplier_x,
                                sprite.y*multiplier_y,
                                sprite.width*multiplier_x,
                                sprite.height*multiplier_y,
                                multiplier_x,multiplier_y)
                # перевірка часу для радара
                if m_data.time_for_radar:
                    # цикл для спрайту в списку для радара
                    for sprite in m_data.list_for_radar:
                        # малюємо круги
                        pygame.draw.circle(self.screen,(50,255,50),((sprite.x+sprite.width/2)*multiplier_x,(sprite.y+sprite.height/2)*multiplier_y),10,25)
                # якщо підключення відбулося
                if m_data.connected:
                    # якщо черга змінилась
                    if m_data.turn:
                        # зміна кольору
                        m_buttons.opponent_turn.COLOR = (0, 0, 255)
                        # m_buttons.your_turn.COLOR = ()
                    else:
                        # зміна кольору
                        m_buttons.opponent_turn.COLOR = (255, 0, 0)
                        # m_buttons.your_turn.COLOR = (140, 140, 140)
                    # if m_data.turn:
                    #     m_buttons.opponent_turn.COLOR = (140, 140, 140)
                    #     m_buttons.your_turn.COLOR = (0, 0, 255)
                    # else:
                    #     m_buttons.opponent_turn.COLOR = (255, 0, 0)
                    #     m_buttons.your_turn.COLOR = (140, 140, 140)
                    # кнопка магазину
                    sprite = m_buttons.shop
                    # виводимо кнопку на екран
                    m_buttons.shop.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    # sprite = m_buttons.your_turn
                    # m_buttons.your_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                    # кнопка черги опонента
                    sprite = m_buttons.opponent_turn
                    # виводимо кнопку на екран
                    m_buttons.opponent_turn.blit(self.screen,sprite.x*multiplier_x,sprite.y*multiplier_y,sprite.width*multiplier_x,sprite.height*multiplier_y,multiplier_x,multiplier_y)
                else:
                    # кнопка очікування
                    wait = m_buttons.wait
                    # виводимо кнопку на екран
                    wait.blit(self.screen,wait.x*multiplier_x,wait.y*multiplier_y,wait.width*multiplier_x,wait.height*multiplier_y,multiplier_x,multiplier_y)
            #  перевірка досягнень
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
                    # перевірка наявності досягнень
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
            # якщо знаходимося в грі то 
            if m_data.progression == 'game':
                # прибираємо видимість мишки
                pygame.mouse.set_visible(False)
                # задаємо мишці координати появи
                x,y = pygame.mouse.get_pos()
                t= m_images.target
                # відображаємо картинку цілі на екран
                m_images.target.blit(self.screen,
                                     x-50*multiplier_x,
                                     y-50*multiplier_y,
                                     100*multiplier_x,
                                     100*multiplier_y,
                                     multiplier_x,multiplier_y)
            else:
                # задаємо видимість мишки
                pygame.mouse.set_visible(True)
            # якщо знаходимося в звуках то
            if m_data.progression == 'sounds':
                
                # малюємо контрол 
                m_controls.draw(self.screen,multiplier_x,multiplier_y)
            # оновлення екрану 
            m_transform.transform(self,multiplier_x,multiplier_y)
            # фпс
            self.clock.tick(60)

# створення екземпляру классу
screen = Screen()