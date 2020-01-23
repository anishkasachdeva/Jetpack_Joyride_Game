from colorama import Fore, Back, Style
from background import Background
from person import Mando
from alarmexception import AlarmException
from getch import _getChUnix as getChar
import numpy as np
import time
import os
import signal
import tty
import sys
import termios


class Obstacles:
    def __init__(self,row,column):
        self.row = row
        self.column = column

    def put_in_grid(self,height,width,matrix, grid,type):
            grid [self.row : self.row + height , self.column : self.column + width ] = matrix


class Coins(Obstacles):
    def __init__(self,row,column):
        super().__init__(row,column)

        self.height = 3
        self.width = 10
        self.matrix = np.zeros((self.height,self.width),dtype='<U20')
        self.matrix[:] = ' '
        self.matrix [0:3 , 0:10] = Fore.YELLOW + '$' + Fore.RESET


class Obstacles_horizontal(Obstacles):
    def __init__(self,row,column):
        super().__init__(row,column)

        self.height = 1
        self.width = 8
        self.matrix = np.zeros((self.height,self.width),dtype='<U20')
        self.matrix[:] = ' '
        self.matrix[0:1 , 0:8] = Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL


class Obstacles_vertical(Obstacles):
    def __init__(self,row,column):
        super().__init__(row,column)

        self.height = 8
        self.width = 1
        self.matrix = np.zeros((self.height,self.width),dtype='<U20')
        self.matrix[:] = ' '
        self.matrix[0:8 , 0:1] = Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL


class Obstacles_slanting(Obstacles):
    def __init__(self,row,column):
        super().__init__(row,column)

        self.height = 8
        self.width = 8
        self.matrix = np.zeros((self.height,self.width),dtype='<U20')
        self.matrix[:] = ' '
        for i in range(8):
            for j in range(i):
                if i == j:
                    self.matrix[i:i+1 , j:j+1] = Back.RED + Fore.BLACK + '*' + Fore.RESET + Style.RESET_ALL


class Enemy(Obstacles):
    def __init__(self,row,column):
        super().__init__(row,column)

        self.height = 3
        self.width = 5
        self.matrix = np.zeros((self.height,self.width),dtype='<U20')
        self.matrix[:] = ' '
        self.matrix[0:1 , 0:5] = Back.RED + Fore.BLACK + '~' + Fore.RESET + Style.RESET_ALL
        self.matrix[1:2 , 2:3] = Back.RED + Fore.BLACK + '~' + Fore.RESET + Style.RESET_ALL
        self.matrix[2:3 , 1:2] = Back.RED + Fore.BLACK + '~' + Fore.RESET + Style.RESET_ALL
        self.matrix[2:3 , 3:4] = Back.RED + Fore.BLACK + '~' + Fore.RESET + Style.RESET_ALL

class Magnet(Obstacles):
    def __init__(self,row,column):
        super().__init__(row,column)

        self.height = 5
        self.width = 8
        self.matrix = np.zeros((self.height,self.width),dtype='<U20')
        self.matrix[:] = ' '
        self.matrix[0:2 , 0:8] = Fore.GREEN + '+' + Fore.RESET
        self.matrix[2:3 , 0:2] = Fore.GREEN + '+' + Fore.RESET
        self.matrix[2:3 , 6:8] = Fore.GREEN + '+' + Fore.RESET
        self.matrix[3:4 , 0:2] = Fore.GREEN + '+' + Fore.RESET
        self.matrix[3:4 , 6:8] = Fore.GREEN + '+' + Fore.RESET
        self.matrix[4:5 , 0:2] = Fore.GREEN + '+' + Fore.RESET
        self.matrix[4:5 , 6:8] = Fore.GREEN + '+' + Fore.RESET
        
        