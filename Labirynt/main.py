import tkinter as tk
from menu import Menu
# ustawianie wielkosci labiryntu oraz pozycji startowej i wyjsciowej
labyrinth_width = 17
labyrinth_height = 17
start_position = (1, 1)
exit_position = (labyrinth_width - 1, labyrinth_height - 2)

# wywołanie głownego okna menu
root = tk.Tk()
Menu(root, labyrinth_width, labyrinth_height, start_position, exit_position)
root.mainloop()





