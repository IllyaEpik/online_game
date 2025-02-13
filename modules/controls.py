# імпортуємо необхідні модулі
import modules.data as m_data
import modules.audio as m_audio
import modules.images as m_images
import modules.buttons as m_buttons
import customtkinter
import pygame, os, shutil
screen = customtkinter.CTk()
screen.withdraw()
# print()
# словник для крнтролю
controls = {
    "rotate ship":[pygame.K_r,None,None,None,],
    'random attack':[pygame.K_r,None,None,None, ],
    "fire attack":[pygame.K_LSHIFT,None,None,None, ],
    'last item': [pygame.K_LCTRL,None,None,None,]
}
y_wheel = -120
surface_sizes = [500,680]
music_surface = pygame.Surface([500,600])
music_surface.get_height
# список для лрису
descriptions = ['this key rotate your ship','this key do random attack on enemy field','if you attack when you press this key use fire rocket','use last item what you buy in shop (previous turn)']
# словник з управлінням
l_controls = {}
# цикл для контролю
for control in controls:
    print(controls[control])
    # додаємо контроль в управління
    l_controls[control] = f'{controls[control][0]},{controls[control][1]},{controls[control][2]},{controls[control][3]}'
# змінна з контролем2
controls2 = m_data.reading_data(l_controls,'controls.txt')
# превіряємо контроль2
if controls2:
    # контроль дорівнює контролю2
    controls = controls2
    # цикл для контролю
    for control in controls:
        print(control,'who is it')
        # розділяємо на строки за допомогою ','
        controls[control] = controls[control].split(',')
# словник для музики
music = {
    "soundtracks":[
        '5',
        '4',
        "3",
        '2',
        '1'
    ]
}
# задаємо x
x = 20
# задаємо y
y = 200
# створюємо список для управління
list_controls = []
# створюємо список для музики, наслідуємо клас Button і задаємо параметри
list_music = [[m_buttons.Button(progression='sounds',name='button_start',y=y,x=x,width=500,height=100,fun=f"sounds:{music['soundtracks']}",text=f"soundtracks"),0,'soundtracks']]
# цикл для контролю
for control in controls:
    # до списку контролю додаємо параметри
    list_controls.append( [m_buttons.Button(progression='keys',name='button_start',y=y,x=x,width=500,height=100,fun=f'key:{control}',text=f"{control}"),0,control])
    # змінюємо y
    y += 120
# створюємо список ключів
list_keys = []
# створюємо список для музики
list_musics = []

off_change_button = m_buttons.Button(progression='sounds', name='off_change', y=y, x=x, width=500, height=100, fun='off_change', text='Off Change')
list_musics.append(off_change_button)

def draw(screen,multiplier_x=1,multiplier_y=1):
    pygame.draw.line(screen,(255,255,255),(942*multiplier_x,60*multiplier_y),(1242*multiplier_x,60*multiplier_y),25)
    pygame.draw.line(screen,(50,255,50),(942*multiplier_x,60*multiplier_y),(942*multiplier_x+(300*m_audio.main_volume*multiplier_x),60*multiplier_y),25)
def fun(pos:list,multiplier_x,multiplier_y,hk):
    if 1242*multiplier_x> pos[0] > 942*multiplier_x and 50*multiplier_y < pos[1] < 80*multiplier_y:

        m_audio.main_volume = (pos[0]-(942*multiplier_x))/(300*multiplier_x)
        print(m_audio.main_volume,pos[0]-(942*multiplier_x),300*multiplier_x) 
        m_audio.track.volume(m_audio.main_volume*m_audio.soundtrack)
        with open(m_data.path+m_data.type+'volume.txt', "w") as file:
            file.write(str(m_audio.main_volume))

# функція для редагування тексту
def text_edit(current):
    '''
        >>> Редагує текст
    '''
    # робимо список ключів глобальним
    global list_keys
    # задаємо y
    y = 700
    # задаємо x
    x = 825
    # створюємо список ключів
    list_keys = []
    # цикл для кількості
    for count in range(4):
        # перевіряємо поточність
        if current:
            print(type(controls[current][count]))
            # перевіряє тип контролю
            if type(controls[current][count]) != type(1) and 'None' in controls[current][count]:
                # задає текст None
                text = 'None'
            else:
                # до тексту записуємо ключ
                text = pygame.key.name(int(controls[current][count]))
        else:
            # задає текст None
            text = 'None'
        # до списку з ключами задаємо параметри через наслідування класа Button 
        list_keys.append([m_buttons.Button(width= 400,height=100,x=x,y=y,text=text,progression='Noke'),0,count])
        # змінюємо y
        y -= 120
# до функції редагування тексту додаємо значення None
text_edit(None)
# створює функцію для редагування музики
def music_edit(current,multiplier_x):
    '''
        >>> Змінює саундтрек
    '''
    # Використовуємо глобальну змінну list_musics, щоб зберігати кнопки
    global list_musics
    # Початкова координата y для кнопок
    y = 600
    # Початкова координата x для кнопок
    x = 0
    # Очищуємо список vepbrb
    list_musics = []
    if not current:
        current = 'soundtracks'
    # Цикл для створення 4 кнопок
    for count in range(len(music['soundtracks'])):
        # Друк порожнього рядка 
        # print()
        # перевіряємо поточне
        if current:
            # беремо музику з тексту
            text = music[current][count]
        else:
            # до тексту задаємо значення None
            text = 'None'
        # друк тексту кнопки, поточного значення і постійного значення 10
        # print(text, current, 10)
        # Додаємо нову кнопку в список з музикою
        list_musics.append([m_buttons.Button(width=100, height=100, x=x, y=y, text=text, progression='Noke'),
                            # m_buttons.Button(width=400, height=100, x=x - 50 * multiplier_x, y=y, text=text, progression='Noke'),
                            m_buttons.Button(width=100, height=100, x=x + 150 * multiplier_x, y=y, text="", progression=text, name = "upload",fun=music_upload),
                            0, count])
        # print(x,y)
        # Змінюємо координату y для розташування кнопок вертикально
        y -= 120
def music_upload(self:m_buttons.Button):
    # print('haaaaads')
    filename = customtkinter.filedialog.askopenfilename(filetypes=(('MP3','*.mp3'),("WAV","*.wav"),('OGG','*.ogg'))) 
    r = None
    # with open(filename,'r') as file:
    #     r = file
    #     os.path
    # with open(,'w') as file:
    #     file.writable(r)
    # 
    # os.remove()
    shutil.copy(filename,os.path.abspath(m_data.path+f"/../audio/Soundtracks/{self.progression}.{filename.split('.')[-1]}"))
# Виклик функції 
music_edit(None,1)


