import tkinter as tk

class infoWindow:
	def __init__(self, root, name = "No name", value = 1000):
		self.window = tk.Toplevel(root)
		self.window.transient(root)
		self.window.resizable(True,False)
		self.window.geometry("150x0")
		self.name = name
		self.window.title(f"{self.name} {value}")
		self.window.withdraw()
		self.window.protocol("WM_DELETE_WINDOW", lambda: 1)
	
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
		#print(f'+{x+self.x_offset}+{y+self.y_offset}')
		self.window.geometry(f'+{x+self.x_offset}+{y+self.y_offset}') 
		self.window.update_idletasks()
		self.window.lift()
  
class buttonWindow:
	def __init__(self, root, name = "Button", value = 0, command = lambda: print('you forgor to set command')):
		self.window = tk.Toplevel(root)
		self.window.transient(root)
		self.window.resizable(True,False)
		self.window.geometry("250x0")
		self.name = name
		self.window.title(f"{self.name} {value} ->")
		self.window.withdraw()
		self.window.protocol("WM_DELETE_WINDOW", command)
		self.window.command(lambda: print("command"))	
  
	def update_value(self, value):
		self.window.title(f"{self.name} {value} ->")
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
		#print(f'+{x+self.x_offset}+{y+self.y_offset}')
		self.window.geometry(f'+{x+self.x_offset}+{y+self.y_offset}') 
		self.window.update_idletasks()
		self.window.lift()
  
class UpgradeWindow:
	def __init__(self, root, name = "Button", command = lambda: print('you forgor to set command')):
		self.window = tk.Toplevel(root)
		self.window.transient(root)
		self.window.resizable(True,False)
		self.window.geometry("200x0")
		self.name = name
		self.level = 0
		self.window.title(f"{self.name} {self.level}")
		self.window.withdraw()
		self.window.protocol("WM_DELETE_WINDOW", lambda: command() and self.updateLevel())	

	def updateLevel(self):
		self.level +=	1
		self.window.title(f"{self.name} {self.level}")


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
  