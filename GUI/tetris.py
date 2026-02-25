import tkinter as tk

posX, posY = 0, 0

def startTetris():
    global root
    root = tk.Tk()
    root.title("Tetris")
    root.geometry("500x500+300+300")
    root.mainloop()

def moveWindow(a):
    global posX, posY, root
    if a == 'left':
        posX -= 1
    root.geometry(f"500x500+{posX}+{posY}")