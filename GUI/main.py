import tkinter as tk
from game import Buildings
from info_window import infoWindow, buttonWindow
import winsound

#game
buy_start_price = 100
buy_multiplier = 0
money_multiplier = 0.2
buy_price = lambda: buy_start_price * 1.7**(buy_multiplier)
#how many frames to update (60/x)
frame_update = 2
#counter
money = 100

#inisilise root
root = tk.Tk()
root.title("Graj")
root.geometry("300x500")
root.minsize(100, 100)
root.maxsize(300, 500)
root.update()

#constats so i wont need to get it every time
win_height = root.winfo_height()
win_width = root.winfo_width()

#bind my classes
buildings = Buildings()
population_info = infoWindow(root, "Population:")
population_info.snapTo(root.winfo_x, root.winfo_y, y_offset=50, x_offset=75)
money_info = infoWindow(root, "Money:")
money_info.snapTo(root.winfo_x, root.winfo_y, y_offset=83, x_offset=75)


#globals so that funcion work
hidden_windows = []


#change use of maximise window
def moveUpWindows(a = any):
    if root.state() == 'zoomed':
        root.state("normal")
        windowList = root.tk.call("wm", "stackorder", ".")
        for window in windowList:
            win = root.nametowidget(window)
            win.lift(root)
            
def minimiseWindows(a = any):
    windowList = root.tk.call("wm", "stackorder", ".")
    for window in windowList:
        win = root.nametowidget(window)
        hidden_windows.append(win)
        win.iconify()
        
def maximiseWindows(a = any):  
    for win in buildings.buildingList:
        win.deiconify()
    population_info.window.deiconify()
    money_info.window.deiconify()

def windowMoved(a = any):
    moveUpWindows()
    money_info.updatePos()
    population_info.updatePos()
    buy_button.updatePos()
    
    
def startGame():
    game_screen.pack(side=tk.TOP, expand=True)
    start_screen.destroy()
    
    population_info.set()
    money_info.set()
    buy_button.set()
    
def gameLoop(frame = 0):
    global money, testInfo

    money_info.update_value(int(money))
    population_info.update_value(buildings.population)
    
    if frame % frame_update == 0:
        money += money_multiplier * buildings.population
    
    
    root.after(16, lambda:gameLoop(frame+1 if frame < 60 else 0))

def buyBuilding(a = any):
    global money, buy_multiplier
    if money >= buy_price():
        money -= buy_price()
        buy_multiplier += 1
        buildings.newBuilding(root)
    else:
        winsound.MessageBeep(winsound.MB_ICONASTERISK)

#change state of children with root
root.bind("<Configure>", windowMoved)
root.bind("<Unmap>", minimiseWindows)
root.bind("<Map>", maximiseWindows)


#Main screen
start_screen = tk.Frame(root, width=100, height=100)
start_screen.pack(side=tk.TOP, expand=True)

start_gameButton = tk.Button(start_screen, text="Start", command=startGame)
start_gameButton.place(width=100 ,height=50, x=0, y=25)

#game screen
game_screen = tk.Frame(root, width=root.winfo_width(), height=root.winfo_height())
game_screen.pack(side=tk.TOP, expand=True)
game_screen.pack_forget()

buy_button = buttonWindow(root, "BUY  ->", buyBuilding)
buy_button.snapTo(root.winfo_x, root.winfo_y, y_offset=160, x_offset=75)
# buy_buildingsButton = tk.Button(game_screen, text="Buy", command=buyBuilding, width=10, height=2)
# buy_buildingsButton.grid(row=2, column=0, rowspan=2, pady=10)


root.after(0, gameLoop)
print("mainloop")
root.mainloop()