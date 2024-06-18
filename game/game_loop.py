from game.game_map import GameMap
from game.player import Player
from data.maps.main_map import over_world


def start_game():
    # Initialize game objects
    player_name = input("Enter your name: ")
    game_map = GameMap(0, 0)
    player = Player(player_name)
    intro_text()
    # Main game loop
    while True:
        grid = (game_map.x, game_map.y)
        print_description(grid)
        command = options(grid)
        # Process command
        if command == "quit":
            break
        else:
            handle_command(command, player, game_map, grid)


def handle_command(command, player, game_map, grid):
    action = over_world[grid][command]
    if action == "look around":
        print(over_world[grid]["detailed_description"])
    elif action == "north":
        game_map.move_north()
    elif action == "south":
        game_map.move_south()
    elif action == "east":
        game_map.move_east()
    elif action == "west":
        game_map.move_west()


def intro_text():
    print("This is some intro text that plays when you start the game.")


def print_description(grid):
    print(over_world[grid]["description"])


def options(grid):
    return int(input(over_world[grid]["options"]))
