import random
import time
from art import *
print('put this window in fullscreen')
x1=5
print(str(x1))
time.sleep(1)
print(str(x1-1))
time.sleep(1)
print(str(x1-2))
time.sleep(1)
print(str(x1-3))
time.sleep(1)
print(str(x1-4))
time.sleep(1)

tprint('Stardew Valley \n text edtion')
time.sleep(2)
def menu():
    print('MENU:')
    print(' 1: create a new save. \n 2: Load an existing save\n 3:About, copyright etc. (boring stuff) \n 4: THe debug version')

    #all this shit is broken!! however it works for my very specific use case.
menu()
option1=input('\n >')

if option1 == '4':
    pass
else:
    menu()

print('you have passed')

print('Welcome to stardew valley.')
print('please create a character.')
name = input('what is your name >')
age = int(input('how old are you?'))
favoritething = input('What is your favorite thing')
pet12 = input('1 for cat 2 for dog')
if pet12 == 1:
    pet='cat'
if pet12 == 2:
    pet='dog'
else:
    pet=input('what pet??/?????????>')


print('this is your information, no you cannot change it.')
print(name + str(age) + favoritething + pet)

tprint("let's go!")
time.sleep(2)
print('you are about to start a bad quality port of a really good game. ')
print('stardew valley the text edition , like the original was created by a solo developer.')
time.sleep(2)
print('If you would like to donate please send me an email and I can reccive cash in the mail.')
print('Just send a photo of your passport along with your SSN and credit card info.')
time.sleep(2)
print('ok seriously though lets start.')
print('You (yes you) are a farmer. \n you must make money.')
print('run the command /farm to get started.')
input = input('>')
def farm():
    print('you are in farming mode')
    turnips=0
    turnipspersecond=turnips/4
    print('you have '+turnips+' turnips, press any key and then enter to plant turnips.')
    input('')
    time.sleep(random.randint(1,20))
    turnips=turnips+random.randint(1,300)
    turnipspersecond=turnips/4
    print('you now have '+ turnips+ ' producing a total of ' + turnipspersecond + ' turnips every second.')

if input == '/farm':
    farm()
else:
    farm()
