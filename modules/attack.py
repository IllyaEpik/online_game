# імпортуємо необхідні модулі
import pygame 
import modules.data as m_data
import modules.images as m_images
import modules.client as m_client
import modules.audio as m_audio
# список клітинок без кораблів
list_miss = "05"
# список клітинок з кораблями
list_explosion = "1234"
# метод з атакою
def attack(pos: tuple):
    # створення глобальних змінних
    global list_miss, list_explosion
    # умова для повора кораблів
    if m_data.turn:
        # цикл для ряду
        for row in range(10):
            # цикл для клітинки
            for cell in range(10):
                # створюємо хіт-бокс
                rect = pygame.Rect(725+55.7*cell, 
                                115+55.7*row,
                                55.7,
                                55.7)
                # перевірка на колізію
                if rect.collidepoint(pos):
                    for rows in m_data.enemy_field:
                        print(rows)
                    print('ok')
                    for rows in m_data.my_field:
                        print(rows)
                    # 6 - explosion 7 - miss
                    # змінна ім'я зі значенням нічого
                    name = None
                    # умова для клітинок заповнених ворожими кораблями
                    if str(m_data.enemy_field[row][cell]) in list_explosion:
                        # відправляє закодовані данні
                        m_client.send(f"attack:{row},{cell} explosion".encode())
                        # import time
                        # time.sleep(0.1)
                        # відповідає за те яка клітинка створиться
                        name = "explosion"
                        # клітинка з вибухнувшим кораблем
                        m_data.enemy_field[row][cell] = 6
                        # for ship in m_data.enemy_ships:
                        # список з клітинками в яких є кораблі
                        explosions = []
                        # 
                        # цикл для ворожих кораблів
                        for ship in m_data.enemy_ships:
                            # перевіряє ворожий корабль
                            ship.check_enemy()
                            # умова для всіх кораблів
                            if ship in m_data.all_ships:
                                # список з клітинками кораблів
                                cells = []
                                # цикл для додавання всіх клітинок корабля до cells
                                for count in range(int(ship.name[0])):
                                    # якщо корабель стоїть горизонтально то
                                    if ship.rotate %180 == 0 and m_data.my_field[ship.row][ship.cell+count] != int(ship.name[0]):
                                        # додається клітика
                                        cells.append([ship.row, ship.cell+count])
                                    # інакше якщо корабель стоїть вертикалюно то
                                    elif ship.rotate %180 != 0 and m_data.my_field[ship.row+count][ship.cell] != int(ship.name[0]):
                                        # додається клітинка
                                        cells.append([ship.row+count, ship.cell])
                                #
                                for explosion in m_data.list_explosions:
                                    #
                                    for celll in cells:
                                        #
                                        if explosion[1] == celll[0] and explosion[2] == celll[1]:
                                            #
                                            explosions += [explosion[0]]
                        #           
                        for ex in explosions:
                            try:
                                #
                                m_data.list_blits['game'].remove(ex)
                            except:
                                pass
                    #
                    elif str(m_data.enemy_field[row][cell]) in list_miss:
                        #
                        m_data.enemy_field[row][cell] = 7
                        #
                        name = "miss"
                        #
                        m_data.turn = False
                        #
                        m_client.send(f"attack:{row},{cell} miss".encode())
                    #
                    if name:
                        #
                        image = m_images.Image(
                            progression = "game",
                            name = name,
                            x = 725+55.7*cell,
                            y = 115+55.7*row,
                            width= 55.7,
                            height=55.7
                        )
                        #
                        if name == 'explosion':
                            #
                            print(image, row, cell)
                            # m_audio.explosion.play()
                            #
                            m_data.list_explosions.append([image, row, cell])
                            # m_audio.track.play()
                    for ship in m_data.enemy_ships:
                        # перевіряє ворожий корабль
                        ship.check_enemy()
    win_lose()
def win_lose():
    yes_no = True
    print(m_data.enemy_ships, 153)

    for ship in m_data.all_ships:
        if ship in m_data.enemy_ships:
            pass
        elif not ship.explosion:
            yes_no = False
    if yes_no and m_data.enemy_ships:
        m_data.progression = "lose"
        m_client.send("lose:".encode())