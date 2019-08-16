# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:09:57 2019

@author: User
"""
import tkinter as tk
import display
import threading
import time
#from PIL import ImageTk,Image

count=0

def clickOK():
    global count
    count+=1;
    label.config(text="Click OK " + str(count) + " times")

def toolBar_Animation():
    th=threading.Thread(target=Animation)
    th.setDaemon(True)
    th.start()
    
def Animation():
    while(1):
        #hide or show toolbar 
        if(count%2 == 1):
            display.toolbar.hide()
        else:
            display.toolbar.show()
        
        display.homepage.time()    
            
            
        
        time.sleep(0.005)
        #label.config(text="GG")


display = Display()
label=tk.Label(display.root, text="Hello World!", font=("Arial",12))

GG=tk.Button(display.root, text="sh", command=clickOK, width=5, height=2)
GG.place(x=100, y=100)
toolBar_Animation()


label.pack(side='bottom')


display.root.mainloop()


