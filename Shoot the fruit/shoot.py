import pgzrun

from random import randint

apple=Actor('apple')
orange=Actor('orange')
score=0

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    screen.draw.text('score: '+str(score),color='white',topleft=(10,10))

def place_apple():
    apple.x=randint(10,800)
    apple.y=randint(10,600)

def place_orange():
    orange.x=randint(10,800)
    orange.y=randint(10,600)

def on_mouse_down(pos):
    global score,apple
    if apple.collidepoint(pos):
        score=score+1
        print('Good shot!')
        if apple.image=='orange':
            print('hello')
        place_apple()
        place_orange()
    elif orange.collidepoint(pos):
        score=0
        print('Too bad ..')
        place_orange()
        place_apple()
    else:
        print('You missed!')
        print(score)
        quit()
        

place_apple()
place_orange()

pgzrun.go()
