from turtle import *
shape('turtle')
def draw_star(x,y,length):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
draw_star(10,20,100)
mainloop()