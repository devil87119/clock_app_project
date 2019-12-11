 # -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:09:57 2019

@author: User
"""
import tkinter as tk
from  display_and_toolbar import *
#import threading
#import time
#import pandas as pd
#from PIL import ImageTk,Image

'''def toolBar_Animation():
        th=threading.Thread(target=Animation) 
        th.setDaemon(True)
        th.start()
        
def Animation():
    global count
    while(1):
        #hide or show toolbar 
        if(count%2 == 1):
            display.toolbar.hide()
         else:
            display.toolbar.show()
        
        display.homepage.time()
        display.homepage.refresh_weather()                     
        
        time.sleep(0.005)
        #label.config(text="GG")'''

display = Display()
#label=tk.Label(display.root, text="Hello World!", font=("Arial",12))

#GG=tk.Button(display.root, text="sh", command=clickOK, width=5, height=2)
#GG.place(x=100, y=100)
#toolBar_Animation()
#toolBar_Animation()  

#label 

display.root.mainloop()


