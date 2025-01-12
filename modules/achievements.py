# імпортуємо необхідні модулі
import pygame, os, time, threading
# з файлу дата імпортуємо дату
import modules.data as m_data
# з файлу аудіо імпортуємо аудіо
import modules.audio as m_audio
# задаємо ширину
width = 400
# задаємо висоту
height = 120
# задаємо y
y = 0
# задаємо x
x = 1280

# класс з досягненнями
class achievement():
    # метод класу
    def __init__(self,name):
        # робимо змінні глобальними
        global x,y,width,height
        # перевіряємо чи не має досягнення
        if m_data.achievements_data[name]['has'] == "False":
            # задаємо наявність досягнення
            m_data.achievements_data[name]['has'] = "True"
            if name != "Into the Sunset...":
                yes_no = True
                for achievement_code in m_data.achievements_data:
                    if not m_data.achievements_data[achievement_code]['has'] and achievement_code!= "Into the Sunset...":
                        yes_no = False
                if yes_no:
                    achievement("Into the Sunset...")
            # задаємо шрифт
            self.FONT = pygame.font.SysFont("algerian", 40)
            # задаємо розмір квадрату
            self.rect = pygame.Rect(x,y,width,height)
            # додаємо срисок досягнень
            m_data.list_achievements.append(self)
            # розділяємо текст на частини
            self.text = name.split(' ')
            # об'єднує розмір шрифта тексту
            size = self.FONT.size(" ".join(self.text))
            # перевіряємо розмір
            if size[0] < 300:
                # об'єднуємо текст
                self.text = [" ".join(self.text)]
            # віднімаємо 2 від довжини тексту
            elif len(self.text)-2:
                # створюємо список для тексту
                list_text = []
                # створюємо змінну з текстом
                text = ''
                # цикл для тексту
                for text_for in self.text:
                    # розмір шрифту
                    size = self.FONT.size(text+text_for)
                    # перевіряємо розмір
                    if size[0] < 280:
                        # додаємо текст до змінної з текстом для
                        text += text_for+' '
                    # перевіряємо розмір
                    if size[0] > 280:
                        # додаємо текст до списку
                        list_text.append(text)
                        # текст дорівнює змінній текст для
                        text = text_for
                    # від тексту віднімаємо одне значення
                    elif self.text[-1] == text_for:
                        # додаємо текст до списку
                        list_text.append(text)
                # перевіряємо чи немає текту в списку
                if not text_for in list_text[-1]:
                    # додаємо розміри текту і тексту для
                    size = self.FONT.size(text+text_for)
                    # перевіряємо розмір
                    if size[0] < 280:
                        # додаємо текст до змінної з текстом для
                        text += text_for+' '
                    # перевіряємо розмір
                    if size[0] > 280:
                        # додаємо текст до списку
                        list_text.append(text)
                        # текст дорівнює змінній текст для
                        text = text_for
                    # від тексту віднімаємо одне значення
                    elif self.text[-1] == text_for:
                        # додаємо текст до списку
                        list_text.append(text)
                # тукст дорівнює списку з текстом
                self.text = list_text
            # звук при отриманні досягнення   
            m_audio.achievement.play()
            # задаємо час
            self.time = 5
            # задаємо активацію таймеру
            self.activate_timer = False
            # задаємо деактивацію таймеру
            self.deactivate_timer = False
            # задаємо ім'я
            self.name = name
            # безпечно відкриваємо файл
            with open(m_data.path+m_data.type+'achievements'+m_data.type+name+'.txt', "w") as file:
                # записуємо значення True в файл
                file.write('True')
    # метод для руху
    def move(self):
        # робимо змінні глобальними
        global x,y,width,height
        # перевіряємо чи не активований таймер
        if not self.activate_timer:
            # перевіряємо x квадрату і не деактивований таймер
            if self.rect.x < 1280-395 and not self.deactivate_timer:
                # активовуємо таймер
                self.activate_timer = True
                # створення потоків
                threading.Thread(target=self.timer,daemon=1).start()
            # перевіряємо x квадрату і деактивовацію таймеру
            elif self.rect.x > 1280 and self.deactivate_timer:
                # видаляємо зі списку
                m_data.list_achievements.remove(self)
            else:
                # перевіряємо чи не деактивований таймер
                if not self.deactivate_timer:
                    # від x квадрату віднімаємо 15
                    self.rect.x -= 15
                else:
                    # від x квадрату додаємо 15
                    self.rect.x += 15
    # промальовуємо основу поверхності
    def blit(self,screen:pygame.Surface,multiplier_x,multiplier_y):
        # завантажуємо картинку
        self.img = pygame.image.load(os.path.abspath(f"{__file__}/../../images/achievements/{self.name}.png"))
        # трансформуємо масштаб
        self.img = pygame.transform.scale(self.img, (100, 100))
        # кольори пікселів, які збігаються стають прозорими
        self.img.set_colorkey((0, 0, 0))
        # змінюємо розмір квадрату
        rect = pygame.Rect(
            self.rect.x*multiplier_x,
            self.rect.y*multiplier_y,
            self.rect.width*multiplier_x,
            self.rect.height*multiplier_y
            )
        # промальовка квадрату
        square = pygame.Surface((rect.width,rect.height))
        # заповнення квадрату кольором
        square.fill((69, 69, 69))
        # заливаємо квадрат кольором зображення
        square.set_alpha(200)
        # відображення квадрату на екрані
        screen.blit(square,rect)
        # відображення картинки на екрані
        screen.blit(self.img, ((self.rect.x+10)*multiplier_x,(self.rect.y)*multiplier_y))
        # задаємо кількість
        count = 0
        # цикл для текту
        for text in self.text:
            # перевіряємо чи x більший за y
            if multiplier_x > multiplier_y:
                # задаємо шрифт для тексту y
                self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_y)))
            else:
                # задаємо шрифт для тексту x
                self.FONT = pygame.font.SysFont("algerian", int((40*multiplier_x)))
            # задаємо шрифт для висоти
            height = self.FONT.size(text)[1]
            # задаємо y для тексту
            y = (self.rect.y+10+height*count) * multiplier_y
            # задаємо x для тексту
            x = (self.rect.x + 120)*multiplier_x
            # відображення тексту на екрані
            screen.blit(self.FONT.render(text,True,(0,0,0)), (x, y))
            # до кількості додаємо 1
            count += 1
    # метод для таймеру
    def timer(self):
        # працює поки час не дорувнює 0
        while self.time != 0:
            # від часу віднімається 1
            self.time -= 1
            # пауза 1 секунда
            time.sleep(1)
        # задаємо значення True для деактивації таймеру
        self.deactivate_timer = True
        # задаємо значення False для активації таймеру
        self.activate_timer = False
