# Rocket vs Aliens Game

A classic space shooter game built with Python's turtle graphics library with enhanced gameplay features.

## How to Play

1. **Start the Game**: Run `python main.py` to start the game
2. **Controls**:
   - **Left Arrow**: Move rocket left (smooth movement)
   - **Right Arrow**: Move rocket right (smooth movement)
   - **Spacebar**: Fire bullets
   - **Q**: Quit the game

## Game Features

- **Rocket**: Controllable rocket ship with smooth movement
- **Aliens**: Colorful alien enemies that fire back at you!
- **Player Bullets**: Fire yellow bullets upward (max 3 at once)
- **Alien Bullets**: Red bullets fired by aliens downward
- **Collision Detection**: 
  - Player bullets destroy aliens on contact
  - Alien bullets can destroy the rocket
- **Progressive Difficulty**: 
  - Aliens move down faster each level
  - Aliens fire more frequently as levels progress
- **Multi-Level System**: Complete levels by destroying all aliens
- **Score System**: Earn 10 points for each alien destroyed

## Enhanced Gameplay Mechanics

### Smooth Movement
- Hold arrow keys for continuous smooth rocket movement
- No more jerky single-step movement

### Alien AI
- Aliens randomly fire bullets at the player
- Bullet firing frequency increases with each level
- Aliens gradually speed up their descent

### Progressive Difficulty
- **Level 1**: Slow alien movement, infrequent shooting
- **Higher Levels**: Faster alien descent, more frequent alien bullets
- Each level completed spawns a new wave of aliens

### Game Over Conditions
- **Win**: Destroy all aliens to advance to next level
- **Lose**: Get hit by alien bullet OR aliens reach the bottom

## Game Mechanics

- **Aliens**: Move downward with increasing speed per level
- **Player Bullets**: Move upward, automatically removed at screen edge
- **Alien Bullets**: Move downward, can hit and destroy the rocket
- **Real-time collision detection** for all projectiles
- **60 FPS** smooth gameplay
- **Screen boundaries** keep rocket within playable area

## Files Structure

- `main.py`: Enhanced main game with alien AI and progressive difficulty
- `rocket.py`: Rocket class with smooth movement controls
- `bullet.py`: Enhanced bullet system supporting multiple directions/colors
- `aliens.py`: Alien group class with firing capabilities
- `rkt_resized.gif`: Rocket sprite image
- `requirements.txt`: Required Python packages

## Requirements

- Python 3.x
- Pillow (PIL) library for image handling: `pip install Pillow`

## Installation

1. Ensure you have Python installed
2. Install required packages: `pip install -r requirements.txt`
3. Run the game: `python main.py`

## Strategy Tips

- Keep moving to avoid alien bullets
- Focus on destroying bottom-row aliens first (they're more dangerous)
- Watch for increasing alien firing frequency in higher levels
- Use the 3-bullet limit strategically

Enjoy the enhanced Rocket vs Aliens experience!
