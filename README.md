# Rocket vs Aliens Game

A classic space shooter game built with Python's turtle graphics library.

## How to Play

1. **Start the Game**: Run `python main.py` to start the game
2. **Controls**:
   - **Left Arrow**: Move rocket left
   - **Right Arrow**: Move rocket right  
   - **Spacebar**: Fire bullets
   - **Q**: Quit the game

## Game Features

- **Rocket**: Controllable rocket ship at the bottom of the screen
- **Aliens**: Colorful alien enemies arranged in rows
- **Bullets**: Fire up to 3 bullets at a time
- **Collision Detection**: Bullets destroy aliens on contact
- **Score System**: Earn 10 points for each alien destroyed
- **Game Over Conditions**: 
  - Win by destroying all aliens
  - Lose if aliens reach the bottom

## Game Mechanics

- Aliens slowly move downward over time
- Bullets are automatically removed when they leave the screen
- The rocket is confined to the screen boundaries
- Real-time collision detection between bullets and aliens

## Files Structure

- `main.py`: Main game file that integrates all components
- `rocket.py`: Rocket class with movement controls
- `bullet.py`: Bullet class and bullet management
- `aliens.py`: Alien group class for enemy management
- `rkt_resized.gif`: Rocket sprite image
- `requirements.txt`: Required Python packages

## Requirements

- Python 3.x
- Pillow (PIL) library for image handling: `pip install Pillow`

## Installation

1. Ensure you have Python installed
2. Install required packages: `pip install -r requirements.txt`
3. Run the game: `python main.py`

Enjoy playing Rocket vs Aliens!
