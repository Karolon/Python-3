import tkinter as tk
from tetris import *

root = tk.Tk()
root.title("Konstytant")
root.geometry("500x500")
root.minsize(100, 100)
root.update()

win_height = root.winfo_height()
win_width = root.winfo_width()

def startGame():
    start_screen.pack_forget()
    game_screen.pack(side=tk.TOP, expand=True)
    startTetris()

#Main screen
start_screen = tk.Frame(root, width=100, height=100)
start_screen.pack(side=tk.TOP, expand=True)

#the other screen
game_screen = tk.Frame(root, width=100, height=100)
game_screen.pack(side=tk.TOP, expand=True)
game_screen.pack_forget()

start_gameButton = tk.Button(start_screen, text="Start", command=startGame)
start_gameButton.place(width=100 ,height=50, x=0, y=25)

move_upButton = tk.Button(game_screen, text="left", command=moveWindow('left'))
move_upButton.grid(row = 1, column = 0)

while True:
    root.update()

root.mainloop()