from tkinter import *

root = Tk()
root.geometry("800x700+30+30") 
Label(root, 
		 text="SPACECRAFT LANDING SIMULATION",
		 fg = "green",
         bg = "light green",
		 font = "Helvetica 12").pack(ipadx=400, ipady=15)
Label(root, 
		 text="Deep Q-learning parameter settings",
		 fg = "blue",
		 font = "Helvetica 11").place(x=90, y=60)
Label(root, 
		 text="Landing environment settings",
		 fg = "blue",
		 font = "Helvetica 11").place(x=450, y=60)

l = Label(root, text="Learning rate (B/W 0 to 1):")
l_rate=Entry(root)
l.place(x=30,y=100)
l_rate.place(x=250, y=100)

l2 = Label(root, text="Discount factor (B/W 0 to 1):")
d_rate=Entry(root)
l2.place(x=30,y=150)
d_rate.place(x=250, y=150)

l3 = Label(root, text="Environment Variables:")
l3.place(x=30, y=200)
env_var = Scale(root, from_=1, to=10, orient=HORIZONTAL)
env_var.place(x=250, y=180)

l3 = Label(root, text="Environment Actions:")
l3.place(x=30, y=250)
env_action = Scale(root, from_=4, to=10, orient=HORIZONTAL)
env_action.place(x=250, y=230)

l4 = Label(root, text="Training Epochs:")
l4.place(x=30, y=300)
t_epochs = Scale(root, from_=1, to=10, orient=HORIZONTAL)
t_epochs.place(x=250, y=280)

l4 = Label(root, text="No. of games to play:")
l4.place(x=30, y=350)
t_epochs = Scale(root, from_=1, to=100, orient=HORIZONTAL)
t_epochs.place(x=250, y=330)

l5 = Label(root, text="Load previous weights:")
l5.place(x=30, y=400)

var1 = IntVar()
Checkbutton(root, text="YES", variable=var1).place(x=250, y=400)
var2 = IntVar()
Checkbutton(root, text="NO", variable=var2).place(x=300, y=400)

l6 = Label(root, text="Save weights:")
l6.place(x=30, y=450)

var1 = IntVar()
Checkbutton(root, text="YES", variable=var1).place(x=250, y=450)
var2 = IntVar()
Checkbutton(root, text="NO", variable=var2).place(x=300, y=450)

root.mainloop()