import random

class Labyrinth:
    def __init__(self, width, height, start_position, exit_position):
        self.width = width
        self.height = height
        self.start_position = start_position
        self.exit_position = exit_position
        self.generate_grid()

    def generate_grid(self):
        # tworzenie macierzy(labiryntu) wypełnionej jedynkami(sciany)
        # przy pomocy algorytmu DFS tworzy scierzke z pozycji startowej do wyjscia(droga jest zapisywana jako 0 w macierzy)
        self.grid = [[1] * self.width for i in range(self.height)]
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
