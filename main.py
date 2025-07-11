import turtle
import math
from rocket import Rocket
from bullet import Control_bullet
from aliens import AlienGroup

class Game:
    def __init__(self):
        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.title("Rocket vs Aliens Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=1200, height=800)
        self.screen.tracer(0)  # Turn off animation for better performance
        
        # Initialize game objects
        self.rocket = Rocket()
        self.rocket.goto(0, -350)  # Position rocket at bottom center
        
        self.bullet_controller = Control_bullet()
        self.alien_group = AlienGroup([-500, 600], [300, -100])
        
        # Game state
        self.game_running = True
        self.score = 0
        
        # Create score display
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(-580, 350)
        self.update_score_display()
        
        # Set up controls
        self.setup_controls()
        
        # Start game loop
        self.game_loop()
    
    def setup_controls(self):
        """Set up keyboard controls"""
        self.screen.listen()
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.fire_bullet, "space")
        self.screen.onkey(self.quit_game, "q")
    
    def move_left(self):
        """Move rocket left"""
        x = self.rocket.xcor()
        if x > -580:  # Keep rocket within screen bounds
            self.rocket.move_left(20)
    
    def move_right(self):
        """Move rocket right"""
        x = self.rocket.xcor()
        if x < 580:  # Keep rocket within screen bounds
            self.rocket.move_right(20)
    
    def fire_bullet(self):
        """Fire a bullet from rocket position"""
        x, y = self.rocket.xcor(), self.rocket.ycor()
        self.bullet_controller.make_bullet(x, y + 20)
    
    def quit_game(self):
        """Quit the game"""
        self.game_running = False
        self.screen.bye()
    
    def check_collisions(self):
        """Check for collisions between bullets and aliens"""
        for bullet in self.bullet_controller.bullets[:]:  # Use slice to avoid modification during iteration
            for alien in self.alien_group.Aliens[:]:
                # Calculate distance between bullet and alien
                distance = math.sqrt(
                    (bullet.xcor() - alien.xcor()) ** 2 + 
                    (bullet.ycor() - alien.ycor()) ** 2
                )
                
                # If collision detected (distance less than combined size)
                if distance < 50:
                    # Remove bullet
                    bullet.hideturtle()
                    self.bullet_controller.bullets.remove(bullet)
                    
                    # Remove alien
                    self.alien_group.destroy(alien)
                    
                    # Increase score
                    self.score += 10
                    self.update_score_display()
                    break
    
    def check_game_over(self):
        """Check if game is over (all aliens destroyed or aliens reach bottom)"""
        # Check if all aliens are destroyed
        if not self.alien_group.Aliens:
            self.display_message("YOU WIN!", "green")
            return True
        
        # Check if any alien reached the bottom
        for alien in self.alien_group.Aliens:
            if alien.ycor() < -300:
                self.display_message("GAME OVER!", "red")
                return True
        
        return False
    
    def display_message(self, message, color):
        """Display a message on screen"""
        msg_turtle = turtle.Turtle()
        msg_turtle.speed(0)
        msg_turtle.color(color)
        msg_turtle.penup()
        msg_turtle.hideturtle()
        msg_turtle.goto(0, 0)
        msg_turtle.write(message, align="center", font=("Arial", 24, "bold"))
        self.screen.update()
    
    def update_score_display(self):
        """Update the score display"""
        self.score_display.clear()
        self.score_display.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))
    
    def move_aliens_down(self):
        """Move all aliens down periodically"""
        for alien in self.alien_group.Aliens:
            alien.sety(alien.ycor() - 5)
    
    def game_loop(self):
        """Main game loop"""
        if not self.game_running:
            return
        
        # Move bullets
        self.bullet_controller.move_bullets(15, 400)
        
        # Check collisions
        self.check_collisions()
        
        # Move aliens down every 100 frames (adjust for difficulty)
        if hasattr(self, 'frame_count'):
            self.frame_count += 1
        else:
            self.frame_count = 0
        
        if self.frame_count % 100 == 0:
            self.move_aliens_down()
        
        # Check game over conditions
        if self.check_game_over():
            self.game_running = False
            return
        
        # Update screen
        self.screen.update()
        
        # Schedule next frame
        self.screen.ontimer(self.game_loop, 20)  # 50 FPS

def main():
    """Start the game"""
    try:
        game = Game()
        game.screen.mainloop()
    except turtle.Terminator:
        print("Game window closed")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()