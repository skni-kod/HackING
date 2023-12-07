from labyrinth import Labirynth
from labirynthApp import LabirynthApp
from QLearningAgent import QLearningAgent

import tkinter as tk

labirynth_width = 17
labirynth_height = 17
start_position = (1, 1)
exit_position = (labirynth_width - 1, labirynth_height - 2)
labirynth_object = Labirynth(labirynth_width, labirynth_height, start_position, exit_position)

agent = QLearningAgent(labirynth_object)

num_episodes = 1000

agent.train(labirynth_object, num_episodes)


root = tk.Tk()
app = LabirynthApp(root, labirynth_object)
root.mainloop()