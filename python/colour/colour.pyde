c, d = None, None

def setup():
    size(800, 800)
    global c, d
    c= color(random(255), random(255), random(255))
    d= color(random(255), random(255), random(255))


def draw():
    global c, d
    for x in range(width+height): # loop through every x
        p = lerpColor(c, d, 1.0*x/(width+height))
        stroke(p)
        if (x<width):
            line(0,x , x, 0)
        else:
            stroke(color(random(255), random(255), random(255)))
            line(x-width+20,height,height,x+20-width)
    for x in range(width):
        stroke(color(random(255), random(255), random(255)))
        line(x,300,x,500)
     
     

def mousePressed():
    global c, d
    c= color(random(255), random(255), random(255))
    d= color(random(255), random(255), random(255))
  
# What happens when you change:
