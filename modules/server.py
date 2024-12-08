import socket
import modules.data as m_data
import modules.ships as m_ships
import modules.images as m_images
# from .main_window import Screen

# server_screen = Screen().run()
# server = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
# ip = "127.0.0.1"
# ip = '46.118.25.208'
# print(ip)
# print(hostname)
print(socket.SO_KEEPALIVE,'132123132321132132132')
def activate():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as server:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        server.bind((f"{ip}", 8800))
        server.listen()
        client = server.accept()
        for coun in range(100):
            print(client[1],"katkit")
        # print()
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
                image = m_images.Image(
                    progression = "game",
                    name = data[1].split(" ")[-1],
                    x = 59+55.7*pos[1],
                    y = 115+55.7*pos[0],
                    width= 55.7,
                    height=55.7
                )

                        # m_data.list_explosions.remove(ex)
                        
                #     m_data.turn = False
            elif data[0] == "explosion":
                pos = data[1].split(",")
                pos = [int(pos[0]), int(pos[1])]
                for ship in m_data.all_ships:
                    if ship in m_data.enemy_ships:
                        pass
                    elif ship.row == pos[0] and ship.cell == pos[1]:
                        ship.explosion = True
                        # cells = []
                        # for count in range(int(ship.name[0])):
                        #     if ship.rotate % 180 == 0 and m_data.my_field[ship.row][ship.cell + count] != int(ship.name[0]):
                        #         cells.append([ship.row, ship.cell + count])

                        #     elif ship.rotate % 180 != 0 and m_data.my_field[ship.row + count][ship.cell] != int(ship.name[0]):
                        #         cells.append([ship.row + count, ship.cell])
    
                        # field = m_data.my_field
                        # # print(cells)
                        # for celll in cells:
                        #     row = celll[0]
                        #     cell = celll[1]
                        #     # print(row, cell)
                        #     m_ships.fill_field(field)
                        #     ship.check(field=field, row=row + 1, cell=cell + 1, values=[5, 7])
                        #     ship.check(field=field, row=row - 1, cell=cell - 1, values=[5, 7])
                        #     ship.check(field=field, row=row - 1, cell=cell + 1, values=[5, 7])
                        #     ship.check(field=field, row=row + 1, cell=cell - 1, values=[5, 7])
                        #     ship.check(field=field, row=row + 1, cell=cell, values=[5, 7])
                        #     ship.check(field=field, row=row, cell=cell + 1, values=[5, 7])
                        #     ship.check(field=field, row=row - 1, cell=cell, values=[5, 7])
                        #     ship.check(field=field, row=row, cell=cell - 1, values=[5, 7])

            m_data.enemy_data.append(client_data)
# 127.0.0.1
# activate()