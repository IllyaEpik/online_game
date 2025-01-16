'''
    >>> Відповідає за атаку кораблей
    >>> Перевіряє чи відбулась атака
    >>> Відповідає за роботу зброї
'''
# імпортуємо необхідні модулі
import pygame,random, time, threading,os
import modules.data as m_data
import modules.images as m_images
import modules.clients_server as m_client
import modules.audio as m_audio
import modules.achievements as m_achievements
import modules.transform as m_transform
import modules.animations as m_animations
# список клітинок без кораблів
list_miss = "05"
# список клітинок з кораблями
list_explosion = "1234"
def attack_for_cell(row,cell):
    name = None
    image = m_images.Image(
            progression = "Noke",
            name = "",
            x = 725+55.7*cell,
            y = 115+55.7*row ,
            width= 55.7,
            height=55.7,
    )
    if str(m_data.enemy_field[row][cell]) in list_explosion:
        m_data.enemy_field[row][cell] = 6
        image = m_animations.Animation(progression = "Noke",
            x = 725+55.7*cell,
            y = 115+55.7*row ,
            width= 55.7,
            name = 'explosion',
            height=55.7)
        name = "explosion"
        if m_data.attack == 'fire_rocket':
            name = 'fire'
            image.name = 'fire'
            m_data.enemy_field[row][cell] = 8
            m_data.attack = None
        # відправляє закодовані данні
        m_data.coins += 10
        image.update_image()
        m_data.list_explosions.append([image, row, cell])
        m_achievements.achievement('It’s a Hit!')
        explosions = []
        for row2 in m_data.enemy_field:
            print(row2,'the best')
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
            # 
            if int(ship.name) == len(cells):
                # 
                for explosion in m_data.list_explosions:
                    #
                    for celll in cells:
                        #
                        if explosion[1] == celll[0] and explosion[2] == celll[1]:
                            #
                            explosions.append(explosion[0])
        
        for ex in explosions:
            try:
                #
                m_data.list_blits['game'].remove(ex)
                
            except:
                # 
                print('reoeroreoreoreooeroeroreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    #
    elif str(m_data.enemy_field[row][cell]) in list_miss:
        #
        m_achievements.achievement('Missed Shot')
        if m_data.attack == 'fire_rocket':
            m_data.attack = None
        m_data.enemy_field[row][cell] = 7
        #
        name = "miss"
        image.name = 'miss'
        image.update_image()
        #
        m_data.turn = False
        m_data.list_explosions.append([image, row, cell])
        #
    return name

def timer_for_radar():
    while m_data.time_for_radar:
        m_data.time_for_radar -= 1
        time.sleep(1)
    if not m_data.turn:
        m_client.send("pass:")
need_to_send = []
# метод з атакою
def attack(pos: tuple,multiplier_x,multiplier_y):
    # створення глобальних змінних
    global list_miss, list_explosion
    # умова для повора кораблів
    
    # blits = True
    text_for_send = ''
    if m_data.turn and m_data.connected:
        
        # цикл для ряду
        if m_data.attack == 'homing_rocket':
            fire()
            list_ships = []
            for ship in m_data.enemy_ships:
                if not ship in m_data.all_ships:
                    list_ships.append(ship)
            
            main_ship = list_ships[random.randint(0,len(list_ships)-1)]
            main_cell = random.randint(0,int(main_ship.name)-1)
            main_row = main_ship.row
            rotate_ship = main_ship.rotate
            if rotate_ship % 180 == 0:
                main_cell += main_ship.cell
                # name = attack_for_cell(main_ship.row,main_cell + main_ship.cell)
                # m_client.send(f"attack:{ main_ship.row},{main_cell + main_ship.cell},{name}".encode())
            else:
                main_row += main_cell
                m_achievements.achievement('Closed Skies')
                main_cell = main_ship.cell
            for buff in m_data.buffs:
                if buff[0] == 'Air_Defence':
                    list_cells = []
                    buff_row = int(buff[1])
                    buff_cell = int(buff[2])
                    for row_air in range(5):
                        for cell_air in range(5):
                            row = buff_row + row_air-2
                            cell = buff_cell + cell_air-2
                            if -1 < row < 10 and -1 < cell < 10:
                                list_cells.append([row,cell])
                    for cell_for_air in list_cells:
                        if main_row == cell_for_air[0] and main_cell == cell_for_air[1]:
                            main_row = buff_row
                            main_cell = buff_cell
                            m_data.buffs.remove(buff)
            # if can_attack:
            name = attack_for_cell(main_row,main_cell)
            text_for_send+=f"attack:{main_row},{main_cell},{name};"
            # if name: 
            m_data.attack = None
            m_data.turn = False
            for buff in m_data.buffs:
                if buff[0] == 'Energetic':
                    m_data.turn = True
            if not m_data.turn:
                text_for_send+= 'pass:;'
            ## 59, 115
            m_audio.explosion.play()
        elif m_data.attack == 'Air_Defence':
            fire()
            for row in range(10):
                # цикл для клітинки
                for cell in range(10):
                    rect = pygame.Rect((59+55.7*cell) * multiplier_x, 
                                    (115+55.7*row) * multiplier_y,
                                    55.7 * multiplier_x,
                                    55.7 * multiplier_y)
                    # перевірка на колізію
                    if rect.collidepoint(pos) and str(m_data.my_field[row][cell]) in '05':
                        m_data.my_buffs.append(['Air_Defence',row,cell])
                        text_for_send+=f'buff:Air_Defence,{row},{cell};'
                        m_data.attack = None
                        m_data.turn = False
                        for buff in m_data.buffs:
                            if buff[0] == 'Energetic':
                                m_data.turn = True
                        if not m_data.turn:
                            text_for_send+='pass:;'
        else:
            for row in range(10):
                # цикл для клітинки
                for cell in range(10):
                    
                    # створюємо хіт-бокс
                    rect = pygame.Rect((725+55.7*cell) * multiplier_x, 
                                    (115+55.7*row) * multiplier_y,
                                    55.7 * multiplier_x,
                                    55.7 * multiplier_y)
                    # перевірка на колізію
                    if rect.collidepoint(pos):
                        # for rows in m_data.enemy_field:
                        #     print(rows)
                        # 6 - explosion 7 - miss
                        # змінна ім'я зі значенням нічого
                        if m_data.attack == 'rocket_3x3':
                            text = 'attack:'
                            for row_3x3 in range(3):
                                for cell_3x3 in range(3):
                                    for count in range(5):
                                        print(row_3x3,cell_3x3,row+row_3x3,cell+cell_3x3)
                                    if -1 < row+row_3x3-1 < 10 and -1 < cell+cell_3x3-1 < 10:
                                        name = attack_for_cell(row+row_3x3-1,cell+cell_3x3-1)
                                        text += f'{row+row_3x3-1},{cell+cell_3x3-1},{name} '
                            text_for_send+= text + ';'
                            m_data.attack = None
                            fire()
                            
                        elif m_data.attack == 'line_rocket':
                            fire()
                            text = 'attack:'
                            for cell in range(10):
                                ship = str(m_data.enemy_field[row][cell])
                                name = attack_for_cell(row,cell)
                                text += f"{row},{cell},{name}"
                                text_for_send+= f"attack:{row},{cell},{name};"
                                if ship in '1234':
                                    break
                                print(m_data.enemy_field[row][cell])
                            text_for_send+= ';' + text + ';'
                            text_for_send+= 'pass:' + ';'
                            m_data.attack = None
                                # elif str(m_data.enemy_field[row][cell]) in '05':
                        elif m_data.attack == 'radar':

                            fire()
                            m_achievements.achievement('used radar')
                            width = 55.7 * multiplier_x
                            height = 55.7 * multiplier_y
                            x = (725+55.7*cell) * multiplier_x
                            y = (115+55.7*row) * multiplier_y
                            start_cell = cell
                            start_row = row
                            end_cell = cell
                            end_row = row
                            if row > 1:
                                width += 55.7 * multiplier_x *2
                                x -= 55.7 * multiplier_x *2
                                start_row -= 2
                            elif row == 1:
                                width += 55.7 * multiplier_x
                                x -= 55.7 * multiplier_x
                                start_row -= 1
                            if row < 8:
                                width += 55.7 * multiplier_x*2
                                end_row += 2
                            elif row == 8:
                                width += 55.7 * multiplier_x
                                end_row += 1
                            if cell < 8:
                                height += 55.7 * multiplier_y*2
                                end_cell += 2
                            elif cell == 8:
                                height += 55.7 * multiplier_y
                                end_cell += 1
                            if cell > 1:
                                start_cell -=2
                                height += 55.7 * multiplier_y*2
                                y -= 55.7 * multiplier_y * 2 
                            elif cell == 1:
                                start_cell -=1
                                height += 55.7 * multiplier_y
                                y -= 55.7 * multiplier_y
                            m_data.rect_for_radar = pygame.Rect(x,y,width,height)
                            m_data.list_for_radar = []
                            print(start_row,start_cell,end_row,end_cell)
                            m_audio.radar.play()
                            for row2 in range(10):
                                for cell2 in range(10):
                                    if row2 >= start_row and row2 <= end_row:
                                        if cell2 >= start_cell and cell2 <= end_cell:
                                            if str(m_data.enemy_field[row2][cell2]) in '1234':
                                                m_data.list_for_radar.append(
                                                    m_images.Image(55.7,
                                                                55.7,
                                                                725+55.7*cell2,
                                                                115+55.7*row2,
                                                                'explosion',
                                                                progression='Noke')
                                                                )
                                                print('hallo')

                            m_data.time_for_radar = 5
                            threading.Thread(target= timer_for_radar,daemon = True).start()
                            m_data.attack = None
                            m_data.turn = False
                            for buff in m_data.buffs:
                                if buff[0] == 'Energetic':
                                    m_data.turn = True
                        
                        else:
                            fire()
                            name = attack_for_cell(row,cell)
                            text = ''
                            
                            if name: 
                                text_for_send+= f"attack:{row},{cell},{name};"
                                #
                                m_audio.explosion.play()
        

        # if text != 'fire:':
        #     text_for_send+= ';'+text
        
        
        win_lose(text_for_send)
def fire():
    global need_to_send
    text = 'fire:'
    for row in range(10):
            if 8 in m_data.my_field[row]:
                for cell in range(10):
                    if m_data.my_field[row][cell] == 8:
                        for row_fire in range(3):
                            for cell_fire in range(3):
                                if -1 < (row_fire + row-1) < 10:
                                    if -1 < (cell_fire + cell-1) < 10:
                                        if str(m_data.my_field[row+row_fire-1][cell+cell_fire-1]) in list_explosion:
                                            # with open(os.path.abspath(__file__+'/../../data/output.txt')) as file:
                                            #     text += file.read()
                                            # for r in m_data.my_field:
                                            #     text += str(r)+'\n'
                                            # with open(os.path.abspath(__file__+'/../../data/output.txt'),'w') as file:
                                            #     file.write(text+'\n'+f"{m_data.my_field[row+row_fire-1][cell+cell_fire-1]},{row+row_fire-1},{cell+cell_fire-1}")
                                            # for count in range(1000):
                                            #     print(m_data.my_field[row+row_fire-1][cell+cell_fire-1],row+row_fire-1,cell+cell_fire-1)
                                            m_data.my_field[row+row_fire-1][cell+cell_fire-1] = 9

                        # m_data.my_field[row][cell] = 6
                        # for explosion in m_data.list_explosions:
                            # if explosion[0].name == 'fire' and explosion[1] == row and explosion[2] == cell:
                            #     explosion[0].name == 'explosion'
                            #     explosion[0].update_image()
    
    for row in range(10):
        if 9 in m_data.my_field[row]:
            for cell in range(10):
                if m_data.my_field[row][cell] == 9:
                    text += f'{row},{cell} '
                    m_data.my_field[row][cell] = 8
                    image = m_animations.Animation(
                            progression = "Noke",
                            name = 'fire',
                            x = 59+55.7*cell,
                            y = 115+55.7*row,
                            # 5 9 4
                            width= 55.7,
                            height=55.7
                        )
                    m_data.list_explosions.append([image,row,cell])
    if text != 'fire:':
        need_to_send.append(';' + text)
    # return text
def win_lose(text_for_send):
    global need_to_send
    yes_no = True

    for ship in m_data.enemy_ships:
        print(ship in m_data.enemy_ships, not ship.explosion)
        if not ship.explosion:
        #     pass
        # elif :
            yes_no = False
    if yes_no and m_data.enemy_ships:
        m_transform.color = (25,255,25)
        m_transform.type_transform = 0
        m_data.progression = "win"
        m_achievements.achievement('Like a Clap of Hands')
        can= True
        for row in m_data.my_field:
            for cell in row:
                if cell == 6 or cell == 8:
                    can = False
                    break 
        if can:
            m_achievements.achievement('Total Domination')
        m_data.read_data['wins']+= 1
        m_data.reading_data(m_data.read_data,'date.txt')
        if m_data.read_data['wins'] > 2:
            m_achievements.achievement('Smells Like Victory')
            if m_data.read_data['wins'] > 49:
                m_achievements.achievement('True Cossack')
                # 0/0 = капибара 
        if m_data.coins == 200:
            m_achievements.achievement('Need More Gold!')
        elif m_data.coins == 190:
            m_achievements.achievement("Big Spender")
        text_for_send += ";lose:?????"
    if text_for_send:
        add = ''
        if not m_data.turn:
            add = ';pass:'
        if need_to_send:
            text_for_send +=';' + ";".join(need_to_send)
            need_to_send = []
        m_client.send(text_for_send + add)