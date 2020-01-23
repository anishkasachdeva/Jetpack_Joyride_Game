from obstacles import Coins, Obstacles_horizontal, Obstacles_vertical, Obstacles_slanting, Magnet
import random
import global_var


def Generate_coordinates(height, width, grid):
    y = 0
    while(y <= width - 200):
        type = random.choice([1,2,3,4])
        x = random.randint(10,19)
        y += random.randint(20,40)

        if type == 1:
            coin_obj = Coins(x,y)
            coin_obj.put_in_grid(coin_obj.height, coin_obj.width, coin_obj.matrix, grid, type)
            y += 20

        elif type == 2:
            horizontal_obj = Obstacles_horizontal(x,y)
            horizontal_obj.put_in_grid(horizontal_obj.height, horizontal_obj.width, horizontal_obj.matrix , grid, type)
            y += 20

        elif type == 3:
            vertical_obj = Obstacles_vertical(x,y)
            vertical_obj.put_in_grid(vertical_obj.height, vertical_obj.width, vertical_obj.matrix, grid, type)
            y += 20

        elif type == 4:
            slanting_obj = Obstacles_slanting(x,y)
            slanting_obj.put_in_grid(slanting_obj.height, slanting_obj.width, slanting_obj.matrix, grid, type)
            y += 20

    x = 5
    y = 351
    global_var.magnet_info.append(x)
    global_var.magnet_info.append(y)
    magnet_obj = Magnet(x,y)
    magnet_obj.put_in_grid(magnet_obj.height, magnet_obj.width, magnet_obj.matrix,grid,type)