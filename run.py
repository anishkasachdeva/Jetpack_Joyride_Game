from initial import Initial

import tty
import sys
import termios


# indices_list_row = []
# indices_list_column = []


game = Initial()
''' back is the instance of the class Background in background.py file'''

if __name__ == '__main__':
    game.run()

#     game.welcome_msg()
#     ''' Calling welcome_msg() function of the class Background on the instance 'back' '''

#     game.make_numpygrid()
#     ''' Calling make_numpygrid() function of the class Background on the instance 'back' to make the 2d grid for the background'''

#     back.fit_in_objects()
# while True:
#     orig_settings = termios.tcgetattr(sys.stdin)

#     tty.setcbreak(sys.stdin)
#     x = 0
#     x = sys.stdin.read(1)[0]
#     if x == chr(97): # ESC
#         print("You pressed", x)
#     elif x == chr(100):
#         print("You pressed", x)
#     elif x == chr(119):
#         print("You pressed", x)

#     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)