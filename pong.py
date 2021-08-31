# Game Ping-Pong

# Imports
from tkinter import *
import random
import time

# User input
level = int(input("What level would you like to play? 1/2/3/4/5 \n"))

# Var
length = 500/level

# Tk Object
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Canvas result
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()
root.update()

# Var
count = 0

# Var
lost = False

# Class
class Bola:
    def __init__(self, canvas, Barra, color):

        # Var
        self.canvas = canvas
        self.Barra = Barra
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)

        # List
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        # Var
        self.x = starts_x[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Function
    def draw(self):

        # Var
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)

        # Condicional if
        if pos[1] <= 0:

            # Var
            self.y = 3

        # Condicional if
        if pos[3] >= self.canvas_height:

            # Var
            self.y = -3

        # Condicional if
        if pos[0] <= 0:

            # Var
            self.x = 3
            
        # Condicional if
        if pos[2] >= self.canvas_width:

            # Var
            self.x = -3

        # Var
        self.Barra_pos = self.canvas.coords(self.Barra.id)

        # Condicional if aninhado
        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:

                # Variáveis
                self.y = -3
                global count
                count +=1

                # Chamada à função
                score()

        # Condicional if 
        if pos[3] <= self.canvas_height:

            # Var
            self.canvas.after(10, self.draw)
        else:

            # function call
            game_over()

            # Var
            global lost
            lost = True

# Class
class Barra:
    def __init__(self, canvas, color):

        # Var
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    # Function
    def draw(self):

        # method call
        self.canvas.move(self.id, self.x, 0)

        # Var
        self.pos = self.canvas.coords(self.id)

        # Condicional if 
        if self.pos[0] <= 0:

            # Var
            self.x = 0
        
        # Condicional if 
        if self.pos[2] >= self.canvas_width:

            # Var
            self.x = 0
        
        global lost
        
        # Condicional if 
        if lost == False:
            self.canvas.after(10, self.draw)

    # Function
    def move_left(self, event):

        # Condicional if 
        if self.pos[0] >= 0:

            # Variável
            self.x = -3

    # Function
    def move_right(self, event):

        # Condicional if 
        if self.pos[2] <= self.canvas_width:

            # Var
            self.x = 3

# Function
def start_game(event):

    # Var
    global lost, count
    lost = False
    count = 0

    # Function call
    score()

    # Variável que recebe o resultado da função
    canvas.itemconfig(game, text=" ")

    # Métodos dos objetos
    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Function
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

# Function
def game_over():
    canvas.itemconfig(game, text="Game over!")

# Instâncias dos objetos Barra e Bola
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

# Variáveis que recebem o resultado das funções
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))
canvas.bind_all("<Button-1>", start_game)

# Run
root.mainloop()


