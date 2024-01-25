# from tkinter import *
# from tkinter import messagebox
import pyautogui

top = Tk()
top.resizable(False,False)

def helloCallBack():
    pyautogui.click()
    print("this")
   
B = Button(top, text ="Hello", command = helloCallBack)
B.place(x=50,y=50)
top.mainloop()