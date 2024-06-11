class Puzzle:
    def __init__(self, description, solution):
        self.description = description
        self.solution = solution
        self.solved = False

    def attempt_solve(self, attempt):
        if attempt == self.solution:
            self.solved = True
            return True
        return False
