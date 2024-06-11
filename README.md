Module Descriptions
main.py: This is the entry point of your game. It will contain the main function that starts the game loop.

game/**init**.py: Makes the game directory a Python package.

game/game_loop.py: Contains the main game loop and logic for transitioning between different states and scenes.

game/game_map.py: Manages the game map, including loading maps from files and handling movement and transitions between different grids.

game/player.py: Defines the player character, including attributes, inventory, and actions.

game/items.py: Manages items that the player can interact with, including collecting, using, and inspecting items.

game/enemies.py: Defines enemies that the player may encounter, including their behaviors and interactions with the player.

game/puzzles.py: Contains the logic for puzzles that the player can solve.

game/utils.py: Contains utility functions that are used throughout the game, such as input handling, saving/loading game state, etc.

data/maps/: Directory containing map data files in JSON format.

data/items.json: File containing item data in JSON format.
