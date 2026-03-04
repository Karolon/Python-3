import tkinter as tk
from game import Buildings

root = tk.Tk()
root.title("Graj")
root.geometry("500x500")
root.minsize(100, 100)
root.update()


win_height = root.winfo_height()
win_width = root.winfo_width()

buildings = Buildings()

#game
money = 0
money_multiplier = 1

def startGame():
    start_screen.pack_forget()
    game_screen.pack(side=tk.TOP, expand=True)

def gameLoop():
    global money
    if root.state() == "iconic":
        buildings.minimiseAllWindows()
    elif root.state() == "normal":
        buildings.openAllWindows()

    money_label.config(text=f"Money: {money}")
    money += money_multiplier * len(buildings.placed_buildingList)
    root.after(16, gameLoop)

#change use of maximise window
def moveUpWindows(a):
    if root.state() == 'zoomed':
        root.state("normal")
        buildings.moveAllWinToFirstPlan()


root.bind("<Configure>", moveUpWindows)

#Main screen
start_screen = tk.Frame(root, width=100, height=100)
start_screen.pack(side=tk.TOP, expand=True)

start_gameButton = tk.Button(start_screen, text="Start", command=startGame)
start_gameButton.place(width=100 ,height=50, x=0, y=25)

#the other screen
game_screen = tk.Frame(root, width=100, height=100)
game_screen.pack(side=tk.TOP, expand=True)
game_screen.pack_forget()

buy_buildingsButton = tk.Button(game_screen, text="Buy", command=lambda:buildings.newBuilding(root))
buy_buildingsButton.place(width=100 ,height=50, x=0, y=50)

money_label = tk.Label(game_screen, text="Money: 0")
money_label.place(width=100 ,height=50, x=0, y=10)


root.after(0, gameLoop)
root.mainloop()