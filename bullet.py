import turtle

class Bullet(turtle.Turtle):
    def __init__(self, color="red", shape="circle", size=1, direction=90):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.shapesize(size)
        self.penup()
        self.speed(0)  # Set the speed to the fastest
        self.setheading(direction)  # Set the initial heading

class Control_bullet():
    def __init__(self):
        self.bullets = []

    def make_bullet(self, x, y, color="red", direction=90):# when space is pressed then call this
        if len(self.bullets) < 3:
            b = Bullet(color=color, direction=direction)
            b.setposition(x, y)
            self.bullets.append(b)

    def move_bullets(self, speed, end_top, end_bottom=-400): # while loop keep on moving
        for b in self.bullets[:]:  # Use slice to avoid modification during iteration
            b.forward(speed)
            # if bullet will cross boundaries
            if b.ycor() >= end_top or b.ycor() <= end_bottom:
                b.hideturtle()
                self.bullets.remove(b)

        
# def add(a,v):
#     return a+v
# add(5,10)

# add2 = lambda a,v:a+v
# add2(4,3)

if __name__ == "__main__":
    # Create a Bullet instance
    bullets = Control_bullet()

    turtle.listen()  # Start listening for keyboard events

    # Bind the space key to fire the bullet
    turtle.onkey(lambda:bullets.make_bullet(0,-400), "space")  # Reset position on space key press
    # turtle.onkey(lambda:bullets.move_bullets(10,800), "Up")  # Reset position on space key press

    def game_loop():
        bullets.move_bullets(10, 800)
        turtle.ontimer(game_loop, 1)  # Call this function again after 20 ms

    game_loop()  # Start the loop
    turtle.mainloop()

