import random
import time
from art import *
print('put this window in fullscreen')
x1=5
print(str(x1))
#time.sleep(1)
print(str(x1-1))
#time.sleep(1)
print(str(x1-2))
#time.sleep(1)
print(str(x1-3))
#time.sleep(1)
print(str(x1-4))
#time.sleep(1)

tprint('Stardew Valley \n text edtion')
def menu():
    print('MENU:')
    print(' 1: create a new save. \n 2: Load an existing save\n 3:About, copyright etc. (boring stuff) \n 4: THe debug version')

    
menu()
option1=input('\n >')

if option1 == '4':
    pass
else:
    menu()

print('you have passed')