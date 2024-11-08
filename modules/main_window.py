import pygame
pygame.init()
import modules.buttons as m_buttons
import modules.data as m_data
import modules.images

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
            self.screen.fill((255,255,255))
            for sprite in m_data.list_blits[m_data.progression]:
                sprite.blit(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

screen = Screen()