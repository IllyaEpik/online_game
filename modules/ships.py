import modules.images as m_images
import modules.data as m_data
import pygame 

class Ship(m_images.Image):
    def __init__(self, x: int, y: int, name='1', row = 0, cell = 0, field_cor = [59, 115]):
        self.width = int(name[0]) * 50
        self.height = 50
        print(self.height)
        super().__init__(self.width, self.height, x, y, name, "F")
        self.x += (cell * 55.7)
        self.y += (row * 55.7)
        m_data.all_ships.append(self)
        print(self.y)
        self.select = False
        self.row = row
        self.cell = cell
        for count in range(int(name[0])):
            m_data.my_field[row][cell+count] = int(name[0])
        self.field_cor = field_cor
        self.field = pygame.Rect(field_cor, (10 * 55.7, 10 * 55.7))
        self.rect = pygame.Rect(self.x, self.y,self.width,self.height)



    def activate(self, event):
        if self.rect.collidepoint(event.pos):
            self.select = True
            print('eqw')
        else:
            self.select = False
    def place(self, event):
        if self.select:
            print(self.field.collidepoint(event.pos))
            for row in range(10):
                for cell in range(10):
                    if m_data.my_field[row][cell] == 0:
                        rect = pygame.Rect(
                            self.field_cor[0] + cell * 55.7,
                            self.field_cor[1] + row * 55.7,
                            55.7,55.7)
                        if rect.collidepoint(event.pos):
                            m_data.my_field[self.row][self.cell] = 0 
                            self.row = row
                            self.cell = cell
                            self.x = (cell * 55.7) + self.field_cor[0]
                            self.y = (row * 55.7) + self.field_cor[1]
                            self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
                            m_data.my_field[row][cell] = self.name[0]
                            self.select = False
                            return True
            # if self.field_cor[0] + 10 * 55.7 > cor[0]:
            #     pass
ship = Ship(x = 59, y = 115)
ship1 = Ship(x = 59, y = 115, cell = 8, row = 1)
ship2 = Ship(x = 59, y = 115, cell = 5, row = 2)
ship3 = Ship(x = 59, y = 115, cell = 2, row = 3)
