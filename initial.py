from background import Background
from obstacles import Magnet
from person import Mando, Enemy
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from generate_coordinates import Generate_coordinates
import global_var
import random
from colorama import Fore, Back, Style
import numpy as np
import time
import os
import signal
import tty
import sys
import termios


def print_grid(height,width,cols,new_cols,grid , lives, coins,shield_mode,score,dragon_lives,time):
    for i in range(global_var.curr_lastcol):
        grid[0][i] = Back.RED + ' ' + Style.RESET_ALL
    grid[1:2 , :] = Back.BLUE + Fore.WHITE + '-' + Fore.RESET + Style.RESET_ALL
    for i in range(height):
        for j in range(cols,new_cols):
            if j == cols:
                global_var.curr_startcol = j
                grid[0][global_var.curr_startcol + 0] = Back.RED + Fore.WHITE + 'L' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 1] = Back.RED + Fore.WHITE + 'I' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 2] = Back.RED + Fore.WHITE + 'V' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 3] = Back.RED + Fore.WHITE + 'E' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 4] = Back.RED + Fore.WHITE + 'S' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 6] = lives
                

                grid[0][global_var.curr_startcol + 20] = Back.RED + Fore.WHITE + 'S' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 21] = Back.RED + Fore.WHITE + 'C' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 22] = Back.RED + Fore.WHITE + 'O' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 23] = Back.RED + Fore.WHITE + 'R' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 24] = Back.RED + Fore.WHITE + 'E' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 26] = score


                grid[0][global_var.curr_startcol + 40] = Back.RED + Fore.WHITE + 'T' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 41] = Back.RED + Fore.WHITE + 'I' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 42] = Back.RED + Fore.WHITE + 'M' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 43] = Back.RED + Fore.WHITE + 'E' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 45] = time


                grid[0][global_var.curr_startcol + 59] = Back.RED + Fore.WHITE + 'C' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 60] = Back.RED + Fore.WHITE + 'O' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 61] = Back.RED + Fore.WHITE + 'I' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 62] = Back.RED + Fore.WHITE + 'N' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 63] = Back.RED + Fore.WHITE + 'S' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 65] = coins

                grid[0][global_var.curr_startcol + 79] = Back.RED + Fore.WHITE + 'S' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 80] = Back.RED + Fore.WHITE + 'H' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 81] = Back.RED + Fore.WHITE + 'I' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 82] = Back.RED + Fore.WHITE + 'E' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 83] = Back.RED + Fore.WHITE + 'L' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 84] = Back.RED + Fore.WHITE + 'D' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 86] = shield_mode

                grid[0][global_var.curr_startcol + 100] = Back.RED + Fore.WHITE + 'D' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 101] = Back.RED + Fore.WHITE + '_' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 102] = Back.RED + Fore.WHITE + 'L' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 103] = Back.RED + Fore.WHITE + 'I' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 104] = Back.RED + Fore.WHITE + 'V' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 105] = Back.RED + Fore.WHITE + 'E' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 106] = Back.RED + Fore.WHITE + 'S' + Fore.RESET + Style.RESET_ALL
                grid[0][global_var.curr_startcol + 108] = dragon_lives                             
            global_var.curr_lastcol = j
            print(grid[i][j], end = '')
        print()
        
    return [global_var.curr_startcol,global_var.curr_lastcol] 


class Initial:
    def __init__(self):
        self.grid = Background(40,1000)
        Generate_coordinates(self.grid.height, self.grid.width, self.grid.grid)
        self.magnet_obj = Magnet(global_var.magnet_info[0],global_var.magnet_info[1])
        self.grid.Power_Booster()
        self.mando = Mando(0, self.grid.height - 8,3, 4, 2, -1)
        self.enemy = Enemy(0, self.grid.height - 8, 10, 54, 2, 2)
        self.cols = 0
        self.new_cols = 150
        self.indices_list_row = []
        self.indices_list_column = []
        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)

        def get_cols(self):
            return self.cols
        def modify_cols(self,value):
            self.col = self.col + value

        def get_new_cols(self):
            return self.new_cols
        def modify_new_cols(self,value):
            self.new_cols = self.new_cols + value

        def get_indices_list_row(self):   
            return self.indices_list_row    
        def modify_indices_list_row(self,l_list):
            self.indices_list_row = self.indices_list_row + l_list

        def get_indices_list_column(self):   
            return self.indices_list_column    
        def modify_indices_list_column(self):
            self.indices_list_column = self.indices_list_column + l_list
             


    def run(self):
        previous_time_of_shield = 0
        start_time_of_shield = 0
        Finish = True
        shield_used = 0
        original_time = time.time()
        
        shield_mode = self.mando.get_shield_mode()
        coins = self.mando.get_coins()
        lives = self.mando.get_lives()
        score = self.mando.get_score()
        dragon_lives = self.enemy.get_lives()
        self.mando.modify_score()
        list_of_first_and_last_column = print_grid(self.grid.height,self.grid.width,self.cols,self.new_cols,self.grid.grid,lives,coins, shield_mode,score,dragon_lives,global_var.time_left)
        global_var.curr_startcol = list_of_first_and_last_column[0]
        global_var.curr_lastcol = list_of_first_and_last_column[1]

        original_time = time.time()
        lives = self.mando.get_lives()

        while True:
            global_var.while_value = 1

            global_var.recent_time = time.time()
            global_var.time_left = 300 - round(global_var.recent_time - global_var.overall_time)
            self.magnet_obj.put_in_grid(self.magnet_obj.height, self.magnet_obj.width, self.magnet_obj.matrix,self.grid.grid,1)
            
            score = self.mando.get_score()
            self.mando.modify_score()
            start_row = self.mando.get_start_row()
            if global_var.curr_startcol >= self.grid.width - 150 :
                break

            print('\033[0;0H')
            end_time = time.time()
            if end_time - original_time >= 0.15:
                self.cols += global_var.diff
                self.new_cols += global_var.diff

                shield_mode = self.mando.get_shield_mode()
                coins = self.mando.get_coins()
                lives = self.mando.get_lives()
                if lives == 0 or Finish == False or global_var.time_left == 0:
                    os.system('clear')
                    for i in range(2):
                        print()
                    if(Finish == False):
                        print("Game Quit!")
                        print()
                    if(lives == 0):
                        print("Mando Died!")
                        print()
                    if(global_var.time_left == 0):
                        print("Time Over!")
                        print()
                    print("Final Score is: ", score)
                    print()
                    sys.exit()
                

                dragon_lives = self.enemy.get_lives()
                list_of_first_and_last_column = print_grid(self.grid.height,self.grid.width,self.cols,self.new_cols,self.grid.grid,lives,coins,shield_mode,score,dragon_lives,global_var.time_left)
                global_var.curr_startcol = list_of_first_and_last_column[0]
                global_var.curr_lastcol = list_of_first_and_last_column[1]
                original_time = time.time()

            def alarmhandler(signum, frame):
                raise AlarmException
            
            def user_input(timeout=0.15):
                # ''' input method '''
                signal.signal(signal.SIGALRM, alarmhandler)
                signal.setitimer(signal.ITIMER_REAL, timeout)
                try:
                    text = getChar()()
                    signal.alarm(0)
                    return text
                except AlarmException:
                    pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''

            x = user_input()

            exist = 0
            # bullet_hit = 0
            start_row = self.mando.get_start_row()


            if global_var.power_booster == 1:
                if time.time() - global_var.start_of_power_booster >= 10:
                    global_var.power_booster = 0
                    global_var.power_booster == 1
                    get_dx = self.mando.get_dx()
                    global_var.diff = 2
                    self.mando.modify_dx(2)
                    # global_var.screen_movement = 0.15 

            if (time.time() - start_time_of_shield >= 10):
                shield_mode = self.mando.get_shield_mode()
                self.mando.modify_shield_mode(False)
            if global_var.bullet_hit == 1:
                global_var.bullet_hit = 0
            elif global_var.bullet_hit == 0 :
                for i in range(self.grid.height):
                    for j in range(self.grid.width):
                        if self.grid.grid[i][j] == 'o':
                            self.grid.grid[i][j] = ' '
    
            if x is not None:
                if x == "a":
                    self.mando.place_space(self.grid.grid)
                    self.mando.move_left(global_var.curr_startcol,2)
                    self.mando.check_magnet_attraction(self.grid.grid)
                    ret_value = self.mando.check_collision(self.grid.grid)
                    if ret_value == 0:
                        shield_mode = self.mando.get_shield_mode()
                        if shield_mode == False:
                            self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                        else:
                            self.mando.put_in_mando(self.grid.grid,self.mando.matrix2)
                    if ret_value == 1:
                        # print("rtyuiougyhjk")
                        self.cols = -2
                        self.new_cols = 150
                        self.grid = Background(self.grid.height, self.grid.width)
                        Generate_coordinates(self.grid.height, self.grid.width, self.grid.grid)
                        self.grid.Power_Booster()
                        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
                        time.sleep(0.35)
                    if ret_value == 2:
                        # print("hiiiiiiiiiiii")
                        for i in range(self.grid.height):
                            # print("hiiiiiiiiiiii")
                            for j in range(global_var.index - 20 , global_var.index + 20 , 1):
                                if self.grid.grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                    self.grid.grid[i][j] = ' '
                    

                elif x == "d":
                    self.mando.place_space(self.grid.grid)
                    self.mando.move_right(global_var.curr_lastcol)
                    self.mando.check_magnet_attraction(self.grid.grid)
                    ret_value = self.mando.check_collision(self.grid.grid)

                    if ret_value == 0:
                        shield_mode = self.mando.get_shield_mode()
                        if shield_mode == False:
                            self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                        else:
                            self.mando.put_in_mando(self.grid.grid,self.mando.matrix2)
                    if ret_value == 1:
                        # print("rtyuiougyhjk")
                        self.cols = 0
                        self.new_cols = 150
                        self.grid = Background(self.grid.height, self.grid.width)
                        Generate_coordinates(self.grid.height, self.grid.width, self.grid.grid)
                        self.grid.Power_Booster()
                        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
                        time.sleep(0.35)
                    if ret_value == 2:
                        # print("hiiiiiiiiiiii")
                        for i in range(self.grid.height):
                            # print("hiiiiiiiiiiii")
                            for j in range(global_var.index - 20 , global_var.index + 20 , 1):
                                if self.grid.grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                    self.grid.grid[i][j] = ' '


                elif x == "w":
                    global_var.gravity_time = 0
                    start_row = self.mando.get_start_row()
                    start_column = self.mando.get_start_column()
                    if start_row > 4:
                        self.mando.place_space(self.grid.grid)
                        self.mando.move_up()
                        if start_column >= global_var.curr_lastcol:
                            self.mando.modify_start_column_minus()

                        self.mando.check_magnet_attraction(self.grid.grid)
                        start_row = self.mando.get_start_row()
                        # score = self.mando.get_score()
                        mando_height = self.mando.get_height()
                        top_of_enemy = self.enemy.get_top_of_enemy()
                        enemy_height = self.enemy.get_height()
                        enemy_dx = self.enemy.get_dx()

                        if start_row +  mando_height > top_of_enemy + enemy_height and top_of_enemy < 25:
                            self.enemy.place_space(self.grid.width,self.grid.grid)
                        # if top_of_enemy + enemy_dx <=25:
                            self.enemy.modify_top_of_enemy_down()
                            # top_of_enemy = top_of_enemy + enemy_dx
                        # else:
                            # self.top.enemy = 25

                        if start_row <= top_of_enemy:
                            self.enemy.place_space(self.grid.width,self.grid.grid)
                        # if top_of_enemy - enemy_dx >= 3:
                            self.enemy.modify_top_of_enemy_up()
                            # top_of_enemy = top_of_enemy - enemy_dx
                        # else:
                            # self.__top_of_enemy = 3
                        
                        if start_row == 32 and top_of_enemy < 25:
                            self.enemy.modify_top_of_enemy_down()

                        # self.enemy.move_boss_enemy(self.grid.width,self.grid.grid)
                        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
                        ret_value = self.mando.check_collision(self.grid.grid)
                        if ret_value == 0:
                            shield_mode = self.mando.get_shield_mode()
                            if shield_mode == False:
                                self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                            else:
                                self.mando.put_in_mando(self.grid.grid,self.mando.matrix2)
                        if ret_value == 1:
                            # print("rtyuiougyhjk")
                            self.cols = 0
                            self.new_cols = 150
                            self.grid = Background(self.grid.height, self.grid.width)
                            Generate_coordinates(self.grid.height, self.grid.width, self.grid.grid)
                            self.grid.Power_Booster()
                            self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                            self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
                            time.sleep(0.35)
                        if ret_value == 2:
                            # print("hiiiiiiiiiiii")
                            for i in range(self.grid.height):
                                # print("hiiiiiiiiiiii")
                                for j in range(global_var.index - 20 , global_var.index + 20 , 1):
                                    if self.grid.grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                        self.grid.grid[i][j] = ' '
                    else:
                        self.mando.place_space(self.grid.grid)
                        self.mando.get_start_row()
                        self.mando.modify_start_row_assign(2)
                        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)


                elif x == "s":
                    if (time.time() - previous_time_of_shield >= 60):
                        shield_mode = self.mando.get_shield_mode()
                        self.mando.modify_shield_mode(True)
                        previous_time_of_shield = time.time()
                        start_time_of_shield = time.time()
                    else:
                        shield_mode = self.mando.get_shield_mode()
                        self.mando.modify_shield_mode(False)
                        


                elif x == "q":
                    # quit()
                    # os.system('clear')
                    # print("Game Quit!")
                    # print()
                    Finish = False



                elif x == "b":
                    global_var.bullet_hit = 1
                    self.mando.place_space(self.grid.grid)
                    start_column = self.mando.get_start_column()
                    start_row = self.mando.get_start_row()
                    self.mando.modify_start_column_add()
                
                    temp_col = global_var.curr_lastcol
                    for i in range(start_row,start_row + 3):
                        for j in range(start_column,temp_col,1):
                            if self.grid.grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                exist = 1
                                begin_col = j;
                                break
                        if exist == 1:
                            break
                    if exist == 1:
                        start_time_of_bullet = time.time()
                        begin_bullet = start_column + 20
                    else:
                        begin_bullet = start_column + 20
                        begin_col = start_column + 15

                    for i in range(0,20,4):
                        self.grid.grid[start_row + 1][begin_bullet + i] = 'o'

                    self.mando.place_space(self.grid.grid)
                    if exist == 1:
                        for i in range(self.grid.height):
                            for j in range(begin_col-10,begin_col + 10):
                                if self.grid.grid[i][j] ==  Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                    self.grid.grid[i][j] = ' '
                                if self.grid.grid[i][j] ==  Back.RED + Fore.BLACK + '~' + Fore.RESET + Style.RESET_ALL:
                                    self.grid.grid[i][j] = ' '
                    self.mando.put_in_mando(self.grid.grid,self.mando.matrix1) 



                else:
                    self.mando.place_space(self.grid.grid)
                    self.mando.move_random(global_var.curr_lastcol)
                    start_row = self.mando.get_start_row()
                    if start_row < 32:
                        if global_var.magnet_flag == False:
                            global_var.gravity_time += 0.2
                            self.mando.check_gravity(self.grid.height,global_var.gravity_time,self.grid.grid)
                    
                        start_row = self.mando.get_start_row()
                        # score = self.mando.get_score()
                        mando_height = self.mando.get_height()
                        top_of_enemy = self.enemy.get_top_of_enemy()
                        enemy_height = self.enemy.get_height()
                        enemy_dx = self.enemy.get_dx()

                        if start_row +  mando_height > top_of_enemy + enemy_height and top_of_enemy < 25:
                            self.enemy.place_space(self.grid.width,self.grid.grid)
                            self.enemy.modify_top_of_enemy_down()
                           

                        if start_row <= top_of_enemy:
                            self.enemy.place_space(self.grid.width,self.grid.grid)
                            self.enemy.modify_top_of_enemy_up()


                        if start_row == 32 and top_of_enemy < 25:
                            self.enemy.modify_top_of_enemy_down()

                    start_row = self.mando.get_start_row()
                    if start_row >= 2:
                        self.mando.check_magnet_attraction(self.grid.grid)
                        ret_value = self.mando.check_collision(self.grid.grid)
                        if ret_value == 0:
                            shield_mode = self.mando.get_shield_mode()
                            if shield_mode == False:
                                self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                            else:
                                self.mando.put_in_mando(self.grid.grid,self.mando.matrix2)
                        if ret_value == 1:
                            # print("rtyuiougyhjk")
                            self.cols = 0
                            self.new_cols = 150
                            self.grid = Background(self.grid.height, self.grid.width)
                            Generate_coordinates(self.grid.height, self.grid.width, self.grid.grid)
                            self.grid.Power_Booster()
                            self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                            self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
                            time.sleep(0.35)
                        if ret_value == 2:
                            # print("hiiiiiiiiiiii")
                            for i in range(self.grid.height):
                                # print("hiiiiiiiiiiii")
                                for j in range(global_var.index - 20 , global_var.index + 20 , 1):
                                    if self.grid.grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                        self.grid.grid[i][j] = ' '
                    else:
                        start_row = self.mando.get_start_row()
                        self.mando.modify_start_row_add(2)
                        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)

        mando_lives = self.mando.get_lives()
        enemy_lives = self.enemy.get_lives()
        Finish = True


        while True:
            global_var.while_value = 2
            global_var.recent_time = time.time()
            global_var.time_left = 300 - round(global_var.recent_time - global_var.overall_time)
            score = self.mando.get_score()
            self.mando.modify_score()
            start_row = self.mando.get_start_row()

            print('\033[0;0H')
            
            coins = self.mando.get_coins()
            lives = self.mando.get_lives()
            dragon_lives = self.enemy.get_lives()
            if lives == 0 or dragon_lives == 0 or Finish == False or global_var.time_left == 0:
                os.system('clear')
                for i in range(2):
                        print()
                if(Finish == False):
                    print("Game Quit!")
                    print()
                if(lives == 0):
                    print("Mando Died!")
                    print()
                if(dragon_lives == 0):
                    print("Dragon Died!")
                    print()
                if(global_var.time_left == 0):
                    print("Time Over!")
                    print()
                print("Final Score is: ", score)
                print()
                sys.exit()
            list_of_first_and_last_column = print_grid(self.grid.height,self.grid.width,self.cols,self.new_cols,self.grid.grid,lives,coins,shield_mode,score,dragon_lives,global_var.time_left)
            global_var.curr_startcol = list_of_first_and_last_column[0]
            global_var.curr_lastcol = list_of_first_and_last_column[1]
            
            def alarmhandler(signum, frame):
                raise AlarmException
            
            def user_input(timeout=0.15):
                # ''' input method '''
                signal.signal(signal.SIGALRM, alarmhandler)
                signal.setitimer(signal.ITIMER_REAL, timeout)
                try:
                    text = getChar()()
                    signal.alarm(0)
                    return text
                except AlarmException:
                    pass
                signal.signal(signal.SIGALRM, signal.SIG_IGN)
                return ''

            x = user_input()

            start_row = self.mando.get_start_row()
            if time.time() - global_var.time_for_dragon_bullet >= random.randint(2,4):
                hit_value = self.enemy.release_bullets(self.grid.width,self.grid.grid,start_row)
                if hit_value == 1:
                    self.mando.get_lives()
                    self.mando.modify_lives(1)
                else:
                    pass

            if global_var.bullet_hit == 1:
                global_var.bullet_hit = 0
            elif global_var.bullet_hit == 0 :
                for i in range(self.grid.height):
                    for j in range(self.grid.width):
                        if self.grid.grid[i][j] == 'o':
                            self.grid.grid[i][j] = ' '

            
            if global_var.dragon_releases_bullet == 1:
                global_var.dragon_releases_bullet = 0
            elif global_var.dragon_releases_bullet == 0:
                for i in range(self.grid.height):
                    for j in range(self.grid.width):
                        if self.grid.grid[i][j] == '<':
                            self.grid.grid[i][j] = ' '

            if x is not None:
                if x == "a":
                    self.mando.place_space(self.grid.grid)
                    self.mando.move_left(global_var.curr_startcol,2)
                    self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                    self.mando.check_magnet_attraction(self.grid.grid)
                elif x == "d":
                    self.mando.place_space(self.grid.grid)
                    self.mando.move_right(global_var.curr_lastcol - 65)
                    self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                    self.mando.check_magnet_attraction(self.grid.grid)

                elif x == "w":
                    global_var.gravity_time = 0
                    start_row = self.mando.get_start_row()
                    start_column = self.mando.get_start_column()
                    if start_row > 4:
                        self.mando.place_space(self.grid.grid)
                        self.mando.move_up_change()
                        start_row = self.mando.get_start_row()
                        start_column = self.mando.get_start_column()
                        if start_column >= global_var.curr_lastcol:
                            self.mando.modify_start_column_minus()

                        self.mando.check_magnet_attraction(self.grid.grid)
                        start_row = self.mando.get_start_row()
                        mando_height = self.mando.get_height()
                        top_of_enemy = self.enemy.get_top_of_enemy()
                        enemy_height = self.enemy.get_height()
                        enemy_dx = self.enemy.get_dx()
                        if start_row <= top_of_enemy:
                            self.enemy.modify_top_of_enemy_up()
                            self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                            self.enemy.place_space(self.grid.width,self.grid.grid)
                            self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
                    else:
                        self.mando.place_space(self.grid.grid)
                        start_row = self.mando.get_start_row()
                        self.mando.modify_start_row_assign(2)
                        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                        self.enemy.place_space(self.grid.width,self.grid.grid)
                        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)

                elif x == "q":
                    # quit()
                    Finish = False



                elif x == "b":
                    global_var.bullet_hit = 1
                    self.mando.place_space(self.grid.grid)
                    start_column = self.mando.get_start_column()
                    start_row = self.mando.get_start_row()
                    self.mando.modify_start_column_add()
                    temp_col = global_var.curr_lastcol
                    for i in range(start_row,start_row + 3):
                        for j in range(start_column,temp_col,1):
                            if self.grid.grid[i][j] == Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                exist = 1
                                begin_col = j;
                                break
                        if exist == 1:
                            break
                    if exist == 1:
                        start_time_of_bullet = time.time()
                        begin_bullet = start_column + 20
                    else:
                        begin_bullet = start_column + 20
                        begin_col = start_column + 15

                    start_row = self.mando.get_start_row()
                    top_of_enemy = self.enemy.get_top_of_enemy()
                    height_of_enemy = self.enemy.get_height()

                    if start_row + 1 >= top_of_enemy and start_row + 1 <= top_of_enemy + height_of_enemy:
                        lives = self.enemy.get_lives
                        self.enemy.modify_lives(1)


                    for i in range(0,20,4):
                        self.grid.grid[start_row + 1][begin_bullet + i] = 'o'

                    self.mando.place_space(self.grid.grid)
                    if exist == 1:
                        for i in range(self.grid.height):
                            for j in range(begin_col-10,begin_col + 10):
                                if self.grid.grid[i][j] ==  Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL:
                                    self.grid.grid[i][j] = ' '
                                if self.grid.grid[i][j] ==  Back.RED + Fore.BLACK + '~' + Fore.RESET + Style.RESET_ALL:
                                    self.grid.grid[i][j] = ' '
                    self.mando.put_in_mando(self.grid.grid,self.mando.matrix1) 



                else:
                    self.mando.place_space(self.grid.grid)
                    start_row = self.mando.get_start_row()
                    if start_row < 32:
                        global_var.gravity_time += 0.2
                        self.mando.check_gravity(self.grid.height,global_var.gravity_time,self.grid.grid)
                        start_row = self.mando.get_start_row()
                        mando_height = self.mando.get_height()
                        top_of_enemy = self.enemy.get_top_of_enemy()
                        enemy_height = self.enemy.get_height()
                        enemy_dx = self.enemy.get_dx()

                        if start_row +  mando_height > top_of_enemy + enemy_height and top_of_enemy < 25:
                            self.enemy.modify_top_of_enemy_down()
                        self.enemy.place_space(self.grid.width,self.grid.grid)
                        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)

                    start_row = self.mando.get_start_row()
                    if start_row >= 2:
                        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                        self.enemy.place_space(self.grid.width,self.grid.grid)
                        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
                        self.mando.check_magnet_attraction(self.grid.grid)
                    else:
                        start_row = self.mando.get_start_row()
                        self.mando.modify_start_row_add(2)
                        self.mando.put_in_mando(self.grid.grid,self.mando.matrix1)
                        self.enemy.place_space(self.grid.width,self.grid.grid)
                        self.enemy.put_in_boss_enemy(self.grid.width,self.grid.grid)
            mando_height = self.mando.get_height()
            top_of_enemy = self.enemy.get_top_of_enemy()
            enemy_height = self.enemy.get_height()
            enemy_dx = self.enemy.get_dx()
            if start_row == 32 and top_of_enemy < 25:
                self.enemy.modify_top_of_enemy_down()
