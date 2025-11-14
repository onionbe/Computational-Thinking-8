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


# Section 2: Setup
# TODO - create your player character
# TODO - set your background
# TODO - set the starting value for your variable

housesbuilt = 0
points = 0

# Background (moveable sprite)
green = create_sprite("green", 0,0)
background = create_sprite("background", 0,0)


# Houses
house1 = create_sprite("materials", -350,-325)
house2 = create_sprite("materials", -380,460)
house3 = create_sprite("materials", 310,190)

# Characters
mcharacter = create_sprite("mplayer", -25,-30)
helper = create_sprite("helper_player", -250,-30)

# Section 3: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Arrow Key Movement - FOR BACKGROUND 

def move_up():
    background.setheading(270)
    background.forward(10)
    house1.setheading(270)
    house1.forward(10)
    house2.setheading(270)
    house2.forward(10)
    house3.setheading(270)
    house3.forward(10)
    helper.setheading(270)
    helper.forward(10)
        
def move_down():
    background.setheading(90)
    background.forward(10)
    house1.setheading(90)
    house1.forward(10)
    house2.setheading(90)
    house2.forward(10)
    house3.setheading(90)
    house3.forward(10)
    helper.setheading(90)
    helper.forward(10)
    
def move_left():
    background.setheading(0)
    background.forward(10)
    house1.setheading(0)
    house1.forward(10)
    house2.setheading(0)
    house2.forward(10)
    house3.setheading(0)
    house3.forward(10)
    helper.setheading(0)
    helper.forward(10)
    
def move_right():    
    background.setheading(180)
    background.forward(10)
    house1.setheading(180)
    house1.forward(10)
    house2.setheading(180)
    house2.forward(10)
    house3.setheading(180)
    house3.forward(10)
    helper.setheading(180)
    helper.forward(10)

def interact1():
	global points
	if get_distance(mcharacter, house1) < 100: 
		house1.color("White")
		house1.write("Building... Please wait...", font = ("Times New Roman", 12, "bold"))
		window.update()
		time.sleep(5)
		set_image(house1, "built_house")
		house1.clear()
		window.update()
		points += 1
		window.update()

def interact2():
	global points
	if get_distance(mcharacter, house2) < 100: 
		house2.color("White")
		house2.write("Building... Please wait...", font = ("Times New Roman", 12, "bold"))
		window.update()
		time.sleep(5)
		set_image(house2, "built_house")
		house2.clear()
		window.update()
		points += 1
		window.update()

def interact3():
	global points
	if get_distance(mcharacter, house3) < 100: 
		house3.color("White")
		house3.write("Building... Please wait...", font = ("Times New Roman", 12, "bold"))
		window.update()
		time.sleep(5)
		set_image(house3, "built_house")
		house3.clear()
		window.update()
		points += 1
		window.update()

def interact_all():
	interact1()
	interact2()
	interact3()
	window.update()


window.onkeypress(interact_all, "space")
	
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right") 

# DIALOGUE FROM HELPER
helper.color("White")
helper.write("Hello! I need some help with building some houses.", font = ("Times New Roman", 12, "bold"))
window.update()
time.sleep(4)
window.update()
helper.clear()
window.update()

helper.write("There should be materials around here somewhere...(press space)", font = ("Times New Roman", 12, "bold"))
window.update()
time.sleep(5)
window.update()
helper.clear()
helper.hideturtle()
window.update()

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
 	# Code for automatic actions
	

	window.update()

	if timer >= 1000 and points <= 3:
		mcharacter.color("White")
		window.update()
		mcharacter.write("Try again...", font = ("Times New Roman", 12, "bold"))
		window.update()
		time.sleep(2)
		break
	if timer <= 1000 and points == 3:
		mcharacter.color("White")
		window.update()
		mcharacter.write("You Win!", font = ("Times New Roman", 12, "bold"))
		window.update()
		time.sleep(2)
		break 

print(f"Game Over! Your score was {points}")