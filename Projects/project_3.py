# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")

def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)

def draw_rectangle( color="black",x=0,y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)



######################################################################
# https://en.wikipedia.org/wiki/Web_colors#Extended_colors
# Section 2 - Your code

# My background is a blue and pink ambre (my favorite colors)
set_background("bluepink")

draw_rectangle("royalblue", 100, 100, 200, 200)
draw_rectangle("lightskyblue", -100, 100, 200, 200)
draw_rectangle("lightskyblue", 100, -100, 200, 200)
draw_rectangle("royalblue", -100, -100, 200, 200)

# I wanted something in the center of my project, so I added these 2 squares

draw_rectangle("hotpink", 0, 0, 60, 60)
draw_rectangle("white", 0, 0, 25, 25)

s1 = create_sprite("soccerball3", 100, 100)

# Flowers go well with the colors AND for my birthday which is in spring
s2 = create_sprite("flower3 (1)", -100, -100)

# My favorite drink!
s3 = create_sprite("matcha", -100, 100)

s4 = create_sprite("paintpalette", 110, -70)

message1 = create_sprite("alien",-200,200)
message1.color("royal blue")
message1.write("Maya Lesso",font = ("Times New Roman", 30, "normal"))
message1.hideturtle()

# this is my text that chose my 2 favorite things from my coat of arms
message2 = create_sprite("flower2", -200, -250)
message2.color("hotpink")
message2.write("Artist and Soccer Player!",font = ("Times New Roman", 30, "normal"))
message2.hideturtle()


######################################################################


# Section 3 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()