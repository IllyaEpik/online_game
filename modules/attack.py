import pygame
import modules.data as m_data
import modules.images as m_images
import modules.client as m_client

def attack(pos: tuple):
    if m_data.turn:
        for row in range(10):
            for cell in range(10):

                rect = pygame.Rect(725+55.7*cell, 
                                115+55.7*row,
                                55.7,
                                55.7)
                if rect.collidepoint(pos):
                    # 6 - explosion 7 - miss
                    list_miss = "05"
                    list_explosion = "1234"
                    # list_author
                    name = None
                    if str(m_data.enemy_field[row][cell]) in list_explosion:
                        name = "explosion"
                        m_client.send(f"attack:{row},{cell} explosion".encode())
                    elif str(m_data.enemy_field[row][cell]) in list_miss:
                        name = "miss"
                        m_data.turn = False
                        m_client.send(f"attack:{row},{cell} miss".encode())
                    if name:
                        m_images.Image(
                            progression = "game",
                            name = name,
                            x = 725+55.7*cell,
                            y = 115+55.7*row,
                            width= 55.7,
                            height=55.7
                        )
                        