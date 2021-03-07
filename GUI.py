import tkinter as tk
import os
from SendShot import SendShotApplication
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        
        self.master.title('SendShot')
        self.status=False
        self.status_color=tk.Label(self.master,text="---")
        self.status_color.config(foreground="red",background="red")
        self.status_color.pack(side="bottom")
        self.SShot=SendShotApplication()
        
        screen_width=self.master.winfo_screenwidth()
        screen_height=self.master.winfo_screenheight()
        self.master.geometry(f"400x200+{ (screen_width>>1) - 200 }+{ (screen_height>>1) - 100}")
        
        self.start_btn = tk.Button(self, text="Start",command=self.sendshot_start)
        self.start_btn.pack()

        self.stop_btn = tk.Button(self, text="Stop",command=self.sendshot_stop)
        self.stop_btn.pack()

        self.stop_btn = tk.Button(self, text="Quit", fg="red",command=self.sendshot_quit)
        self.stop_btn.pack()

    def background(self):
        self.SShot.sendshot()
        

    def sendshot_start(self):
        if self.status:
            return
        self.status=True
        self.status_color.config(foreground="green",background="green")
        self.status_color.pack(side="bottom")
        
        Thread(target=self.background).start()

    def sendshot_stop(self):
        if self.status==False:
            return
        self.status=False
        self.status_color.config(foreground="red",background="red")
        self.status_color.pack(side="bottom")
        
        self.SShot.stop()        

    def sendshot_quit(self):
        if self.status:
            self.SShot.stop()
        self.master.destroy()