from colorama import Fore, Back, Style
from person import Mando
import numpy as np
import time
import os
import random

class Background():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = np.zeros((self.height,self.width),dtype='<U20')
        self.grid[:] = ' '

        ''' making road'''
        self.grid[height - 5 : height - 4 , :] = Back.BLACK + Fore.YELLOW + '-' + Fore.RESET + Style.RESET_ALL
        self.grid[height - 4 : height , :] = Back.YELLOW + Fore.YELLOW + '_' + Fore.RESET + Style.RESET_ALL
        self.grid[height - 4 : height , ::5] = Back.BLACK + Fore.RED + '|' + Fore.RESET + Style.RESET_ALL

        '''making upper sky'''

        self.grid[1:2 , :] = Back.BLUE + Fore.WHITE + '-' + Fore.RESET + Style.RESET_ALL

        
    def Power_Booster(self):
        power_booster = np.zeros((1,1),dtype='<U20')
        power_booster[:] = ' '
        self.grid[28:29 , 91:92] = Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL
        self.grid[24:25 , 195:196] = Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL
        self.grid[30:31 , 400:401] = Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL
        self.grid[28:29 , 355:356] = Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL
        self.grid[28:29 , 450:451] = Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL
        self.grid[24:25 , 550:551] = Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL
        self.grid[30:31 , 600:601] = Back.BLUE + Fore.WHITE + 'P' + Fore.RESET + Style.RESET_ALL