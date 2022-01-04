import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=50
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h, i, 0.1)
    h+=1/n
    t.color(c)
    t.forward(i*2)
    t.left(45)