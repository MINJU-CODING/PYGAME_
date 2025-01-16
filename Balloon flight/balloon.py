import pgzrun
from random import randint

#set the screen size
WIDTH=800
HEIGHT=600

#set up the actors
balloon = Actor('balloon')
balloon.pos=400,300

#prepare the obstacles
bird=Actor('bird-up')
bird.pos=randint(800,1600),randint(10,200)

house=Actor('house')
house.pos=randint(800,1600),460

tree=Actor('tree')
tree.pos=randint(800,1600),450

#create variables
bird_up=True
up=False
game_over=False
score=0
number_of_updates=0  #to change the image of bird

scores=[]

#manage the high scores (맨 마지막에 안의 내용 채울 것임)
def update_high_scores():
    global score,scores
    filename=r"/Users/mj/Documents/pygames/Balloon flight/high-scores.txt"
    #위의 파일명에서 \ 이 백슬래쉬 기호와 맨 뒤에 공백 반드시 삭제할 것!
    scores=[]
    with open(filename,'r') as file:
        line=file.readline()
        high_scores=line.split()
        for high_score in high_scores:
            if (score>int(high_score)):
                scores.append(str(score)+' ')
                score=int(high_score)
            else:
                scores.append(str(high_score)+' ')
    with open(filename,'w') as file:
        for high_score in scores:
            file.write(high_score)
    
def display_high_scores():
    screen.draw.text('HIGH SCORES',(350,150),color='black')
    y=175
    position=1
    for high_score in scores:
        screen.draw.text(str(position)+'. '+high_score,(350,y),color='black')
        y=y+25
        position=position+1

#let's draw
def draw():
    screen.blit('background',(0,0))
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text('Score: '+str(score),(700,5),color='black')
    else:  #게임이 끝나
        display_high_scores()

#마우스에 반응하기
def on_mouse_down():  #마우스를 클릭하면 열기구를 위로 올리
    global up
    up=True
    balloon.y=balloon.y-50

def on_mouse_up(): #마우스 클릭 안할때에는 다시 up값을 False
    global up
    up=False

#make the bird flap
def flap():
    global bird_up
    if bird_up:
        bird.image='bird-down'
        bird_up=False
    else:
        bird.image='bird-up'
        bird_up=True

#update 함수 내에서 중력 만들기
def update():
    global game_over,score,number_of_updates
    if not game_over:
        if not up:
            balloon.y=balloon.y+1  #게임 오버도 아니고, 상승하고 있지도 않을때에는 계속해서 1씩 내려가게 만들기
            
    if bird.x>0:
        bird.x=bird.x-4  #새가 오른쪽에서 왼쪽으로 이동하게 만들고
        if number_of_updates==9: #새의 움직임을 만들어주는 코드
            flap()
            number_of_updates=0
        else:
            number_of_updates=number_of_updates+1
    else: #새가 왼쪽 화면 밖으로 사라졌을때 다시 오른쪽에서 나타나게 해야함
        bird.x=randint(800,1600)
        bird.y=randint(10,200)
        score=score+1
        number_of_updates=0

    if house.right>0:
        house.x=house.x-2
    else:
        house.x=randint(800,1600)
        score=score+1

    if tree.right>0:
        tree.x=tree.x-2
    else:
        tree.x=randint(800,1600)
        score=score+1

    if balloon.top<0 or balloon.bottom>560: #열기구가 천장에 닿거나 바닥에 닿으면 게임 종료
        game_over=True
        update_high_scores()

    if balloon.collidepoint(bird.x,bird.y) or balloon.collidepoint(house.x,house.y) or balloon.collidepoint(tree.x,tree.y):
        game_over=True
        update_high_scores()


pgzrun.go()












        
