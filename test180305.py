import random

print('This is a number guess game...')
secret=random.randint(1,100)
num=input('please guess a number between 1 and 100:')
num=int(num)
while num!=secret:
    num=input('guess again:')
    num=int(num)
    if(num==secret):
        print('you are smart')
    else:
        if(num<secret):
            print('too small')
        else:
            print('too high')
print('game over')
