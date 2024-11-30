import socket
import modules.data as m_data
import threading 
import modules.ships as m_ships
# from .main_window import Screen

# server_screen = Screen().run()
# server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
# ip = "127.0.0.1"
# ip = '46.118.25.208'
print(ip)
print(hostname)
def activate():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server:

        server.bind((f"{ip}", 8800))
        server.listen()
        client = server.accept()
        print("Acept_Client")
        while True:
            client_data = client[0].recv(1024).decode()
            # print('1231212312312123')
            print(client_data)
            data = client_data.split(":")
            # print('GOOD')
            if data[0] == "field":
                # print('GOOD1')
                data = data[1].split(" ")
                for ship in data:
                    splited_data = ship.split(",")
                    if splited_data != [""]:
                        
                        print('create ship')
                        print(splited_data)
                        ship = m_ships.Ship(x = 724,y = 115,
                                    field_cor = (724,115),
                                    name  = splited_data[0],
                                    row = int(splited_data[1]),
                                    cell = int(splited_data[2]),
                                    rotate = int(splited_data[3]),
                                    add = False)
                        for count in range(int(ship.name[0])):
                            if ship.rotate % 180 == 0:
                                
                                m_data.enemy_field[ship.row][ship.cell+count] = int(ship.name[0])
                            else:
                                m_data.enemy_field[ship.row+count][ship.cell] = int(ship.name[0])

                        m_data.enemy_ships.append(ship)

                for row in m_data.enemy_field:
                    print(row)
            elif data[0] == "attack":
                print("attack_get")
                pos = data[1].split(" ")[0].split(",")
                pos = [int(pos[0]), int(pos[1])]
                if data[1].split(" ")[-1] == "miss":
                    m_data.turn = True
                    m_data.my_field[pos[0]][pos[1]] = 7
                else:
                    m_data.my_field[pos[0]][pos[1]] = 6
                    
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
                        # m_data.list_explosions.remove(ex)
                        
                #     m_data.turn = False
                
            m_data.enemy_data.append(client_data)
# 127.0.0.1
# activate()