# Tic-Tac-Toe Game with Pygame

A sleek and interactive Tic-Tac-Toe game built using Pygame, featuring two exciting game modes: **Classic** and **Advanced**. The Classic mode offers the traditional 3x3 grid experience, while the Advanced mode introduces a unique twist where moves older than six turns fade and are replaced, adding strategic depth. With a clean user interface, vibrant visuals, and smooth gameplay, this project is perfect for players and developers alike.

## Features

- **Two Game Modes**:
  - **Classic**: Standard Tic-Tac-Toe rules where players take turns placing 'X' or 'O' to achieve three in a row.
  - **Advanced**: After six moves, the oldest move is removed, and the second-oldest fades to a lighter shade, requiring players to plan strategically.
- **Interactive UI**: A polished start screen with hoverable buttons to select game modes.
- **Dynamic Visuals**: Distinct colors for 'X' and 'O' marks, with lighter shades in Advanced mode to indicate fading moves.
- **Win/Draw Detection**: Automatically detects wins or draws, displaying results with a striking line across winning cells.
- **Restart Functionality**: Click anywhere after a game ends to return to the mode selection screen and start a new game.
- **Responsive Design**: A 600x600 pixel grid with clean lines and intuitive click-based input.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ErfanZmp/PyGame-Tic-Tac-Toe.git
   cd tictactoe-pygame
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.x installed. Install Pygame using pip:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Execute the main script to start the game:
   ```bash
   python main.py
   ```

## How to Play

1. Launch the game to see the mode selection screen.
2. Click **Classic** or **Advanced** to start the respective game mode.
3. Players take turns clicking on the 3x3 grid to place their mark ('X' or 'O').
   - In **Classic** mode, the game ends with a win (three in a row) or a draw (grid full).
   - In **Advanced** mode, after six moves, the oldest move is removed, and the second-oldest fades, continuing until a win or draw.
4. When the game ends, the winner (or draw) is displayed. Click anywhere to restart and choose a game mode again.

## Project Structure

- **`main.py`**: The core game logic, handling the Pygame setup, UI, game loop, and rendering. It includes functions for drawing the board, handling moves, and displaying win/draw states.
- **`base.py`**: Contains the `Base` class, managing the game state, move logic, win detection, and the Advanced mode's move expiration mechanic.

## Code Highlights

- **Modular Design**: The game logic is cleanly separated between `main.py` (UI and rendering) and `base.py` (game state and rules).
- **Advanced Mode Innovation**: The move expiration system in Advanced mode uses a list to track recent moves, updating the board dynamically.
- **Visual Feedback**: Hover effects on buttons and distinct colors for marks enhance the user experience.
- **Robust Win Detection**: The `Base` class efficiently checks for wins across rows, columns, and diagonals.

## Future Improvements

- Add AI opponents for single-player mode.
- Implement sound effects for moves and game outcomes.
- Add a scoring system to track wins across sessions.
- Enhance visuals with animations for mark placement and win lines.

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. Please ensure code follows PEP 8 guidelines and includes clear comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Pygame](https://www.pygame.org/), a powerful library for 2D game development in Python.
- Inspired by classic Tic-Tac-Toe with a creative twist for the Advanced mode.

---

Enjoy the game, and may the best strategist win! 🎮