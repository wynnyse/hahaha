import tkinter as tk
from auth import Auth

#run here
# no no touch sa accounts.txt

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Label Demo")
        self.geometry("800x600")
        Auth(self)

def main():
    
    app = MyApp()
    app.mainloop()

main()
