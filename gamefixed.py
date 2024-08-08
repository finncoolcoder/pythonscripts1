import random
import time
import webbrowser
from art import tprint  # Ensure `tprint` is imported from `art`

print('Put this window in fullscreen. (There is some ascii art)')
x1 = 5
for i in range(5):
    print(str(x1 - i))
    time.sleep(.4)

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
        elif option == '1':
            import newsave
            break
        elif option =='2':
            from readsave import save
            break
        elif option == '3':
            print('loading information')
            time.sleep(random.randint(1,5))
            print('Stardew valley text edition was created by @finncoolcoder on github. \n if you paid money for this software you were scammed \n do what you like with that information.')
            print('this script is not a 1 to 1 recreation of the original game Stardew valley.\n This is strictly a parody. All original Ideas belong to ConcernedApe and his studio affliates.')
            input()
handle_menu()
from readsave import save
data = save

#unpacks list to variables
age, name, favorite_animal, beard, favorite_color = data


print("Age:", age)
print("Name:", name)
print("Favorite Animal:", favorite_animal)
print("Beard?:", beard)
print("Favorite Color:", favorite_color)
time.sleep(3)
print('You have passed \n \n \n')
print('Welcome to Stardew Valley. \n \n \n \n')


tprint("Let's go!")
time.sleep(2)
print('\n \n \n \n')
print('You are about to start a bad quality port of a really good game. \n')
time.sleep(.5)
print('Stardew Valley: The Text Edition, like the original, was created by a solo developer.')
time.sleep(.5)
print('If you would like to donate, please send me an email.')
time.sleep(.5)
print('Just send a photo of your passport along with your SSN and credit card info.')
time.sleep(2)
print('Okay seriously though, let\'s start.')
time.sleep(.5)
print('You (yes you) are a farmer. \nYou must make money.')
time.sleep(.5)
print('Run the command /farm to get started.')

ask2 = input('> ')
#defines the farming simulation command
#this is currently really broken.
def farm():
    global turnips, turnips_per_second
    turnips = 0
    turnips_per_second = turnips / 4
    print(f'You have {turnips} turnips. Press any key and then enter to plant turnips \n This may take a while.')
    input('>')
    time.sleep(random.randint(1, 20))
    turnips += random.randint(1, 300)
    turnips_per_second = turnips / 4
    print(f'You now have {turnips} turnips, producing a total of {turnips_per_second} turnips every second.')

if ask2 == '/farm':
    farm()
else:
    farm()


try:
    while turnips <999999999999999999999999999999999999999999999999:
        turnips += turnips_per_second*2
        turnips_per_second = turnips / 4
        print(f'Turnips(press ctrl+c to exit): {turnips}')
        time.sleep(0.9)
except KeyboardInterrupt:
    import webbrowser
    webbrowser.open_new_tab('https://youtube.com/@finndolf')
    print('subscribe.')
