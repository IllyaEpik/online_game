'''
    >>> Відповідає за атаку кораблей
    >>> Перевіряє чи відбулась атака
    >>> Відповідає за роботу зброї
'''
# імпортуємо необхідні модулі
import pygame,random, time, threading,os
import modules.data as m_data
import modules.images as m_images
import modules.buttons as m_buttons
import modules.clients_server as m_client
import modules.audio as m_audio
import modules.achievements as m_achievements
import modules.transform as m_transform
import modules.animations as m_animations
# список клітинок без кораблів
list_miss = "05"
# список клітинок з кораблями
list_explosion = "1234"
attack_list = '012345'
# функція для атаки кораблів в клітинках
def attack_for_cell(row,cell):
    '''
        >>> Відповідає за вибух кораблів
    '''
    # змінна з назвою
    name = None
    # наслідування класа Image для картинки і задання параметрів для неї
    image = m_images.Image(
            progression = "Noke",
            name = "",
            x = 725+55.7*cell,
            y = 115+55.7*row ,
            width= 55.7,
            height=55.7,
    )
    # для вибуху кораблів на ворожому полі
    yes = False
    if m_data.attack == 'fire_rocket' or m_data.fire_attack and m_data.attack == None and m_data.coins > 1:
        # назва змінюється на вогонь
        m_data.coins -= m_data.cost_data['fire_rocket']
        m_data.list_Bought['fire_rocket'] = True
        yes = True
    if str(m_data.enemy_field[row][cell]) in list_explosion:
        # вибухи кораблів на ворожому полі
        m_data.enemy_field[row][cell] = 6
        # наслідування класа Animation для анімації і задання параметрів для неї
        image = m_animations.Animation(progression = "Noke",
            x = 725+55.7*cell,
            y = 115+55.7*row ,
            width= 55.7,
            name = 'explosion',
            height=55.7)
        # назва змінюється на виьух
        name = "explosion"
        # для атаки з використанням вогненної ракети
        print(m_data.fire_attack, m_data.attack)
        if m_data.attack == 'fire_rocket' or m_data.fire_attack and m_data.attack == None and yes:
            # назва змінюється на вогонь
            # m_data.coins -= m_data.cost_data['fire_rocket']
            name = 'fire'
            # назва картинки змінюється на вогонь
            image.name = 'fire'
            # вибух корабля на ворожому полі
            m_data.enemy_field[row][cell] = 8
            # атака
            m_data.attack = None
        # додає монети за атаку
        m_data.coins += 10
        # оновлює картинки
        image.update_image()
        # додає параметри до списку з вибухами
        m_data.list_explosions.append([image, row, cell])
        # додає досягнення гравцю
        m_achievements.achievement('It’s a Hit!')
        # список для вибухів
        explosions = []
        # цикл для ворожих кораблів
        for ship in m_data.enemy_ships:
            # перевіряє ворожий корабль
            ship.check_enemy()
            # список з клітинками кораблів
            cells = []
            # цикл для додавання всіх клітинок корабля до cells
            for count in range(int(ship.name)):
                # якщо корабель стоїть горизонтально то
                if ship.rotate %180 == 0 and m_data.enemy_field[ship.row][ship.cell+count] != int(ship.name[0]):
                    # додається клітика
                    cells.append([ship.row, ship.cell+count])
                # інакше якщо корабель стоїть вертикалюно то
                elif ship.rotate %180 != 0 and m_data.enemy_field[ship.row+count][ship.cell] != int(ship.name[0]):
                    # додається клітинка
                    cells.append([ship.row+count, ship.cell])
            # назва корабля повинна дорівнювати довжині клітинок
            if int(ship.name) == len(cells):
                # для вибухів в списку вибухів
                for explosion in m_data.list_explosions:
                    # цикл для клітинок
                    for celll in cells:
                        # якщо вибухи дорівнюють клітинкам то
                        if explosion[1] == celll[0] and explosion[2] == celll[1]:
                            # до вибухів додається 0
                            explosions.append(explosion[0])
        # цикл минулих для вибухів
        for ex in explosions:
            try:
                # до списку додається значення 'game' і прибирається минулиц вибух
                m_data.list_blits['game'].remove(ex)
            except:
                pass
    # інакше промах на воожому полі
    elif str(m_data.enemy_field[row][cell]) in list_miss:
        # нове досягнення
        m_achievements.achievement('Missed Shot')
        # для атаки вогненної ракети
        if m_data.attack == 'fire_rocket':
            # атака
            m_data.attack = None
        # промах на ворожому полі
        m_data.enemy_field[row][cell] = 7
        # зміна назви на промах
        name = "miss"
        # зміна назви картинки на промах
        image.name = 'miss'
        # оновлення картинки
        image.update_image()
        # зміна ходу
        m_data.turn = False
        # додає параметри до списку з вибухами
        m_data.list_explosions.append([image, row, cell])
    # повертає назву
    return name
# функція для часу радара
def timer_for_radar():
    '''
        >>> Відповідає за час роботи(таймер) радару
    '''
    # поки радар працює
    while m_data.time_for_radar:
        # від часу віднімається 1 секунда
        m_data.time_for_radar -= 1
        # пауза на 1 секунду
        time.sleep(1)
    # якщо не має ходу
    if not m_data.turn:
        # відправляє пропуск в m_client
        m_client.send("pass:")
# список для відправки всього необхідного
need_to_send = []
# метод з атакою
def attack(pos: tuple,multiplier_x,multiplier_y):
    '''
        >>> Відповідає за атаку кораблів зі зброєю
    '''
    # створення глобальних змінних
    global list_miss, list_explosion
    # blits = True
    # текст для відправки
    text_for_send = ''
    # зміна ходу і підключення
    if m_data.turn and m_data.connected and not m_data.list_rockets:
        # цикл для атаки самонаводящою ракетою
        if m_data.attack == 'homing_rocket':
            m_data.coins -= m_data.cost_data[m_data.attack]
            m_data.list_Bought['homing_rocket'] = True
            # функція з вогнем
            fire()
            # список кораблів
            list_ships = []
            # для кораблів на ворожому полі
            for ship in m_data.enemy_ships:
                # якщо не кораблі в всіх кораблях то
                if not ship in m_data.all_ships:
                    # до списку кораблів додається корабель
                    list_ships.append(ship)
            # головний корабель, його поворот і довжина списку кораблів
            main_ship = list_ships[random.randint(0,len(list_ships)-1)]
            # головна клітинка і віднімання 1 значення від корабля
            main_cell = random.randint(0,int(main_ship.name)-1)
            # головний ряд
            main_row = main_ship.row
            # поворот кораблів
            rotate_ship = main_ship.rotate
            # перевірка розвороту корабля
            if rotate_ship % 180 == 0:
                # головна клітинка додається до головного корабля
                main_cell += main_ship.cell
                # name = attack_for_cell(main_ship.row,main_cell + main_ship.cell)
                # m_client.send(f"attack:{ main_ship.row},{main_cell + main_ship.cell},{name}".encode())
            else:
                # головна клітинка додається до головного корабля
                main_row += main_cell
                # нове досягнення
                # головна клітинка дорівнює головному кораблю
                main_cell = main_ship.cell
            # наявнісь ефектів
            for buff in m_data.buffs:
                # якщо ефект протиповітряної оборони
                if buff[0] == 'Air_Defence':
                    # список клітинок
                    list_cells = []
                    # ефект в ряду
                    buff_row = int(buff[1])
                    # ефект в клітинці
                    buff_cell = int(buff[2])
                    # для ракети в ряд
                    for row_air in range(5):
                        # для ракети по клітинкам
                        for cell_air in range(5):
                            # до ефекту в ряд додається ракета в ряд
                            row = buff_row + row_air-2
                            # до ефекту по клітинкам додається ракета по клітинкам
                            cell = buff_cell + cell_air-2
                            # перевірка значення в ряду і клітинці
                            if -1 < row < 10 and -1 < cell < 10:
                                # до списку клітинок додаються параметри: ряд і клітинка
                                list_cells.append([row,cell])
                    # для клітинок в повітрі в списку клітинок 
                    for cell_for_air in list_cells:
                        # якщо клітинки мають однакові значення
                        if main_row == cell_for_air[0] and main_cell == cell_for_air[1]:
                            # в ряду ефект в ряд
                            main_row = buff_row
                            # в клітинці ефект в клітинку
                            m_achievements.achievement('Closed Skies')
                            main_cell = buff_cell
                            # видалення ефекту
                            m_data.buffs.remove(buff)
            # if can_attack:
            def atta(main_row,main_cell):
                '''
                    >>> Відповідає за хід після атаки
                '''
                # функція атаки для клітинок
                name = attack_for_cell(main_row,main_cell)
                # текст для відправки: атака
                text_for_send = f"attack:{main_row},{main_cell},{name};"
                # if name: 
                # атака
                m_data.attack = None
                # зміна ходу
                m_data.turn = False
                # для ефекту в ефектах
                for buff in m_data.buffs:
                    # якщо ефект енергетик
                    if buff[0] == 'Energetic':
                        # зміна ходу
                        m_data.turn = True
                # якщо не має ходу
                if not m_data.turn:
                    # текст для відправки: пропуск
                    text_for_send+= 'pass:'
                win_lose(text_for_send) 
                # звук вибуху
                m_audio.explosion.play()
            # додає картинку до списку ракет
            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*main_row,f'weapons/homing_rocket','Noke',0),main_row,main_cell,lambda:atta(main_row,main_cell),0))
            try:
                # запускає анімації
                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
            except:
                pass
            ## 59, 115
            # звук вибуху
        # атака протиповітряної оборони
        elif m_data.attack == 'Air_Defence':
            # функція вогню
            fire()
            # цикл для ряду
            for row in range(10):
                # цикл для клітинки
                for cell in range(10):
                    # створюємо хіт-бокс
                    rect = pygame.Rect((59+55.7*cell) * multiplier_x, 
                                    (115+55.7*row) * multiplier_y,
                                    55.7 * multiplier_x,
                                    55.7 * multiplier_y)
                    # перевірка на колізію
                    if rect.collidepoint(pos) and str(m_data.my_field[row][cell]) in '05':
                        m_data.coins -= m_data.cost_data[m_data.attack]
                        m_data.list_Bought['Air_Defence'] = True
                        # до моїх ефектів додається протиповітряна оборона
                        m_data.my_buffs.append(['Air_Defence',row,cell])
                        # текст для відправки: ефект протиповітряної оборони
                        text_for_send+=f'buff:Air_Defence,{row},{cell};'
                        # атака
                        m_data.attack = None
                        # зміна ходу
                        m_data.turn = False
                        # цикл для ефекту в ефектах
                        for buff in m_data.buffs:
                            # якщо ефект енергетик
                            if buff[0] == 'Energetic':
                                # зміна ходу
                                m_data.turn = True
                        # якщо не має ходу
                        if not m_data.turn:
                            # текст для відправки: пропуск
                            text_for_send+='pass:;'
        else:
            # цикл для ряду
            for row in range(10):
                # цикл для клітинки
                for cell in range(10):
                    # наслідуємо клас Rect і створюємо хіт-бокс
                    rect = pygame.Rect((725+55.7*cell) * multiplier_x, 
                                    (115+55.7*row) * multiplier_y,
                                    55.7 * multiplier_x,
                                    55.7 * multiplier_y)
                    # перевірка на колізію
                    # малюємо обводку
                    if rect.collidepoint(pos) and str(m_data.enemy_field[row][cell]) in attack_list:
                        # якщо атака ракетою 3x3
                        if m_data.attack == 'rocket_3x3':
                            m_data.coins -= m_data.cost_data[m_data.attack]
                            m_data.list_Bought['rocket_3x3'] = True
                            # текст: атака
                            def atta(row,cell):
                                '''
                                    >>> Відповідає за атаку ракетою 3x3
                                '''
                                text = 'attack:'
                                # цикл для ракети 3х3
                                for row_3x3 in range(3):
                                    # цикл для ракети 3х3
                                    for cell_3x3 in range(3):
                                        # перевірка ракети в клітинках 3х3
                                        if -1 < row+row_3x3-1 < 10 and -1 < cell+cell_3x3-1 < 10:
                                            # атака для клітинок
                                            name = attack_for_cell(row+row_3x3-1,cell+cell_3x3-1)
                                            # текст для ракети 3х3 в ряду і клітинці
                                            text += f'{row+row_3x3-1},{cell+cell_3x3-1},{name},1 '
                                # до тексту додаємо символ ";"
                                # атака
                                m_data.attack = None
                                # функція вогню
                                fire()
                                m_audio.explosion.play(1)
                                win_lose(text + ';')
                            # змінна для тимчасового збереження рядка   
                            ok,ok1 = row,cell 
                            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*row,f'weapons/rocket_3x3','Noke',0),ok,ok1,lambda:atta(ok,ok1),0))
                            try:
                                # запускаємо анімації
                                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
                            except:
                                pass
                        # атака дінійною ракетою  
                        elif m_data.attack == 'line_rocket':
                            m_data.coins -= m_data.cost_data[m_data.attack]
                            m_data.list_Bought['line_rocket'] = True
                            fire()
                            # функція для атаки
                            def atta(row,cell,last = 0):
                                '''
                                    >>> Відповідає за атаку в клітинках
                                '''
                                # функція вогню
                                # даємо назву - атака для клітинок
                                name = attack_for_cell(row,cell)
                                # змінна текст
                                text = ''
                                # якщо назва - атака для клітинок
                                if name: 
                                    # виграш або програш 
                                    # win_lose(f"attack:{row},{cell},{name}")
                                    if last:
                                        win_lose(m_data.list_rockets[-1][-1]+f"{row},{cell},{name}")
                                        # звук вибуху
                                        m_audio.explosion.play() 
                                    else:
                                        # m_data.list_rockets[-1][-1]+=f"{row},{cell},{name} "
                                        win_lose(f"attack:{row},{cell},{name},0")
                                
                            # змінна для тимчасового збереження рядка   
                            ok = row
                            # до списку ракет додаємо параметри
                            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*row,f'weapons/line_rocket','Noke',0),ok,atta,'pass;attack:'))
                            try:
                                # запуск списку ракет, їх анімація
                                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
                            except:
                                pass
                                # elif str(m_data.enemy_field[row][cell]) in '05':
                        # атака радаром
                        elif m_data.attack == 'radar':
                            m_data.list_Bought['radar'] = True
                            m_data.coins -= m_data.cost_data[m_data.attack]
                            # функція вогню
                            fire()
                            # змінюємо ширину
                            width = 55.7 * multiplier_x
                            # змінюємо висоту
                            height = 55.7 * multiplier_y
                            # змінюємо розташування по x
                            x = (725+55.7*cell) * multiplier_x
                            # змінюємо розташування по y
                            y = (115+55.7*row) * multiplier_y
                            # задаємо початок клітинок
                            start_cell = cell
                            # задаємо початок рядів
                            start_row = row
                            # задаємо кінець клітинок
                            end_cell = cell
                            # задаємо кінець рядів
                            end_row = row
                            # перевіряємо розташування рядів
                            if row > 1:
                                # змінюємо параметри ширини, x і початку ряду
                                width += 55.7 * multiplier_x *2
                                x -= 55.7 * multiplier_x *2
                                start_row -= 2
                            # перевіряємо розташування рядів
                            elif row == 1:
                                # змінюємо параметри ширини, x і початку ряду
                                width += 55.7 * multiplier_x
                                x -= 55.7 * multiplier_x
                                start_row -= 1
                            # перевіряємо розташування рядів
                            if row < 8:
                                # змінюємо параметри ширини і кінця ряду
                                width += 55.7 * multiplier_x*2
                                end_row += 2
                            # перевіряємо розташування рядів
                            elif row == 8:
                                # змінюємо параметри ширини і кінця ряду
                                width += 55.7 * multiplier_x
                                end_row += 1
                            # перевіряємо розташування клітинок
                            if cell < 8:
                                # змінюємо параметри висоти і кінця клітинок
                                height += 55.7 * multiplier_y*2
                                end_cell += 2
                            # перевіряємо розташування клітинок
                            elif cell == 8:
                                # змінюємо параметри висоти і кінця клітинок
                                height += 55.7 * multiplier_y
                                end_cell += 1
                            # перевіряємо розташування клітинок
                            if cell > 1:
                                # змінюємо параметри висоти, y і початку клітинок
                                start_cell -=2
                                height += 55.7 * multiplier_y*2
                                y -= 55.7 * multiplier_y * 2 
                            # перевіряємо розташування клітинок
                            elif cell == 1:
                                # змінюємо параметри висоти, y і початку клітинок
                                start_cell -=1
                                height += 55.7 * multiplier_y
                                y -= 55.7 * multiplier_y
                            # поле для радару
                            m_data.rect_for_radar = pygame.Rect(x,y,width,height)
                            # список для радару
                            m_data.list_for_radar = []
                            # звук радару
                            m_audio.radar.play()
                            # цикл для ряду
                            for row2 in range(10):
                                # цикл для клітинки
                                for cell2 in range(10):
                                    # перевірка першого і останнього ряда
                                    if row2 >= start_row and row2 <= end_row:
                                        # перевірка першої клітинки і останньої
                                        if cell2 >= start_cell and cell2 <= end_cell:
                                            # перевірка розташування кораблів на ворожому полі
                                            if str(m_data.enemy_field[row2][cell2]) in '1234':
                                                # додаємо до списку з радаром:
                                                m_data.list_for_radar.append(
                                                    # наслідуємо клас Image і задаємо параметри
                                                    m_images.Image(55.7,
                                                                55.7,
                                                                725+55.7*cell2,
                                                                115+55.7*row2,
                                                                'explosion',
                                                                progression='Noke')
                                                                )
                            # ставимо час для роботи радару 5 секунд
                            m_data.time_for_radar = 5
                            # запускаємо час дії радару
                            threading.Thread(target= timer_for_radar,daemon = True).start()
                            # атакуємо
                            m_data.attack = None
                            # змінюємо ход
                            m_data.turn = False
                            # для ефекту в ефектах
                            for buff in m_data.buffs:
                                # якщо ефект - енергетик
                                if buff[0] == 'Energetic':
                                    # дозволяємо ходити
                                    m_data.turn = True
                        
                        else:
                            # функція для атаки
                            def atta(row,cell):
                                '''
                                    >>> Відповідає за атаку по клітинкам
                                '''
                                # функція вогню
                                fire()
                                # даємо назву - атака для клітинок
                                name = attack_for_cell(row,cell)
                                # змінна текст
                                text = ''
                                # якщо назва - атака для клітинок
                                if name: 
                                    # виграш або програш                                  
                                    win_lose(f"attack:{row},{cell},{name}")
                                    # звук вибуху
                                    m_audio.explosion.play()
                            # змінна для тимчасового збереження рядка   
                            ok,ok1 = row,cell
                            # створення назви для звичайної ракети
                            name_for_rocket = 'standart_rocket'
                            # якщо атака вогняною ракетою, то
                            if m_data.attack == 'fire_rocket' or (m_data.fire_attack and not m_data.attack):
                                # назва ракети змінюється на вогняну ракету
                                name_for_rocket = 'fire_rocket'
                            # до списку ракет додаємо параметри
                            m_data.list_rockets.append((m_images.Image(55.7*2,55.7*0.5,-120,115+55.7*row,f'weapons/{name_for_rocket}','Noke',0),ok,ok1,lambda:atta(ok,ok1),0))
                            try:
                                # запуск списку ракет, їх анімація
                                threading.Thread(target=lambda:m_animations.move(m_data.list_rockets[-1][0])).start()
                            except:
                                pass

        # if text != 'fire:':
        #     text_for_send+= ';'+text
        
        # функція для перемоги і програшу
        get = True
        print(m_data.list_Bought)
        for product in m_data.list_Bought:
            if not m_data.list_Bought[product]:
                get = False
        if get:
            m_achievements.achievement('Shopaholic')
        win_lose(text_for_send)
# функція для вогню
def fire():
    '''
        >>> Відповідає за горіння кораблів
    '''
    # робимо змінну необхідної для відправки глобальною
    global need_to_send
    # текст для вогню
    text = 'fire:'
    # цикл для перевірки рядів
    for row in range(10):
            # перевіряємо ряди на полі
            if 8 in m_data.my_field[row]:
                # цикл для перевірки клітинок
                for cell in range(10):
                    #  перевіряємо кількість ряди на полі
                    if m_data.my_field[row][cell] == 8:
                        # цикл для вогню в ряд
                        for row_fire in range(3):
                            # цикл для вогню в клітинках
                            for cell_fire in range(3):
                                # перевіряємо ряди і вогонь в рядах
                                if -1 < (row_fire + row-1) < 10:
                                    # перевіряємо клітинки і вогонь в клітинках 
                                    if -1 < (cell_fire + cell-1) < 10:
                                        # перевіряємо вибухи на полі в списку вибухів
                                        if str(m_data.my_field[row+row_fire-1][cell+cell_fire-1]) in list_explosion:
                                            # 9 рядів і клітинок на полі
                                            m_data.my_field[row+row_fire-1][cell+cell_fire-1] = 9
    # цикл для рядів
    for row in range(10):
        # якщо на полі є 9 рядів
        if 9 in m_data.my_field[row]:
            # цикл для клітинок
            for cell in range(10):
                # якщо на полі 9 рядів і клітинок
                if m_data.my_field[row][cell] == 9:
                    # до тексту записується ряд і клітинка
                    text += f'{row},{cell} '
                    # 8 рядів і клітинок на полі
                    m_data.my_field[row][cell] = 8
                    # наслідування класу Animation для картинки анімацій і задаємо параметри
                    image = m_animations.Animation(
                            progression = "Noke",
                            name = 'fire',
                            x = 59+55.7*cell,
                            y = 115+55.7*row,
                            # 5 9 4
                            width= 55.7,
                            height=55.7
                        )
                    # до списку вибухів додаємо картинку, ряд і клітинку
                    m_data.list_explosions.append([image,row,cell])
    # якщо текст не дорвнює вогню
    if text != 'fire:':
        # додаємо символ ';' до змінної необхідного для відправки
        need_to_send.append(';' + text)
    # return text
# функція для виграшу та поразки
def win_lose(text_for_send):
    '''
        >>> Відповідає за виграш та програш
    '''
    # робимо змінну необхідної для відправки глобальною
    global need_to_send
    # змінна да_ні
    yes_no = True
    # цикл для корабля в ворожих кораблях
    for ship in m_data.enemy_ships:
        # якщо немає вибуху корабля
        if not ship.explosion:
        # elif :
            # змінна да_ні змінюється на False
            yes_no = False
    # перевірка да_ні і ворожих кораблів
    if yes_no and m_data.enemy_ships:
        # зміна кольору
        m_transform.color = (25,255,25)
        # зміна типу переходу
        m_transform.type_transform = 0
        # перехід на вікно перемоги
        m_data.progression = "win"
        # нове досягнення
        m_achievements.achievement('Like a Clap of Hands')
        # змінна може
        can= True
        # цикл для рядів на полі
        for row in m_data.my_field:
            # цикл для клітинок в ряду
            for cell in row:
                # перевірка клітинок
                if cell == 6 or cell == 8:
                    # не може
                    can = False
                    # зупинка
                    break 
        # умова для досягнення
        if can:
            # нове досягнення
            m_achievements.achievement('Total Domination')
        # додається перемога
        m_data.read_data['wins'] = 1 + int(m_data.read_data['wins'])
        with open(m_data.path+m_data.type+'data.txt', "w") as file:
            # записуємо нікнейм, ip, звук і клієнт_сервер
            file.write(f"{m_buttons.nickname.TEXT}\n{m_data.ip}\n{not m_audio.track.stoped}\n{m_data.client_server}\n{m_data.read_data['wins']}\n{m_data.read_data['loses']}")
        # записується в дату
        m_data.reading_data(m_data.read_data,'date.txt')
        # якщо більше ніж 2 перемоги, то
        if m_data.read_data['wins'] > 2:
            # нове досягнення
            m_achievements.achievement('Smells Like Victory')
        # перевірка наявних монет 
        if m_data.coins == 200:
            # нове досягнення
            m_achievements.achievement('Need More Gold!')
        # перевіряє кількість монет
        elif m_data.coins == 10:
            # нове досягнення
            m_achievements.achievement("Big Spender")
        # до тексту для відправки додається програш
        text_for_send += ";lose:?????"
    # перевірка тексту для відправки
    if text_for_send:
        # змінна додати
        add = ''
        # якщо хід не змінюється
        if not m_data.turn:
            # пропуск ходу
            add = ';pass:'
        # перевірка необхідного для відправки
        if need_to_send:
            # до тексту додаємо символ ';'
            text_for_send +=';' + ";".join(need_to_send)
            # список для необхідного для відправки
            need_to_send = []
        # відправляємо все в клієнта
        m_client.send(text_for_send + add)