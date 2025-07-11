### make aliens like brick we made
import turtle
import random

class AlienGroup():
    def __init__(self, x_range, y_range):
        self.Aliens = []
        
        colors = ['blue', 'green', 'yellow', 'cyan', 'magenta', 'red', 'orange']
        for j in range(y_range[0], y_range[1], -80):  # Fixed step direction
            for i in range(x_range[0], x_range[1], 100):
                t = turtle.Turtle()
                t.speed(0)
                t.penup()
                t.shape('square')
                t.shapesize(2, 3)  # Slightly smaller aliens
                t.color(random.choice(colors))
                t.goto(i, j)
                self.Aliens.append(t)

    def destroy(self, alien):
        if alien in self.Aliens:
            alien.hideturtle()
            self.Aliens.remove(alien)
    
    def get_random_alien(self):
        """Get a random alien for firing bullets"""
        if self.Aliens:
            return random.choice(self.Aliens)
        return None
    
    def move_down(self, distance):
        """Move all aliens down by specified distance"""
        for alien in self.Aliens:
            alien.sety(alien.ycor() - distance)


        


if __name__ == '__main__':

    ag = AlienGroup(  [-700,700],[500,0]  )
    turtle.mainloop()
