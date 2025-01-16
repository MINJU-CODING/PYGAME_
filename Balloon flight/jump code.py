import pgzrun

WIDTH=500
HEIGHT=500

ba=Actor('balloon')
ba.bottomleft=(0,500)

jumping=False
howmuch=10

def draw():
    screen.clear()
    ba.draw()

def on_mouse_down():  #마우스를 클릭하면 열기구를 위로 올리
    global jumping
    if ba.bottom==500:
        jumping=True
        ba.y=ba.y-100

def on_mouse_up(): #마우스 클릭 안할때에는 다시 up값을 False
    global jumping
    jumping=False

def update():
    if not jumping and ba.bottom!=500:
        ba.y=ba.y+1
pgzrun.go()
