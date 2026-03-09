import tkinter as tk
from tkinter import messagebox

class Buildings:
    def __init__(self, upgradeWin = any):
        #self.upgradeWin = upgradeWin
        self.cursor_x, self.cursor_y = 0, 0 
        self.buildingList = []
        self.placed_buildingList = []
        #temp window for getting screen data
        temp =tk.Tk()
        temp.withdraw()
        temp.state("zoomed")
        temp.attributes("-alpha", 0)
        temp.update()
        #diffriend sizes
        self.screen_width = temp.winfo_screenwidth()
        self.screen_height = temp.winfo_screenheight()
        self.taskbarHeight = temp.winfo_screenheight() - temp.winfo_height()
        self.proportions = self.screen_width//self.screen_height
        temp.destroy()
        #preloading images
        self.house_image = tk.PhotoImage(file = "tall_house.png")
        self.house_image_disabled = tk.PhotoImage(file = "tall_house_disabled.png")
        self.blank = tk.PhotoImage(file="blank.png")
        self.top = tk.PhotoImage(file="building_top.png")
        self.middle = tk.PhotoImage(file="building_middle.png")
        self.bottom = tk.PhotoImage(file="building_bottom.png")
        self.top_disabled = tk.PhotoImage(file="building_top_disabled.png")
        self.middle_disabled = tk.PhotoImage(file="building_middle_disabled.png")
        self.bottom_disabled = tk.PhotoImage(file="building_bottom_disabled.png")
        #game
        self.population = 0
        self.resident_upgrade_level = 0
        self.max_vertical_level = (self.screen_height - self.taskbarHeight - 148) // 72
        self.max_horizontal_level = (self.screen_width - self.taskbarHeight - 148) // 72
 
    
    def newBuilding(self, root, residents = 5, level = 1):
        
        def placeBuilding():
            nonlocal placed_flag, house, residents, level
            placed_flag = True
            self.placed_buildingList.append(house_win)
            house.pack()
            house_disabled.pack_forget()
            self.population += self.resident_upgrade_level + residents * [1, self.proportions+1][level>self.max_vertical_level]
            

        def moveBuilding():
            nonlocal placed_flag, residents
            if placed_flag:
                placed_flag = False
                self.placed_buildingList.remove(house_win)
                self.population -= self.resident_upgrade_level + residents * [1, self.proportions+1][level>self.max_vertical_level]
                house.pack_forget()
                house_disabled.pack()
                
        def move(a):
            x = min(max(a.x_root-self.cursor_x-8, -8), self.screen_width-house_win.winfo_width())
            y = min(max(a.y_root-self.cursor_y-31, 0), self.screen_height-house_win.winfo_height()-self.taskbarHeight)
            x, y = checkCollision(x, y, 0)
            house_win.geometry(f'+{x}+{y}')
            
        def start_moving(a):
            self.cursor_x  = a.x
            self.cursor_y  = a.y
            if self.screen_height != house_win.winfo_screenheight():
                temp = tk.Tk()
                temp.withdraw()
                temp.state("zoomed")
                temp.attributes("-alpha", 0)
                temp.update()
                self.screen_width = temp.winfo_screenwidth()
                self.screen_height = temp.winfo_screenheight()
                self.taskbarHeight = temp.winfo_screenheight() - temp.winfo_height()
                print(self.screen_width, self.screen_height, self.taskbarHeight, house_win.winfo_height())
                temp.destroy()
            moveBuilding()

        def stop_moving(a):
            if -5 <= self.screen_height - house_win.winfo_height() - self.taskbarHeight - 8 <= house_win.winfo_y():
                placeBuilding()

        def sell():
            if messagebox.askyesno("Sell Building", "Are you sure you want to sell this building?\nYou won`t get the money back"):
                nonlocal residents, level
                self.buildingList.remove(house_win)
                if placed_flag:
                    self.placed_buildingList.remove(house_win)
                    self.population -=  self.resident_upgrade_level + residents * [1, self.proportions+1][level>self.max_vertical_level]
                house_win.destroy()

        def checkCollision(x, y, depth):
            #limiter of recursion starts from 0
            if depth > 1:
                return None
            #flags
            yFlag, xFlagL, xFlagR = False, False, False
            new_x = x
            #height of the moving window
            height = house_win.winfo_height()
            #The moving building`s bottom left and right x cordinates and bottom y cordinates
            Left = x 
            Right = x + house_win.winfo_width()
            Down = y + height
            #checks collisions with every building
            for building in self.placed_buildingList:
                #checks y collision only from top
                if Down > building.winfo_y():
                    #left and right x of placed building
                    bL = building.winfo_x()
                    bR = bL + building.winfo_width()
                    #check for collision from the left side
                    if Right >= bL and Right <= bR:
                        xFlagL = True
                        new_x = bL - house_win.winfo_width() - 1
                    #check for collisions from the right side
                    if Left >= bL and Left <= bR:
                        new_x= bR + 1
                        xFlagR = True
                    #check if it is actualy from top
                    if (house_win.winfo_y() + height < building.winfo_y() and (xFlagL or xFlagR)) or (xFlagR and xFlagL):
                        yFlag = True
                        y = min(y, building.winfo_y() - height -1)

            
            #checks if the new position is viable 
            if not yFlag:
                if new_x != x:
                    x_, y_ = checkCollision(new_x, y, depth+1)
                    if new_x != x_ or y_ != y:
                        x = x_ 
                        y = y_
            
            if xFlagL and not xFlagR and not yFlag:
                x = new_x
            elif xFlagR and not xFlagL and not yFlag:
                x = new_x
                

            return x, y

        #FOR TRACING PUTPOSES
        placed_flag = False
        #set up window
        house_win=tk.Toplevel(root)
        house_win.geometry(f"133x{148+level*72}")
        house_win.title("House")
        house_win.resizable(False, False)
        house_win.attributes("-transparentcolor", "white")
        house_win.iconphoto(False, self.blank)
        #binds
        house_win.bind("<Button-1>", start_moving)
        house_win.bind("<B1-Motion>", move)
        house_win.bind("<B1-ButtonRelease>", stop_moving)
        #backgroud image
        house = tk.Canvas(house_win, width=132, height=148+level*72, bg="white")
        house.create_image(0 , 0, anchor=tk.NW, image=self.top)
        for i in range(level):
            house.create_image(0, 48+72*(i), anchor=tk.NW, image=self.middle)
            
        house.create_image(0 , 48+72*(level), anchor=tk.NW, image=self.bottom)
        house.pack()
        house.pack_forget()
        #disabled bg image
        house_disabled = tk.Canvas(house_win, width=132, height=148+level*72, bg="white")
        house_disabled.create_image(0 , 0, anchor=tk.NW, image=self.top_disabled)
        for i in range(level):
            house_disabled.create_image(0, 48+72*(i), anchor=tk.NW, image=self.middle_disabled)
            
        house_disabled.create_image(0 , 48+72*(level), anchor=tk.NW, image=self.bottom_disabled) 
        house_disabled.pack()
        
        # hideLabel = tk.Label(house_win, image = self.house_image_disabled, bg="black", pady=0)
        # buidling_topLabel.place(x = 0, y = 0)
        house_win.protocol("WM_DELETE_WINDOW", sell)
        house_win.LEVEL = level
        self.buildingList.append(house_win)
        
