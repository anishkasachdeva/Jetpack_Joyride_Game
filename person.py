'''Person Class Definition'''
import global_var

from colorama import Fore, Back, Style
import numpy as np
import time
import os
import signal
import tty
import sys
import termios


class Person:

    def __init__(self, x, y, height, width, dx, dy):
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width = width
        self.__dx = dx
        self.__dy = dy
        self.matrix1 = np.zeros((self.__height,self.__width),dtype='<U20')
        self.matrix1[:] = ' '

        self.matrix2 = np.zeros((self.__height,self.__width),dtype='<U20')
        self.matrix2[:] = ' '

    def get_matrix1(self):
        '''Function to return the matrix
        representation of the person
        '''
        return self.matrix1

    def get_matrix2(self):
        '''Function to return the matrix
        representation of the person
        '''
        return self.matrix2

    def place_space(self):
        pass
    

class Mando(Person):
    '''Class to define the main player of the game.
    Initilized Mandalorian with its size, matrix
    '''

    def __init__(self, x, y, height, width, dx, dy):
        super().__init__(x, y, height, width, dx, dy)
        self.__height = 3
        self.__width = 4
        self.__dx = 2
        self.__dy = -1
        self.__coins = 0
        self.__lives = 3
        self.__shield_mode = False
        self.__score = 0
        # self.grid = Background(40,1000)
        self.matrix1[0:1 , 0:1] = '('
        self.matrix1[0:1 , 1:3] = '\''
        self.matrix1[0:1 , 3:4] = ')' 
        self.matrix1[1:2 , 0:1] = '/'
        self.matrix1[1:2 , 1:3] = 'I'
        self.matrix1[1:2 , 3:4] = '\\'
        self.matrix1[2:3 , 0:1] = ' '
        self.matrix1[2:3 , 1:3] = 'I'
        self.matrix1[2:3 , 3:4] = ' ' 


        self.matrix2[0:1 , 0:1] = Fore.GREEN + '(' + Fore.RESET
        self.matrix2[0:1 , 1:3] = Fore.GREEN + '\'' + Fore.RESET
        self.matrix2[0:1 , 3:4] = Fore.GREEN + ')' + Fore.RESET
        self.matrix2[1:2 , 0:1] = Fore.GREEN + '/' + Fore.RESET
        self.matrix2[1:2 , 1:3] = Fore.GREEN + 'I' + Fore.RESET
        self.matrix2[1:2 , 3:4] = Fore.GREEN + '\\' + Fore.RESET
        self.matrix2[2:3 , 0:1] = Fore.GREEN + ' ' + Fore.RESET
        self.matrix2[2:3 , 1:3] = Fore.GREEN + 'I' + Fore.RESET
        self.matrix2[2:3 , 3:4] = Fore.GREEN + ' ' + Fore.RESET 

        self.__start_column = 3
        self.__start_row = 32

        # self.matrix = np.array([
        #                 ['(','\'','\'',')'],
        #                 ['/','I','I','\\'],
        #                 [' ','I','I',' '],
        #              ])


    def get_dx(self):
        return self.__dx

    def modify_dx(self,value):
        self.__dx = value
    def get_score(self):
        return self.__score
    
    def modify_score(self):
        self.__score += self.__coins * 5 + 10

    def get_height(self):
        return self.__height

    def get_start_row(self):
        return self.__start_row

    def modify_start_row_add(self,value):
        self.__start_row += value

    def modify_start_row_assign(self,value):
        self.__start_row = value


    def get_start_column(self):
        return self.__start_column
    
    def modify_start_column_add(self):
        self.__start_column += self.__dx

    def modify_start_column_minus(self):
        self.__start_column -= self.__dx

    def get_coins(self):
        return self.__coins

    def get_lives(self):
        return self.__lives
    
    def modify_lives(self,value):
        self.__lives -= value

    def get_shield_mode(self):
        return self.__shield_mode
    
    def modify_shield_mode(self,value):
        self.__shield_mode = value

    def put_in_mando(self,grid_matrix,matrix):
        grid_matrix[self.__start_row:self.__start_row + self.__height, self.__start_column : self.__start_column + self.__width] = matrix

    def move_left(self,curr_startcol,value):
        self.__start_column -= self.__dx
        if self.__start_column <= curr_startcol:
                self.__start_column = curr_startcol + value

    def move_right(self,curr_lastcol):
        self.__start_column += self.__dx
        if self.__start_column >= curr_lastcol:
            self.__start_column = self.__dx


    def move_up_change(self):
        self.__start_row -= self.__dx
        if self.__start_column + 3 >= global_var.curr_lastcol:
            self.__start_column = global_var.curr_lastcol - 65 - 4
        else:
            self.__start_column += self.__dx

    def move_up(self):
    
        self.__start_row -= self.__dx
        self.__start_column += self.__dx

    def check_gravity(self,height,gravity_time,grid):
        distance = round(0.5 * 1 * gravity_time * gravity_time)
        if distance == 0:
            distance = 1
        if self.__start_row + distance <= 32:
            self.__start_row += distance
        else: 
            self.__start_row = 32

    def move_down(self,curr_lastcol):
        self.__start_row = self.__start_row + self.__dx
        self.__start_column = self.__start_column + self.__dx
        if self.__start_column >= curr_lastcol:
            self.__start_column -= self.__dx

    def move_random(self,curr_lastcol):
        # if global_var.power_booster == 0
        self.__start_column = self.__start_column + self.__dx
        if self.__start_column >= curr_lastcol:
            self.__start_column -= self.__dx
        # else:
        # self.__start_column = self.__start_column + 4
        # if self.__start_column >= curr_lastcol:
        #     self.__start_column -= 4


    def place_space(self,grid):
        grid[self.__start_row : self.__start_row + self.__height , self.__start_column : self.__start_column + self.__width] = ' '

    def check_collision(self,grid):

        index = 0
        exist = 0
        shield_used = 0
        for i in range(self.__start_row, self.__start_row + self.__height):
            for j in range(self.__start_column,self.__start_column + self.__width):
                if grid[i][j] == Fore.YELLOW + '$' + Fore.RESET:
                    self.__coins += 1;
                if grid[i][j] == Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL:
                    self.__dx = 4
                    global_var.power_booster
                    global_var.diff = 4
                    start_of_power_booster = time.time()
                    # global_var.screen_movement = 0.22

                if self.__shield_mode == False:
                    if grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL or grid[i][j] ==  '<':
                        exist = 1
                        self.__start_row = 32
                        self.__start_column = 3
                        self.__lives -= 1
                        if self.__dx == 4:
                            self.__dx = 2
                        break
                if self.__shield_mode == True:
                    if grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL  or grid[i][j] == Back.RED + Fore.BLACK + '~' + Fore.RESET + Style.RESET_ALL:
                        shield_used = 1
                        global_var.index = j
                        self.__shield_mode = False
                        break

            if exist == 1 or shield_used == 1:
                break
        if exist == 0:
            return 0
        if exist == 1:
            return 1
        if shield_used == 1:
            return 2


    def check_magnet_attraction(self,grid):
        if self.__start_column + 30 >= global_var.magnet_info[1]   and self.__start_column < global_var.magnet_info[1]:
            global_var.magnet_flag = True
            
            self.move_right(global_var.curr_lastcol)

            if(self.__start_row > 4):
                self.__start_row -= self.__dx
            else:
                self.__start_row = 2

        elif self.__start_column - 30 <= global_var.magnet_info[1] and self.__start_column >= global_var.magnet_info[1]:
            global_var.magnet_flag = True

            self.__start_column -= 1
            if self.__start_column <= global_var.curr_startcol:
                self.__start_column = global_var.curr_startcol + 2


            if(self.__start_row > 4):           
                self.__start_row -= self.__dx
            else:
                self.__start_row = 2
        else:
            global_var.magnet_flag = False




class Enemy(Person):
    def __init__(self, x, y, height, width, dx, dy):
        super().__init__(x, y, height, width, dx, dy)

        self.mando = Mando(0, 40 - 8,3, 4, 2, -1)
        self.__height = 10
        self.__width = 54
        self.__top_of_enemy = 25
        self.__bottom_of_enemy = self.__top_of_enemy + self.__height
        self.__lives = 5
        self.__dx = 2
        self.matrix1 = np.array(
                                [list("                          __,----'~~~~~~~~~`-----.__  "),
                                list("               .  .     //====-              ____,-'~`"),
                                list("              \_|// .   /||\\\  `~~~~`---.___./        "), 
                                list("           _-~'  `\/    |||  \\\           _,'`        "),
                                list("         ;_,_,/ _-'|-   |`\   \\\        ,'            "),
                                list("           '',/~7  /-   /  ||   `\.     /             "),  
                                list("            '  /  /-   /   ||      \   /              "),
                                list("             /  /|- _/   ,||       \ /                "), 
                                list("            /  `| \\'--===-'       _/`                 "),   
                                list("          /|____)-'\~'______,--''                     ")]
                                )

    def get_lives(self):
        return self.__lives
    
    def modify_lives(self,value):
        self.__lives -= value

    def get_height(self):
        return self.__height

    def get_top_of_enemy(self):
        return self.__top_of_enemy

    def get_dx(self):
        return self.__dx

    # def modify_top_of_enemy(self,value):
    #     self.__top_of_enemy 

    def modify_top_of_enemy_down(self):
        if self.__top_of_enemy <= 23:
            self.__top_of_enemy += self.__dx
        else:
            self.__top_of_enemy = 25

    def modify_top_of_enemy_up(self):
        if self.__top_of_enemy >= 4: 
            self.__top_of_enemy -= self.__dx
        else:
            self.__top_of_enemy = 2
        # self.__top_of_enemy -= self.__dx


    # def place_space(self,grid_width,grid):
    #     for i in range(self.__height):
    #         grid[self.__top_of_enemy + i : self.__top_of_enemy + i + 1, grid_width - 56 : grid_width - 2] = ' '

    def place_space(self,grid_width,grid):
        for i in range(3,35):
            for j in range(grid_width - 65,grid_width - 2, 1):
                grid[i][j] = ' '

    def put_in_boss_enemy(self,grid_width,grid):
        
        for i in range(self.__height):
            grid[self.__top_of_enemy + i : self.__top_of_enemy + i + 1, grid_width - 56 : grid_width - 2] = self.matrix1[i]


    def release_bullets(self,grid_width,grid,mando_start_row):
        global_var.dragon_releases_bullet
        hit = 0
        global_var.time_for_dragon_bullet = time.time()
        global_var.dragon_releases_bullet = 1

        if self.__top_of_enemy + 5 >= mando_start_row and self.__top_of_enemy + 5 <= mando_start_row + 3:
            hit = 1

        for i in range(65,95,1):
            grid[self.__top_of_enemy + 5][grid_width - i] = '<'
            grid[self.__top_of_enemy + 6][grid_width - i] = '<'
        if hit == 1:
            return 1
        else:
            return 0

    def check_collision_with_boss_enemy(self,grid_width,grid):
        for i in range(self.__top_of_enemy,self.__height):
            for j in range(grid_width - 56, grid_width - 2):
                if grid[i][j] == 'o':
                    self.__lives -= 1