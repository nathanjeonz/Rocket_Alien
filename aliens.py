### make aliens like brick we made
import turtle
import random
class AlienGroup():
    def __init__(self,x_range,y_range):
        self.Aliens = []
        
        colors = ['blue','green', 'yellow','cyan','magenta','red','indigo']
        for j in range(y_range[0],y_range[1],-100):
            for i in range(x_range[0],x_range[1],100):
                t = turtle.Turtle()
                t.speed(100)
                t.penup()
                t.shape('square')
                t.shapesize(3,5)
                t.color(random.choice(colors))
                t.goto(i,j)
                self.Aliens.append(t)

    def destroy(self, alien):
        if alien in self.Aliens:
            alien.hideturtle()
            self.Aliens.remove(alien)


        


if __name__ == '__main__':

    bg = BrickGroup(  [-700,700],[500,0]  )
    bg.destroy(5)
    turtle.mainloop()
