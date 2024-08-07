print('interesting book')
print('press 1 then enter to open the book')
book=input('\n')
if book=='1':
    print('book was = to 1 you are now inside a block')
    file = open('C:/Users/ltidd/Dropbox/My PC (LAPTOP-S3NMNLN1)/Documents/list.txt', 'r')

    # This will print every line one by one in the file
    for each in file:
        print (each)

