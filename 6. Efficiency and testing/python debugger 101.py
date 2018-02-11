'''
 Some Commmands :
 next : for next line execution (only sticks to current context; i.e don't enter the function)
 continue : to continue the program
 step : for next step by step line execution including passing to other frames/context i.e enters the functions
 help : list all available commands
'''

import pdb

sum = 0

for i in range(1, 10):
    sum += 1
    pdb.set_trace()
