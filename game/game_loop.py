from game.game_map import GameMap
from game.player import Player


def start_game():
    # Initialize game objects
    game_map = GameMap("data/maps/main_map.json")
    player = Player()

    # Main game loop
    while True:
        # Render the current state
        game_map.render(player.position)

        # Get player input
        command = input("> ")

        # Process command
        if command == "quit":
            break
        else:
            handle_command(command, player, game_map)


def handle_command(command, player, game_map):
    # Process commands like moving, using items, etc.
    pass
