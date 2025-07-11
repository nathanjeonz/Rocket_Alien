import turtle

class Rocket(turtle.Turtle):
    def __init__(self, image_file="rkt_resized.gif"):
        super().__init__()  # Initialize the Turtle superclass

        screen = turtle.Screen()
        screen.title("Rocket Animation")
        screen.bgcolor("cyan")

        # Register the custom image
        screen.addshape(image_file)

        # Set this turtle's shape to the custom image
        self.shape(image_file)
        self.penup()

    def move_left(self, distance):
        """Move the rocket left by a specified distance."""
        self.setheading(0)
        self.forward(distance)
    def move_right(self, distance):
        """Move the rocket right by a specified distance."""
        self.setheading(180)
        self.forward(distance)
    def bullet_fire(self):
        print('bullet is fired')
# ---------- Usage ----------
if __name__ == "__main__":
    # Create a Rocket instance
    rocket = Rocket()

    turtle.listen()  # Start listening for keyboard events
    # Bind the left arrow key to move the rocket left
    turtle.onkeypress(lambda: rocket.move_left(10), "Left")
    # Bind the right arrow key to move the rocket right
    turtle.onkeypress(lambda: rocket.move_right(10), "Right")
    # Bind the space key to fire a bullet
    turtle.onkeypress(rocket.bullet_fire, "space")


    # Keep the window open until closed by the user
    turtle.done()
    

