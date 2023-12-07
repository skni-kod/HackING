import random

class Labirynth:
    def __init__(self, width, height, start_position, exit_position):
        self.width = width
        self.height = height
        self.start_position = start_position
        self.exit_position = exit_position
        self.generate_grid()

    def generate_grid(self):
        self.grid = [[1] * self.width for _ in range(self.height)]
        self.grid[self.width - 2][self.height - 1] = 0
        self.grid[1][0] = 0
        stack = []
        start_x, start_y = self.start_position
        stack.append((start_x, start_y))
        self.grid[start_y][start_x] = 0
        while stack:
            current_x, current_y = stack[-1]
            neighbors = self.get_unvisited_neighbors(current_x, current_y)
            if neighbors:
                next_x, next_y = random.choice(neighbors)
                wall_x, wall_y = (current_x + next_x) // 2, (current_y + next_y) // 2
                self.grid[wall_y][wall_x] = 0
                self.grid[next_y][next_x] = 0
                stack.append((next_x, next_y))
            else:
                stack.pop()

    def get_unvisited_neighbors(self, x, y):
        neighbors = [(x + dx, y + dy) for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]]
        valid_neighbors = [(nx, ny) for nx, ny in neighbors if
                           0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 1]
        return valid_neighbors

    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] == 0

    def is_exit(self, position):
        return position == self.exit_position



    def get_new_position(self, current_position, action):
        x, y = current_position
        if action == "Up":
            return x, y - 1
        elif action == "Down":
            return x, y + 1
        elif action == "Left":
            return x - 1, y
        elif action == "Right":
            return x + 1, y
        else:
            return current_position
        
        

    def calculate_reward(current_position, labirynth):
        if labirynth.is_exit(current_position):
            return 100  # Pozytywna nagroda za dotarcie do celu
        elif not labirynth.is_valid_move(current_position):
            return -10  # Negatywna kara za uderzenie w przeszkodę
        else:
            return 0  # Brak nagrody za inne ruchy
