x = 45
y = -45
t = -45
r = 45
u = -10
z = 220
q = 0
w = 246
v = 255
e = 255
g = 255
c = 0
j = 0
d = 0
m = 255
b = 255
def setup():
    size(1000,600)
    
def draw():
    global x, y, t, u, r, z, q, w, v, e, g, c, j, m, d, b
    #солнце
    background( q, w, v )
    fill( e, g, c )
    ellipse(1000,0,300,300)
    push()
    #трава
    fill( j, m, d )
    rect(0,400,700,300)
    #озеро
    fill(0,0,b)
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
    rotate(radians( y ))
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
    rotate(radians( x ))
    ellipse(0,0,20,450)
    pop()
    #1 пара рук
    push()
    fill(12,131,13)
    translate(450,220)
    rotate(radians( t ))
    ellipse(0,0,50,120)
    pop()
    push()
    fill(12,131,13)
    translate(505,220)
    rotate(radians( r ))
    ellipse(0,0,50,120)
    pop()
    push()
    fill(245,206,148)
    ellipse(540,180,40,40)
    pop()
    #леска
    push()
    fill(144,88,0)
    translate(700, z )
    rotate(radians( u ))
    ellipse(0,0,2,320)
    pop()
    #рыба
    fill(16,212,232)
    ellipse(900,500,100,50)
    ellipse(950,500,25,50)
    fill(0)
    ellipse(870,500,10,10)
    #ведро
    fill(135,139,139)
    ellipse(295,350,50,50)
    push()
    fill( q, w, v )
    noStroke()
    ellipse(295,357,40,40)
    pop()
    fill(135,139,139)
    rect(270,360,50,70)
    #камыши
    fill(j,m,d)
    ellipse(190,300,7,250)
    fill(108,73,38)
    ellipse(190,175,15,100)
    fill(j,m,d)
    ellipse(170,300,7,250)
    fill(108,73,38)
    ellipse(170,175,15,100)
    fill(j,m,d)
    ellipse(150,300,7,250)
    fill(108,73,38)
    ellipse(150,175,15,100)
    fill(j,m,d)
    ellipse(130,300,7,250)
    fill(108,73,38)
    ellipse(130,175,15,100)
    fill(j,m,d)
    ellipse(110,300,7,250)
    fill(108,73,38)
    ellipse(110,175,15,100)
    fill(j,m,d)
    ellipse(90,300,7,250)
    fill(108,73,38)
    ellipse(90,175,15,100)
    fill(j,m,d)
    ellipse(70,300,7,250)
    fill(108,73,38)
    ellipse(70,175,15,100)
    fill(j,m,d)
    ellipse(50,300,7,250)
    fill(108,73,38)
    ellipse(50,175,15,100)
    fill(j,m,d)
    ellipse(30,300,7,250)
    fill(108,73,38)
    ellipse(30,175,15,100)
    #движение удочки
    if keyPressed:
        frameRate(5)
        if x <50:
            x = x + 5 
        else:
            x = 47
  
    #движение лески
    if keyPressed:
       # print(z)
        if z > 220 and z < 129:
            z = z - 90
        else:
            z = 220
    if keyPressed:
        fill(0)
        textSize(50)
        text(u'эх не повезло :(',600,40)
        if u < - 5:
            u = u + 5
        else:
            u = - 10
    if keyPressed:
        if key == 'w':
            v = v - 37
            w = w - 37
            c = c + 37
            m = m - 33
            b = b - 25
