from turtle import Turtle , Screen
koky= Turtle()
window = Screen()
window.setup(width=800, height=800)
window.bgcolor("hotpink")
window.title("اهلا")
list_of_shapes = ("مربع","مثلث","دائرة","square","triangle","circle")
def draw_square():
    for _ in range(4):
        koky.shape("turtle")
        koky.pensize(10)
        koky.color("red")
        koky.forward(100)
        koky.left(90)

def draw_triangle():
    for _ in range(3):
        koky.shape("arrow")
        koky.pensize(5)
        koky.color("purple")
        koky.forward(200)
        koky.left(120)

def draw_circle():
    koky.shape("circle")
    koky.pensize(3)
    koky.color("black")
    koky.circle(100)

game_on=True
while game_on:
    user_choice= window.textinput("ازيك "," do you want square,circle, triangle  or exit عايز ارسملك دائرة,مربع ,مثلث ,خروج")
    if user_choice in list_of_shapes:
        if user_choice =="square" or user_choice=="مربع":
            draw_square()
        elif user_choice =="triangle" or user_choice =="مثلث":
            draw_triangle()
        elif user_choice =="دئرة"or user_choice =="circle":
            draw_circle()    
    elif user_choice =="exit" or user_choice =="خروج":
        game_on= False
        window.clear()
        koky.hideturtle()
        window.bgcolor("gray")
        koky.write("press any key to exit", align="center",font=("times new roman", 35,"normal"))
        koky.color("darkgray")
        koky.penup()
        koky.goto(0,-50)
        koky.write("اضغط في اي مكان للخروج",align="center",font=("times new roman", 25,"normal"))
window.exitonclick()
