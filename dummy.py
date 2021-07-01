import tkinter  as tk 
from tkinter import *
my_w = tk.Tk()
my_w.geometry("200x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

my_str = tk.StringVar()
l1 = tk.Label(my_w,  textvariable=my_str, width=10 )
l1.grid(row=1,column=2,columnspan=6) 

def my_fun(k):
    my_str.set("Btn No is : "+ str(k) )    

n=10 # number of buttons
i=2
for j in range(n):
    e = Button(my_w, text=j,command=lambda k=j: my_fun(k)) 
    e.grid(row=i, column=j) 
            
my_w.mainloop()  # Keep the window open