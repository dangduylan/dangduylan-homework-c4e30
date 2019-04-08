def draw_square(l,c):
    color(c)
    for i in range(4):
        forward(l)
        left(90)
from turtle import *
shape('turtle')       
draw_square(100,'red')
mainloop()