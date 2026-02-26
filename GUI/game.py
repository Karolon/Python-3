import tkinter as tk


class Buildings:
    def __init__(self):
        self.buildingCount = 0

    def newBuilding(self):
        root=tk.Tk()
        root.geometry("100x400")
        root.title("House")
        root.resizable(False, False)
        self.buildingCount += 1

        root.state("moving")
        root.mainloop()
