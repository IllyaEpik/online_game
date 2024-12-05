import pygame
import modules.data as m_data
import modules.images as m_images
import modules.client as m_client
import modules.audio as m_audio
list_miss = "05"
list_explosion = "1234"
def attack(pos: tuple):
    global list_miss, list_explosion
    if m_data.turn:
        for row in range(10):
            for cell in range(10):

                rect = pygame.Rect(725+55.7*cell, 
                                115+55.7*row,
                                55.7,
                                55.7)
                if rect.collidepoint(pos):
                    # 6 - explosion 7 - miss
                   
                    name = None
                    if str(m_data.enemy_field[row][cell]) in list_explosion:
                        name = "explosion"
                        m_client.send(f"attack:{row},{cell} explosion".encode())
                        m_data.enemy_field[row][cell] = 6
                        for ship in m_data.enemy_ships:
                            ship.check_enemy()
                        explosions = []
                        
                        for ship in m_data.enemy_ships:
                            if ship in m_data.all_ships:
                                cells = []
                                for count in range(int(ship.name[0])):
                                    if ship.rotate %180 == 0 and m_data.my_field[ship.row][ship.cell+count] != int(ship.name[0]):
                                        cells.append([ship.row, ship.cell+count])
                                    
                                    elif ship.rotate %180 != 0 and m_data.my_field[ship.row+count][ship.cell] != int(ship.name[0]):
                                        cells.append([ship.row+count, ship.cell])
                                for explosion in m_data.list_explosions:
                                    # [1 3] 
                                    # 1 == [1,1]
                                    for celll in cells:
                                        print(explosion[1], celll[0], explosion[2], celll[1])
                                        

                                        if explosion[1] == celll[0] and explosion[2] == celll[1]:
                                            explosions += [explosion[0]]
                                    
                        for ex in explosions:
                            try:
                                m_data.list_blits['game'].remove(ex)
                            except:
                                pass
                    elif str(m_data.enemy_field[row][cell]) in list_miss:
                        m_data.enemy_field[row][cell] = 7
                        name = "miss"
                        m_data.turn = False
                        m_client.send(f"attack:{row},{cell} miss".encode())
                    
                    if name:
                        image = m_images.Image(
                            progression = "game",
                            name = name,
                            x = 725+55.7*cell,
                            y = 115+55.7*row,
                            width= 55.7,
                            height=55.7
                        )
                        if name == 'explosion':
                            print(image, row, cell)
                            # m_audio.explosion.play()
                            m_data.list_explosions.append([image, row, cell])
                            # m_audio.track.play()