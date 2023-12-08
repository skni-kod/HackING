from labyrinth import Labyrinth
from labirynthApp import LabyrinthApp
import tkinter as tk

class Menu:
    def __init__(self, root, width, height, start_position, exit_position):
        #tworzenie zmiennych
        self.root = root
        self.width = width
        self.height = height
        self.start_position = start_position
        self.exit_position = exit_position
        self.labyrinth = Labyrinth(self.width, self.height, self.start_position, self.exit_position)
        #tworzenie przycisków oraz ustawianie ich lokalizacji
        self.button_random = tk.Button(root, text="Losowy Labirynt", command=self.button_random_clicked)
        self.button_random.pack(pady=20, padx=20)
        self.button_load = tk.Button(root, text="Wczytaj Labirynt", command=self.button_load_clicked)
        self.button_load.pack(pady=20, padx=20)
        self.button_save = tk.Button(root, text="Zapisz Labirynt", command=self.button_save_clicked)

    # funkcjonalnośc przycisków
    def button_random_clicked(self):
        self.button_save.pack(pady=20, padx=20) # ustawianie pozycji przycisku save
        self.button_random.pack_forget() # ukrycie przycisku
        self.button_load.pack_forget()  # ukrycie przycisku
        LabyrinthApp(self.root, self.labyrinth) # wywołanie labiryntu
    def button_load_clicked(self):
        file = open("labirynt.txt", "r")
        content = file.read()
        temp = []
        grid = []
        for i in content:
            if i != ' ' and i != '\n':
                temp.append(int(i))
            if len(temp) == self.width:
                grid += [temp.copy()]
                temp.clear()
        #dorobic wyswietlanie nowego labiryntu

    def button_save_clicked(self):
        file = open("labirynt.txt", "w")
        for i in self.labyrinth.grid:
            for n in i:
                file.write(str(n) + " ")
            file.write("\n")
        file.close()







