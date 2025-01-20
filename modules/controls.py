import modules.data as m_data
import modules.audio as m_audio
import modules.images as m_images
import modules.buttons as m_buttons
import pygame

controls = {
    "rotate ship":[pygame.K_r,None,None,None,],
    'random attack':[pygame.K_r,None,None,None, ],
    "fire attack":[pygame.K_LSHIFT,None,None,None, ],
    'last item': [pygame.K_LCTRL,None,None,None,]
}
descriptions = ['this key rotate your ship','this key do random attack on enemy field','if you attack when you press this key use fire rocket','use last item what you buy in shop (previous turn)']
l_controls = {}
for control in controls:
    print(controls[control])
    l_controls[control] = f'{controls[control][0]},{controls[control][1]},{controls[control][2]},{controls[control][3]}'
controls2 = m_data.reading_data(l_controls,'controls.txt')
if controls2:
    controls = controls2
    for control in controls:
        print(control,'who is it')
        controls[control] = controls[control].split(',')
music = {
    "soundtracks":[
        '4',
        "3",
        '2',
        '1'
    ]
}
x = 20
y = 200
list_controls = []
list_music = [[m_buttons.Button(progression='sounds',name='button_start',y=y,x=x,width=500,height=100,fun=f"sounds:{music['soundtracks']}",text=f"soundtracks"),0,'soundtracks']]
for control in controls:
    list_controls.append( [m_buttons.Button(progression='keys',name='button_start',y=y,x=x,width=500,height=100,fun=f'key:{control}',text=f"{control}"),0,control])
    y += 120
list_keys = []
list_musics = []

def text_edit(current):
    global list_keys
    y = 700
    x = 825
    list_keys = []
    for count in range(4):
        if current:
            print(type(controls[current][count]))
            if type(controls[current][count]) != type(1) and 'None' in controls[current][count]:
                text = 'None'
            else:
                text = pygame.key.name(int(controls[current][count]))
        else:
            text = 'None'
        list_keys.append([m_buttons.Button(width= 400,height=100,x=x,y=y,text=text,progression='Noke'),0,count])
        y -= 120
text_edit(None)
def music_edit(current):
    global list_musics
    y = 700
    x = 825
    list_musics = []
    for count in range(4):
        print()
        if current:
            text = music[current][count]
        else:
            text = 'None'
        print(text,current,10)
        list_musics.append([m_buttons.Button(width= 400,height=100,x=x,y=y,text=text,progression='Noke'),0,count])
        y -= 120
music_edit(None)