import turtle
import math
import random
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
        
        self.player_bullets = Control_bullet()
        self.alien_bullets = Control_bullet()
        self.alien_group = AlienGroup([-500, 600], [300, -100])
        
        # Game state
        self.game_running = True
        self.score = 0
        self.level = 1
        self.alien_speed_base = 2
        self.alien_speed_increment = 0.1
        self.alien_fire_chance = 0.003  # Probability of alien firing per frame
        
        # Movement state for smooth controls
        self.keys_pressed = {'Left': False, 'Right': False}
        
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
        """Set up keyboard controls for smooth movement"""
        self.screen.listen()
        
        # Key press events
        self.screen.onkeypress(self.press_left, "Left")
        self.screen.onkeypress(self.press_right, "Right")
        self.screen.onkeypress(self.fire_bullet, "space")
        self.screen.onkeypress(self.quit_game, "q")
        
        # Key release events
        self.screen.onkeyrelease(self.release_left, "Left")
        self.screen.onkeyrelease(self.release_right, "Right")
    
    def press_left(self):
        """Handle left key press"""
        self.keys_pressed['Left'] = True
    
    def release_left(self):
        """Handle left key release"""
        self.keys_pressed['Left'] = False
    
    def press_right(self):
        """Handle right key press"""
        self.keys_pressed['Right'] = True
    
    def release_right(self):
        """Handle right key release"""
        self.keys_pressed['Right'] = False
    
    def update_rocket_movement(self):
        """Update rocket position based on pressed keys"""
        if self.keys_pressed['Left']:
            x = self.rocket.xcor()
            if x > -580:  # Keep rocket within screen bounds
                self.rocket.move_left(5)
        
        if self.keys_pressed['Right']:
            x = self.rocket.xcor()
            if x < 580:  # Keep rocket within screen bounds
                self.rocket.move_right(5)
    
    def fire_bullet(self):
        """Fire a bullet from rocket position"""
        x, y = self.rocket.xcor(), self.rocket.ycor()
        self.player_bullets.make_bullet(x, y + 20, color="yellow", direction=90)
    
    def alien_fire_bullet(self):
        """Make a random alien fire a bullet"""
        firing_alien = self.alien_group.get_random_alien()
        if firing_alien and random.random() < self.alien_fire_chance:
            x, y = firing_alien.xcor(), firing_alien.ycor()
            self.alien_bullets.make_bullet(x, y - 20, color="red", direction=270)
    
    def quit_game(self):
        """Quit the game"""
        self.game_running = False
        self.screen.bye()
    
    def check_bullet_alien_collisions(self):
        """Check for collisions between player bullets and aliens"""
        for bullet in self.player_bullets.bullets[:]:
            for alien in self.alien_group.Aliens[:]:
                distance = math.sqrt(
                    (bullet.xcor() - alien.xcor()) ** 2 + 
                    (bullet.ycor() - alien.ycor()) ** 2
                )
                
                if distance < 50:
                    # Remove bullet
                    bullet.hideturtle()
                    self.player_bullets.bullets.remove(bullet)
                    
                    # Remove alien
                    self.alien_group.destroy(alien)
                    
                    # Increase score
                    self.score += 10
                    self.update_score_display()
                    break
    
    def check_bullet_rocket_collisions(self):
        """Check for collisions between alien bullets and rocket"""
        for bullet in self.alien_bullets.bullets[:]:
            distance = math.sqrt(
                (bullet.xcor() - self.rocket.xcor()) ** 2 + 
                (bullet.ycor() - self.rocket.ycor()) ** 2
            )
            
            if distance < 40:
                # Remove bullet
                bullet.hideturtle()
                self.alien_bullets.bullets.remove(bullet)
                
                # Game over - rocket hit
                self.display_message("ROCKET DESTROYED! GAME OVER!", "red")
                self.game_running = False
                return True
        return False
    
    def check_game_over(self):
        """Check if game is over"""
        # Check if all aliens are destroyed
        if not self.alien_group.Aliens:
            self.level += 1
            self.display_message(f"LEVEL {self.level} COMPLETE!", "green")
            # Create new alien group for next level
            self.alien_group = AlienGroup([-500, 600], [300, -100])
            self.alien_speed_base += self.alien_speed_increment
            self.alien_fire_chance += 0.001  # Aliens fire more frequently
            return False
        
        # Check if any alien reached the bottom
        for alien in self.alien_group.Aliens:
            if alien.ycor() < -300:
                self.display_message("ALIENS INVADED! GAME OVER!", "red")
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
        self.score_display.write(f"Score: {self.score}  Level: {self.level}", 
                               align="left", font=("Arial", 16, "normal"))
    
    def game_loop(self):
        """Main game loop"""
        if not self.game_running:
            return
        
        # Update rocket movement
        self.update_rocket_movement()
        
        # Move bullets
        self.player_bullets.move_bullets(15, 400)
        self.alien_bullets.move_bullets(10, 400, -400)
        
        # Alien firing
        self.alien_fire_bullet()
        
        # Check collisions
        self.check_bullet_alien_collisions()
        if self.check_bullet_rocket_collisions():
            return
        
        # Move aliens down with gradually increasing speed
        if hasattr(self, 'frame_count'):
            self.frame_count += 1
        else:
            self.frame_count = 0
        
        # Aliens move down more frequently as game progresses
        alien_move_frequency = max(50, 100 - (self.level * 5))
        if self.frame_count % alien_move_frequency == 0:
            current_speed = self.alien_speed_base + (self.level - 1) * self.alien_speed_increment
            self.alien_group.move_down(current_speed)
        
        # Check game over conditions
        if self.check_game_over():
            if not self.alien_group.Aliens:  # Level complete, continue game
                pass
            else:  # Game over
                self.game_running = False
                return
        
        # Update screen
        self.screen.update()
        
        # Schedule next frame
        self.screen.ontimer(self.game_loop, 16)  # ~60 FPS

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