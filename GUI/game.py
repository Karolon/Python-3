import tkinter as tk


class Buildings:
    def __init__(self):
        self.buildingCount = 0
        self.cursor_x, self.cursor_y = 0, 0 
        self.windowList = []
        temp =tk.Tk()
        temp.withdraw()
        self.screen_width = temp.winfo_screenwidth()
        self.screen_height = temp.winfo_screenheight()
        temp.destroy() 
        
        
        
    def newBuilding(self, root):
        
        def move(a):
            house_win.geometry(f'150x400+{min(max(a.x_root-self.cursor_x-8, -8), self.screen_width-house_win.winfo_width())}+{min(max(a.y_root-self.cursor_y-31, 0), self.screen_height-house_win.winfo_height())}')
            
        def start_moving(a):
            self.cursor_x  = a.x
            self.cursor_y  = a.y
           
        house_win=tk.Toplevel(root)
        house_win.geometry("150x400")
        house_win.title("House")
        house_win.resizable(False, False)
        self.buildingCount += 1
        house_win.bind("<Button-1>", start_moving)
        house_win.bind("<B1-Motion>", move)
        self.windowList.append(house_win)
        
    def openAllWindows(self):
        for window in self.windowList:
            window.state("normal")
            #window.deiconify()
        
    def minimiseAllWindows(self):
        for window in self.windowList:
            #window.state("iconic")
            window.iconify()
    
    def moveAllWinToFirstPlan(self):
        for window in self.windowList:
            window.lift()