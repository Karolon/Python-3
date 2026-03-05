import tkinter as tk
from game import Buildings

#game
buy_start_price = 100
buy_multiplier = 0
buy_price = lambda: buy_start_price * (1 + buy_multiplier * 0.2**buy_multiplier)
money = 100
money_multiplier = 0.2
frame_update = 2

root = tk.Tk()
root.title("Graj")
root.geometry("500x500")
root.minsize(100, 100)
root.update()


win_height = root.winfo_height()
win_width = root.winfo_width()

buildings = Buildings()

def startGame():
    start_screen.pack_forget()
    game_screen.pack(side=tk.TOP, expand=True)

def gameLoop(frame = 0):
    global money
    if root.state() == "iconic":
        buildings.minimiseAllWindows()
    elif root.state() == "normal":
        buildings.openAllWindows()

    money_label.config(text=f"Money: {int(money)}")
    population_label.config(text=f"Population: {buildings.population}")
    if frame % frame_update == 0:
        money += money_multiplier * buildings.population


    root.after(16, lambda:gameLoop(frame+1 if frame < 60 else 0))


#change use of maximise window
def moveUpWindows(a):
    if root.state() == 'zoomed':
        root.state("normal")
        buildings.moveAllWinToFirstPlan()

def buyBuilding():
    global money, buy_multiplier
    money -= buy_price()
    buy_multiplier += 1
    buildings.newBuilding(root)

root.bind("<Configure>", moveUpWindows)

#Main screen
start_screen = tk.Frame(root, width=100, height=100)
start_screen.pack(side=tk.TOP, expand=True)

start_gameButton = tk.Button(start_screen, text="Start", command=startGame)
start_gameButton.place(width=100 ,height=50, x=0, y=25)

#the other screen
game_screen = tk.Frame(root, width=root.winfo_width(), height=root.winfo_height())
game_screen.pack(side=tk.TOP, expand=True)
game_screen.pack_forget()

money_label = tk.Label(game_screen, text="Money: 0")
money_label.grid(row=0, column=0)

population_label = tk.Label(game_screen, text="Population")
population_label.grid(row=1, column=0)

buy_buildingsButton = tk.Button(game_screen, text="Buy", command=buyBuilding, width=10, height=2)
buy_buildingsButton.grid(row=2, column=0, rowspan=2, pady=10)


root.after(0, gameLoop)
root.mainloop()