import modules.images as m_images
import modules.data as m_data
import pygame 

class Ship(m_images.Image):
    def __init__(self, x: int, y: int, name='1', row = 0, cell = 0, field_cor = [59, 115], rotate = 0):
        self.width = int(name[0]) * 50
        self.height = 50
        print(self.height)
        super().__init__(self.width, self.height, x, y, name, "F", rotate)
        self.x += (cell * 55.7)
        self.y += (row * 55.7)
        m_data.all_ships.append(self)
        print(self.y)
        self.select = False
        self.row = row
        self.cell = cell
        
        for count in range(int(name[0])):
            if rotate %180 == 0:
                m_data.my_field[row][cell+count] = int(name[0])
            else:
                m_data.my_field[row+count][cell] = int(name[0])
        self.field_cor = field_cor
        self.field = pygame.Rect(field_cor, (10 * 55.7, 10 * 55.7))
        self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
        self.celled = None


    def activate(self, event):
        if self.rect.collidepoint(event.pos):
            self.select = True
            print('eqw')
        else:
            self.select = False

    def rotate_ship(self): 
        print(2132132312123123231213231)

        for count in range(int(self.name[0])):
            if self.rotate % 180 == 0:
                m_data.my_field[self.row][self.cell+count] = 0
            else:
                m_data.my_field[self.row+count][self.cell] = 0
        self.rotate = self.rotate + 90
        fill_field(m_data.my_field)
        no_yes= True 
        try:
            for count in range(int(self.name[0])):
                if self.rotate % 180 == 0:
                    if m_data.my_field[self.row][self.cell+count] != 0:
                        no_yes = False
                else:
                    if m_data.my_field[self.row+count][self.cell] != 0:
                        no_yes = False
        except:no_yes = False
        if no_yes: 
            self.update_image()
        else: 
            self.rotate -= 90
        for count in range(int(self.name[0])):
            if self.rotate % 180 == 0:
                m_data.my_field[self.row][self.cell+count] = int(self.name[0])
            else:
                m_data.my_field[self.row+count][self.cell] = int(self.name[0])
        
    def place(self, event):
        if self.select:
            print(self.field.collidepoint(event.pos))
            for row in range(10):
                for cell in range(10):
                    if m_data.my_field[row][cell] == 5:
                        try:
                            for count in range(int(self.name[0])):
                                print(count,(self.name[0]),row,cell)
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell+count] = 0
                                else:
                                    m_data.my_field[self.row+count][self.cell] = 0
                            fill_field(m_data.my_field)
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell+count] = int(self.name[0])
                                else:
                                    m_data.my_field[self.row+count][self.cell] = int(self.name[0])
                        except:print("копибара")
                        # m_data.my_field[row][cell] = 0
                    if m_data.my_field[row][cell] == 0:
                        rect = pygame.Rect(
                            self.field_cor[0] + cell * 55.7,
                            self.field_cor[1] + row * 55.7,
                            55.7,55.7)
                        if rect.collidepoint(event.pos):
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[self.row][self.cell+count] = 0
                                else:
                                    m_data.my_field[self.row+count][self.cell] = 0
                            if self.celled:
                                m_data.cells[self.name[0]][self.celled][0] = False
                                self.celled = None
                            self.row = row
                            self.cell = cell
                            self.x = (cell * 55.7) + self.field_cor[0]
                            self.y = (row * 55.7) + self.field_cor[1]
                            self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
                            for count in range(int(self.name[0])):
                                if self.rotate % 180 == 0:
                                    m_data.my_field[row][cell+count] = int(self.name[0])
                                else:
                                    m_data.my_field[row+count][cell] = int(self.name[0])
                            self.select = False
                            fill_field(m_data.my_field)
                            for row in m_data.my_field:
                                print(row)
                            return True
            count = 0
            for cell1 in m_data.cells[self.name[0]]:
                print(cell1)
                if not cell1[0]:
                    cell1[0] = True
                    self.x = cell1[1][0]
                    self.y = cell1[1][1]
                    m_data.my_field[row][cell] = 0 
                    self.celled = count
                    self.rect = pygame.Rect(self.x, self.y,self.width,self.height)
                    for row in m_data.my_field:
                         print(row)      
                    break
                count += 1 
            # if self.field_cor[0] + 10 * 55.7 > cor[0]:
            #     pax = 59, y = 115ss
    for row in m_data.my_field:
        print(row)
def check(field, row, cell):
    if row != -1 and -1 != cell:
        if row != 10  and 10 != cell:
            # print(row,cell)
            if field[row][cell] == 0:
                field[row][cell] = 5

def fill_field(field:list):
    clear_field(field)
    for row in range(10):
        for cell in range(10):
            cell_on_field = field[row][cell]
            if cell_on_field != 5 and cell_on_field != 0:
                check(field= field, row= row+1, cell= cell+1)
                check(field= field, row= row-1, cell= cell-1)
                check(field= field, row= row-1, cell= cell+1)
                check(field= field, row= row+1, cell= cell-1)
                
                check(field= field, row= row+1, cell= cell)
                check(field= field, row= row, cell= cell+1)
                check(field= field, row= row-1, cell= cell)
                check(field= field, row= row, cell= cell-1)

def clear_field(field):
    for row in range(10): 
        for cell in range(10):
            if field[row][cell] == 5:
                field[row][cell] = 0

ship1 = Ship(x = 59, y = 115, cell = 8, row = 1)
ship2 = Ship(x = 59, y = 115, cell = 5, row = 2)
ship3 = Ship(x = 59, y = 115, cell = 2, row = 3)
fill_field(m_data.my_field)