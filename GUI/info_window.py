import tkinter as tk

class infoWindow:
	def __init__(self, root, name = "No name", value = 1000):
		self.window = tk.Toplevel(root)
		self.window.geometry("250x0")
		self.name = name
		self.window.title(f"{self.name} {value}")
		self.window.withdraw()
	
	def update_value(self, value):
		self.window.title(f"{self.name} {value}")
		self.window.update()
		
	def set(self):
		self.window.deiconify()

	def snapTo(self, xcommand, ycommand, x_offset=0, y_offset=31):
		self.xcommand = xcommand
		self.ycommand = ycommand
		x = xcommand()
		y = ycommand()
		self.x_offset = x_offset
		self.y_offset = y_offset
		self.window.geometry(f'+{x+self.x_offset}+{y+self.y_offset}') 
  
	def updatePos(self):
		x = self.xcommand()
		y = self.ycommand()
		print(f'+{x+self.x_offset}+{y+self.y_offset}')
		self.window.geometry(f'+{x+self.x_offset}+{y+self.y_offset}') 
		self.window.update()
		self.window.lift()