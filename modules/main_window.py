import pygame
pygame.init()
import modules.buttons as m_buttons
import modules.data as m_data
import modules.images
import modules.ships as m_ships
class Screen():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.WIDTH= 1280
        self.HEIGHT = 832
        self.screen = pygame.display.set_mode(size= (self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('online game')
    def run(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if m_data.progression != "menu":
                        for ship in m_data.all_ships:
                            ship.place(event)
                    else:
                        m_buttons.input.activate(event) 
                        m_buttons.button_start.button_start(event)
                    if m_data.progression == "pre-game":
                        for ship in m_data.all_ships:
                            ship.activate(event)
                if event.type == pygame.KEYDOWN:
                    m_buttons.input.edit(event)
            self.screen.fill((255,255,255))
            for sprite in m_data.list_blits[m_data.progression]:
                sprite.blit(self.screen)
                
            if m_data.progression != "menu":
                for ship in m_data.all_ships:
                    ship.blit(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

screen = Screen()