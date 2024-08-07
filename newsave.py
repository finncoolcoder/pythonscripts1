print('you are making a new save file.')
age = input('input your age>')
name = input('name>')
pet = input('what pet? >')
beard = input('beard? 1 for yes 2 for no')
if beard == 1:
    beard=True
else:
    beard=False
thing= input('what is your favorite thing')

favorites=[age.capitalize(),name.capitalize(),pet.capitalize(),str(beard).capitalize(),thing.capitalize()]


plaintextfavs= ' ,'.join(favorites)

f=open(name + '.txt', 'w')


f.write(plaintextfavs)






