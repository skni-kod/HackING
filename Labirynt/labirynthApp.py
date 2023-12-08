import tkinter as tk
from labyrinth import Labyrinth

class LabyrinthApp:
    def __init__(self, master, labyrinth):
        self.master = master
        self.labyrinth = labyrinth
        self.current_position = labyrinth.start_position
        self.order = []
        self.canvas = tk.Canvas(master, width=labyrinth.width * 30, height=labyrinth.height * 30)
        self.canvas.pack()
        self.draw_labyrinth()
        self.draw_player()
        # sprawdzanie który przycisk został wcisniety i wykonanie akcji przypisaniej do niego
        master.bind("<Up>", self.move_up)
        master.bind("<Down>", self.move_down)
        master.bind("<Left>", self.move_left)
        master.bind("<Right>", self.move_right)

    def draw_labyrinth(self):
        for i in range(self.labyrinth.height):
            for j in range(self.labyrinth.width):
                x1, y1 = j * 30, i * 30
                x2, y2 = x1 + 30, y1 + 30
                if self.labyrinth.grid[i][j] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def draw_player(self):
        x, y = self.current_position
        x1, y1 = x * 30, y * 30
        x2, y2 = x1 + 30, y1 + 30
        self.player = self.canvas.create_oval(x1, y1, x2, y2, fill="red")

    def move_up(self, event):
        self.order.append("Up")
        new_position = (self.current_position[0], self.current_position[1] - 1)
        self.move(new_position)

    def move_down(self, event):
        self.order.append("Down")
        new_position = (self.current_position[0], self.current_position[1] + 1)
        self.move(new_position)

    def move_left(self, event):
        self.order.append("Left")
        new_position = (self.current_position[0] - 1, self.current_position[1])
        self.move(new_position)

    def move_right(self, event):
        self.order.append("Right")
        new_position = (self.current_position[0] + 1, self.current_position[1])
        self.move(new_position)

    def move(self, new_position):
        if self.labyrinth.is_valid_move(new_position):
            x, y = self.current_position
            new_x, new_y = new_position
            self.canvas.move(self.player, (new_x - x) * 30, (new_y - y) * 30)
            self.current_position = new_position
            if self.labyrinth.is_exit(new_position):
                file = open("droga.txt", 'a')
                for n in self.order:
                    file.write(n + " ")
                file.write("end\n")
                file.close()
                self.load_new_labyrinth()

    def load_new_labyrinth(self):
        self.canvas.delete("all")
        self.order.clear()
        self.labyrinth = self.generate_new_labyrinth()
        self.current_position = self.labyrinth.start_position
        self.draw_labyrinth()
        self.draw_player()


    def generate_new_labyrinth(self):
        return Labyrinth(17, 17, (1, 1), (16, 15))
