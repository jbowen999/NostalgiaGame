class GameMap:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_north(self):
        self.y += 1

    def move_south(self):
        self.y -= 1

    def move_east(self):
        self.x += 1

    def move_west(self):
        self.x -= 1

    def print_coords(self):
        print(f"({self.x}, {self.y})")
