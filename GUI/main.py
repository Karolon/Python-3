import tkinter as tk
from game import Buildings
from info_window import infoWindow, buttonWindow, UpgradeWindow
import winsound
from tkinter import messagebox

#game
upgrade_cheaper_buildings_level = 0
upgrade_profit_level = 0
buy_start_price = 100
buy_multiplier = 0 
money_multiplier = 0.2
buy_price = lambda bLevel: buy_start_price * (buy_multiplier)**1.5 * 1.8**(bLevel - upgrade_cheaper_buildings_level)
money_calculator = lambda: buildings.population * (money_multiplier + 0.05*upgrade_profit_level)
#how many frames to update (60/x)
frame_update = 2
#counter
money = 10000000
game_level = 0
population_milestones = [0] + [i**2*7+20 for i in range(30)]#[0, 50, 130, 230]

game_started = False
buttonList = []

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

def upgradeResidents():
    global money
    if money >= 100*2**(buildings.resident_upgrade_level+1):
        money -= 100*2**(buildings.resident_upgrade_level+1)
        buildings.population += sum(h.LEVEL for h in buildings.placed_buildingList)
        buildings.resident_upgrade_level += 1
        return True

def upgradeBuildingPrice():
    global money, upgrade_cheaper_buildings_level
    if money >= 100*3**(upgrade_cheaper_buildings_level+1):
        money -= 100*3**(+1)
        upgrade_cheaper_buildings_level += 1
        for i, b in enumerate(buttonList):
            b.update_value(int(buy_price(i+1)))
        return True

def upgradeProfit():
    global money, upgrade_profit_level
    if money >= 100*3**(upgrade_profit_level+1):
        money -= 100*3**(upgrade_profit_level+1)
        upgrade_profit_level += 1
        return True
   
    
def newBuyButton():
    x = game_level
    buy_button = buttonWindow(root, f"BUY  LEVEL {game_level}:", value=int(buy_price(game_level)), command=lambda: buyBuilding(x))
    buy_button.snapTo(root.winfo_x, root.winfo_y, y_offset=160+32*game_level, x_offset=25)
    buy_button.set()
    buttonList.append(buy_button)

#change use of maximise window
def moveUpWindows(a = any):
    if root.state() == 'zoomed' or a == 1:
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
    global game_started  
    for win in buildings.buildingList:
        win.deiconify()
    if game_started:
        population_info.window.deiconify()
        money_info.window.deiconify()

def windowMoved(a = any):
    global game_started  
    moveUpWindows()
    if game_started:
        money_info.updatePos()
        population_info.updatePos()
    for bButton in buttonList:
        bButton.updatePos()
    
def startGame():
    global game_started  
    game_screen.pack(side=tk.TOP, expand=True)
    start_screen.destroy()
    population_info.set()
    money_info.set()
    upgrade_profit.set()
    upgrade_residents.set()
    upgrade_cheaper_buildings.set()
    game_started = True
    root.after(0, gameLoop)
    
    
def gameLoop(frame = 0):
    global money, game_level

    money_info.update_value(int(money))
    population_info.update_value(buildings.population)
    
    if frame % frame_update == 0:
        money += money_calculator()
    
    if buildings.population >= population_milestones[0] or game_level >= buildings.max_horizontal_level:
        if len(population_milestones) == 1:
            messagebox.showwarning("GAME OVER", "you won")
            winsound.MessageBeep(winsound.MB_OK)
            return
        game_level += 1
        newBuyButton()
        del population_milestones[0]
    
    root.after(16, lambda:gameLoop(frame+1 if frame < 60 else 0))

def buyBuilding(level = 1):
    global money, buy_multiplier
    if money >= buy_price(level):
        money -= buy_price(level)    
        buy_multiplier += 1
        buildings.newBuilding(root, level=level, residents=10 + 5*(level-1))
        for i, bButton in enumerate(buttonList):
            bButton.update_value(int(buy_price(i+1)))
    else:
        winsound.MessageBeep(winsound.MB_ICONASTERISK)

#change state of children with root
root.bind("<Configure>", windowMoved)
root.bind("<Unmap>", minimiseWindows)
root.bind("<Map>", maximiseWindows)
root.bind("<FocusIn>", lambda x: moveUpWindows(1))

#Main screen
start_screen = tk.Frame(root, width=100, height=100)
start_screen.pack(side=tk.TOP, expand=True)

start_gameButton = tk.Button(start_screen, text="Start", command=startGame)
start_gameButton.place(width=100 ,height=50, x=0, y=25)

#game screen
game_screen = tk.Frame(root, width=root.winfo_width(), height=root.winfo_height())
game_screen.pack(side=tk.TOP, expand=True)
game_screen.pack_forget()

#upgrades
upgrade_residents = UpgradeWindow(root, "Resident upgrade", upgradeResidents)
upgrade_residents.snapTo(lambda: 0, lambda: 130)
upgrade_profit = UpgradeWindow(root, "Profit upgrade", upgradeProfit)
upgrade_profit.snapTo(lambda: 0, lambda: 165)
upgrade_cheaper_buildings = UpgradeWindow(root, "Cheap bricks upgrade", upgradeBuildingPrice)
upgrade_cheaper_buildings.snapTo(lambda: 0, lambda: 200)



print("mainloop")
root.mainloop()