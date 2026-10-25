
# 🐍 Snake Game | Python & Pygame

A simple Snake Game built using **Python** and **Pygame** to practice programming logic, keyboard controls, collision detection, and game-state management.

## 📌 About

Control the green snake using the arrow keys, collect red fruit, and earn points. Avoid crossing the game window's boundaries to keep playing!

## ✨ Features

-   🎮 Arrow-key movement
-   🍎 Fruit collection and scoring (+10 points)
-   💥 Boundary collision detection
-   🔄 Restart functionality
-   🎲 Random fruit placement
-   🖥️ Game Over screen

## 🛠️ Tech Stack

-   **Language:** Python
-   **Library:** Pygame
-   **Module:** Random

## 🚀 Installation & Usage

1.  Clone the repository:
    
    bash
    
    ```
    git clone https://github.com/jvedant1001-ship-it/Python_Game.git
    
    ```
    
2.  Navigate to the project directory:
    
    bash
    
    ```
    cd Python_Game
    
    ```
    
3.  Install Pygame:
    
    bash
    
    ```
    python -m pip install pygame
    
    ```
    
4.  Run the game:
    
    bash
    
    ```
    python your_game_file.py
    
    ```
    
    Replace `your_game_file.py` with the actual Python filename.
    

## 🎯 Controls

Key

Action

⬆️ Up Arrow
Move up

⬇️ Down Arrow
Move down

⬅️ Left Arrow
Move left

➡️ Right Arrow
Move right

`R`
Restart after Game Over

## 📖 How It Works

<details> <summary>🎮 Movement and Game Loop</summary>

The game uses a continuous loop to process keyboard events, update the player's position, draw objects, and refresh the display.

Movement occurs in 20-pixel increments using `dx` and `dy`.

</details>

<details> <summary>🍎 Fruit Collection and Scoring</summary>

When the player's position matches the fruit's position, the score increases by 10 points and a new fruit is generated at a random grid position.

</details>

<details> <summary>💥 Collision and Restart Logic</summary>

The game checks whether the player crosses the window boundaries. If this happens, the `game_over` variable becomes `True`, and the Game Over screen appears.

Press `R` to reset the position, score, movement, and fruit location.

</details>

## 🛣️ Future Improvements

-   🐍 Add a growing snake body
-   💥 Implement self-collision detection
-   🍎 Prevent fruit from spawning inside the snake
-   🏆 Add a high-score system
-   🤖 Explore an AI player

## 👨‍💻 About Me

I'm a B.Tech CSE student learning Python and strengthening my programming fundamentals through hands-on projects.

I'm building step by step and exploring AI/ML as a future learning goal.

## 🔗 Connect

-   **GitHub:** [jvedant1001-ship-it](https://github.com/jvedant1001-ship-it)
----------

_Built with Python and Pygame as part of my learning journey._
