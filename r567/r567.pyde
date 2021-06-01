x = 700
y = 350
speed = 2.5
brush = 0
q1 = random(1069)
w1 = random(537)
g1 = random(1233)
h1 = random(481)
pizza = 1



def setup():

    size(1400,700)

def draw():
    frameRate(87)
    background(255)
    fill(240,5,5)
    photo = loadImage('domik.png')
    image(photo,q1,w1)
    photo = loadImage('pepka.png')
    if pizza == 1:
        image(photo,g1,h1)
    ellipse(x,y,50,50)
    textSize(30)
    text(brush,1325,50)
    textSize(30)
    text(speed,1250,85)
    






def keyPressed():
    global x,y, pizza, q1, w1, g1, h1, speed, brush
    if key=='w' or key == 'W':
        y=y-speed
    if key=='s' or key == 'S':
        y=y+speed
    if key=='a' or key=='A':
        x=x-speed
    if key=='d' or key=='D':
        x=x+speed
    if (key=='b' or key=='B') and x>g1 and x<g1+167 and y>h1 and y<h1+219 :
        pizza=0
    if (key=='n' or key=='N') and x>q1 and x<q1+331 and y>w1 and y<w1+163 :
        pizza=1
        q1 = random(1069)
        w1 = random(537)
        g1 = random(1233)
        h1 = random(481)
        speed = speed + 0.5
        brush = brush + 1 
    
