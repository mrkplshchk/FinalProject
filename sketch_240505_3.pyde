x=45
y=-45
t=-45
r=45
u=-19
z=230
def setup():
    size(1000,600)
def draw():
    global x,y,t,u,r,z
    #солнце
    background(29,196,240)
    fill(255,255,0)
    ellipse(1000,0,300,300)
    push()
    #трава
    fill(0,255,0)
    rect(0,400,700,300)
    fill(0,0,250)
    #озеро
    ellipse(750,400,100,50)
    ellipse(850,400,100,50)
    ellipse(950,400,100,50)
    rect(700,400,400,300)
    pop()
    #камни
    fill(157,149,149)
    ellipse(400,370,150,100)
    ellipse(500,390,80,50)
    #1 пара ног
    fill(12,131,13)
    ellipse(550,300,120,50)
    ellipse(600,350,50,120)
    fill(113,108,0)
    ellipse(610,390,70,50)
    #2 пара ног
    fill(12,131,13)
    ellipse(550,330,120,50)
    ellipse(600,370,50,120)
    fill(113,108,0)
    ellipse(610,410,70,50)
    #2 пара рук
    push()
    fill(12,131,13)
    translate(450,220)
    rotate(radians(y))
    ellipse(0,0,50,120)
    pop()
    push()
    fill(12,131,13)
    translate(500,200)
    rotate(radians(45))
    ellipse(0,0,50,120)
    pop()
    push()
    fill(245,206,148)
    ellipse(540,165,40,40)
    pop()
    #тело
    push()
    fill(12,131,13)
    ellipse(450,250,130,190)
    pop()
   #попа
    fill(12,131,13)
    ellipse(450,300,130,100) 
    #голава
    fill(245,206,148)
    ellipse(450,120,70,70)
    #шляпа
    fill(144,88,0)
    ellipse(450,100,90,20)
    ellipse(450,90,40,40)
    #контур
    push()
    noStroke()
    fill(12,131,13)
    ellipse(450,270,125,100) 
    pop()
    #ремень
    rect(385,279,129,40)
    #удочка
    push()
    fill(144,88,0)
    translate(540,180)
    rotate(radians(x))
    ellipse(0,0,20,370)
    pop()
    #1 пара рук
    push()
    fill(12,131,13)
    translate(450,220)
    rotate(radians(t))
    ellipse(0,0,50,120)
    pop()
    push()
    fill(12,131,13)
    translate(505,220)
    rotate(radians(r))
    ellipse(0,0,50,120)
    pop()
    push()
    fill(245,206,148)
    ellipse(540,180,40,40)
    pop()
    #леска
    push()
    fill(144,88,0)
    translate(670,z)
    rotate(radians(u))
    ellipse(0,0,2,330)
    pop()
    if mousePressed:
        if x <50:
            x=x+7
        else:
            x=49
    if mousePressed:
        print(z)
        if z >220:
            z=z-9
        else:
            z=220
    if mousePressed:
        if u <0:
            u=u+1
        else:
            u=0
    
