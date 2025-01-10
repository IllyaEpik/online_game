# імпортуємо необхідні модулі
import pygame,random, time, threading
import modules.data as m_data
import modules.images as m_images
import modules.clients_server as m_client
import modules.audio as m_audio
import modules.achievements as m_achievements
import modules.transform as m_transform
# список клітинок без кораблів
list_miss = "05"
# список клітинок з кораблями
list_explosion = "1234"
def attack_for_cell(row,cell):
    name = None
    image = m_images.Image(
            progression = "game",
            name = "",
            x = 725+55.7*cell,
            y = 115+55.7*row ,
            width= 55.7,
            height=55.7
    )
    if str(m_data.enemy_field[row][cell]) in list_explosion:
        m_data.enemy_field[row][cell] = 6
        # відправляє закодовані данні
        image.name = 'explosion'
        m_data.coins += 10
        image.update_image()
        m_data.list_explosions.append([image, row, cell])
        m_achievements.achievement('It’s a Hit!')
        name = "explosion"
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
                # blits = False
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
                # del m_data.list_blits['game'][ex]
                m_data.list_blits['game'].remove(ex)
                
            except:
                print('reoeroreoreoreooeroeroreeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
                # pass
    #
    elif str(m_data.enemy_field[row][cell]) in list_miss:
        #
        m_data.enemy_field[row][cell] = 7
        #
        name = "miss"
        image.name = 'miss'
        image.update_image()
        #
        m_data.turn = False
        #
    return name

def timer_for_radar():
    while m_data.time_for_radar:
        m_data.time_for_radar -= 1
        time.sleep(1)
    m_client.send("pass:")
# метод з атакою
def attack(pos: tuple,multiplier_x,multiplier_y):
    # створення глобальних змінних
    global list_miss, list_explosion
    # умова для повора кораблів
    # blits = True
    if m_data.turn and m_data.connected :
        # цикл для ряду
        if m_data.attack == 'homing_rocket':
            list_ships = []
            for ship in m_data.enemy_ships:
                if not ship in m_data.all_ships:
                    list_ships.append(ship)
            
            main_ship = list_ships[random.randint(0,len(list_ships)-1)]
            main_cell = random.randint(0,int(main_ship.name)-1)
            rotate_ship = main_ship.rotate

            if rotate_ship % 180 == 0:
                name = attack_for_cell(main_ship.row,main_cell + main_ship.cell)
                m_client.send(f"attack:{ main_ship.row},{main_cell + main_ship.cell},{name}".encode())
            else:
                name = attack_for_cell(main_cell + main_ship.row,main_ship.cell)
                m_client.send(f"attack:{main_cell + main_ship.row},{main_ship.cell},{name}".encode())
            # if name: 
            m_data.attack = None
            #
            m_audio.explosion.play()
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
                            m_client.send(text.encode())
                            m_data.attack = None
                        elif m_data.attack == 'radar':
                            width = 55.7 * multiplier_x
                            height = 55.7 * multiplier_y
                            x = (725+55.7*cell) * multiplier_x
                            y = (115+55.7*row) * multiplier_y
                            start_cell = cell
                            start_row = row
                            end_cell = cell
                            end_row = row
                            print(row,cell)
                            if row > 1:
                                width += 55.7 * multiplier_x *2
                                x -= 55.7 * multiplier_x *2
                                start_row -= 2
                            if row < 8:
                                width += 55.7 * multiplier_x*2
                                end_row += 2
                            if cell < 8:
                                height += 55.7 * multiplier_y*2
                                end_cell += 2
                            if cell > 1:
                                start_cell -=2
                                height += 55.7 * multiplier_y*2
                                y -= 55.7 * multiplier_y * 2 
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
                        else:
                            name = attack_for_cell(row,cell)
                            if name: 
                                m_client.send(f"attack:{row},{cell},{name}".encode())
                                #
                                m_audio.explosion.play()
                        # умова для клітинок заповнених ворожими кораблями
                    
    win_lose()
def win_lose():
    yes_no = True
    print(m_data.enemy_ships, 153)
    
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
        m_client.send("lose:?????".encode())