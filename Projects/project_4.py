import turtle, random

###creating turtles###

t1 = turtle.Turtle()
t2 = turtle.Turtle()

### adding bg color ###
turtle.Screen().bgcolor("black")

t1.penup()
t1.goto(-100, 25)
t1.pendown()
t1.speed(0)

t2.penup()
t2.goto(-71, 10)
t2.pendown()
t2.speed(10)

### picking colors ###

# changed color so that theres blue in mine
# also, I made it larger
color = ["purple", "chartreuse"]
for i in range(1000):
    t1.color(color[i % 2])
    t1.forward(246)
    t1.left(156)
    t1.forward(20 + i)
    t1.left(33)

# colors = ["gold", "yellow"]
# for i in range(52):
#     t2.color(colors[i % 2])
#     t2.forward(175)
#     t2.left(100 + i)
#     t2.forward(45)
#     t2.left(46)

###sending turtles off screen so they dont show up in end product ###

t1.penup()
t1.goto(-1000,0)
t1.pendown()
t2.penup()
t2.goto(-1000,0)
t2.pendown()

turtle.exitonclick()