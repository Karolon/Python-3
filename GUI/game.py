import tkinter as tk

class Buildings:
    def __init__(self):
        self.cursor_x, self.cursor_y = 0, 0 
        self.windowList = []
        temp =tk.Tk()
        temp.withdraw()
        self.screen_width = temp.winfo_screenwidth()
        self.screen_height = temp.winfo_screenheight()
        temp.destroy()
        self.house_image = tk.PhotoImage(file = "tall_house.png")
        
        
        
    def newBuilding(self, root):

        def placeBuilding():
            print('placed')

        def move(a):
            taskBarSize = house_win.winfo_height() - house_win.winfo_y()
            print(taskBarSize)
            house_win.geometry(f'132x279+{min(max(a.x_root-self.cursor_x-8, -8), self.screen_width-house_win.winfo_width())}+{min(max(a.y_root-self.cursor_y-31, 0), self.screen_height-house_win.winfo_height())}')
            
        def start_moving(a):
            self.cursor_x  = a.x
            self.cursor_y  = a.y

        def stop_moving(a):
            if self.screen_height - house_win.winfo_height() == house_win.winfo_y():
                placeBuilding()

        house_win=tk.Toplevel(root)
        house_win.geometry("132x279")
        house_win.title("House")
        house_win.resizable(False, False)
        background_label = tk.Label(house_win, image = self.house_image, bg="white")
        background_label.place(x = 0, y = 0)
        house_win.wm_attributes("-transparentcolor", "white")
        house_win.wm_attributes()
        house_win.bind("<Button-1>", start_moving)
        house_win.bind("<B1-Motion>", move)
        house_win.bind("<B1-ButtonRelease>", stop_moving)
        self.windowList.append(house_win)
        
    def openAllWindows(self):
        for window in self.windowList:
            window.state("normal")
        
    def minimiseAllWindows(self):
        for window in self.windowList:
            window.iconify()
    
    def moveAllWinToFirstPlan(self):
        for window in self.windowList:
            window.lift()