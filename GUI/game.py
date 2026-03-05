import tkinter as tk

class Buildings:
    def __init__(self):
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
        temp.destroy()
        #preloading images
        self.house_image = tk.PhotoImage(file = "tall_house.png")
        self.house_image_disabled = tk.PhotoImage(file = "tall_house_disabled.png")
        #game
        self.population = 0
    
    def newBuilding(self, root, residents = 5):


        def placeBuilding():
            nonlocal placed_flag, background_label, residents
            placed_flag = True
            self.placed_buildingList.append(house_win)
            background_label.config(image=self.house_image)
            self.population += residents

        def moveBuilding():
            nonlocal placed_flag, background_label, residents
            if placed_flag:
                placed_flag = False
                background_label.config(image=self.house_image_disabled)
                self.placed_buildingList.remove(house_win)
                self.population -= residents
        
        def move(a):
            x = min(max(a.x_root-self.cursor_x-8, -8), self.screen_width-house_win.winfo_width())
            y = min(max(a.y_root-self.cursor_y-31, 0), self.screen_height-house_win.winfo_height()-self.taskbarHeight)
            x, y = checkCollision(x, y, 0)
            house_win.geometry(f'+{x}+{y}')
            
        def start_moving(a):
            self.cursor_x  = a.x
            self.cursor_y  = a.y
            moveBuilding()

        def stop_moving(a):
            if self.screen_height - house_win.winfo_height() - self.taskbarHeight - 8 <= house_win.winfo_y():
                placeBuilding()

        def sell():
            nonlocal residents
            self.buildingList.remove(house_win)
            if placed_flag:
                self.placed_buildingList.remove(house_win)
                self.population -= residents
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


        placed_flag = False
        #set up window
        house_win=tk.Toplevel(root)
        house_win.geometry("132x279")
        house_win.title("House")
        house_win.resizable(False, False)
        house_win.wm_attributes("-transparentcolor", "white")
        #binds
        house_win.bind("<Button-1>", start_moving)
        house_win.bind("<B1-Motion>", move)
        house_win.bind("<B1-ButtonRelease>", stop_moving)
        #backgroud image
        background_label = tk.Label(house_win, image = self.house_image_disabled, bg="white")
        background_label.place(x = 0, y = 0)
        house_win.protocol("WM_DELETE_WINDOW", sell)
        
        self.buildingList.append(house_win)
        
