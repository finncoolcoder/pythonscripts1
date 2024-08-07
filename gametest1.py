import random
import time
import webbrowser
from art import tprint  # Ensure `tprint` is imported from `art`

print('Put this window in fullscreen')
x1 = 5
for i in range(5):
    print(str(x1 - i))
    time.sleep(1)

tprint('Stardew Valley \n Text Edition')
time.sleep(2)

def menu():
    print('MENU:')
    print('1: Create a new save.')
    print('2: Load an existing save')
    print('3: About, copyright etc. (boring stuff)')
    print('4: The debug version')

def handle_menu():
    while True:
        menu()
        option = input('\n> ')
        if option == '4':
            break  # Exit the loop if option 4 is selected

handle_menu()

print('You have passed')
print('Welcome to Stardew Valley.')
print('Please create a character.')

name = input('What is your name? > ')
age = int(input('How old are you? '))
favorite_thing = input('What is your favorite thing? ')
pet12 = int(input('1 for cat, 2 for dog > '))

if pet12 == 1:
    pet = 'cat'
elif pet12 == 2:
    pet = 'dog'
else:
    pet = input('What pet? > ')

print('This is your information; no, you cannot change it.')
print(f'Name: {name}, Age: {age}, Favorite Thing: {favorite_thing}, Pet: {pet}')

tprint("Let's go!")
time.sleep(2)

print('You are about to start a bad quality port of a really good game.')
print('Stardew Valley: The Text Edition, like the original, was created by a solo developer.')
time.sleep(2)
print('If you would like to donate, please send me an email.')
print('Just send a photo of your passport along with your SSN and credit card info.')
time.sleep(2)
print('Okay seriously though, let\'s start.')
print('You (yes you) are a farmer. \nYou must make money.')
print('Run the command /farm to get started.')

ask2 = input('> ')

def farm():
    global turnips, turnips_per_second
    turnips = 0
    turnips_per_second = turnips / 4
    print(f'You have {turnips} turnips. Press any key and then enter to plant turnips.')
    input('>')
    time.sleep(random.randint(1, 20))
    turnips += random.randint(1, 300)
    turnips_per_second = turnips / 4
    print(f'You now have {turnips} turnips, producing a total of {turnips_per_second} turnips every second.')

if ask2 == '/farm':
    farm()
else:
    farm()

# Run farming simulation in a loop
try:
    while True:
        turnips += turnips_per_second
        turnips_per_second = turnips / 4
        print(f'Turnips: {turnips}')
        time.sleep(0.9)
except KeyboardInterrupt:
    print('Exiting the farming simulation.')
