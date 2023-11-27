from labyrinth import Labirynth
from labirynthApp import LabirynthApp

import tkinter as tk

labirynth_width = 17
labirynth_height = 17
start_position = (1, 1)
exit_position = (labirynth_width - 1, labirynth_height - 2)
labirynth = Labirynth(labirynth_width, labirynth_height, start_position, exit_position)
root = tk.Tk()
app = LabirynthApp(root, labirynth)
root.mainloop()