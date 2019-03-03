from tkinter import *

def write_slogan():
	print("Started")

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
		 font = "Helvetica 11").place(x=30, y=60)
Label(root, 
		 text="Landing environment settings",
		 fg = "blue",
		 font = "Helvetica 11").place(x=450, y=60)

Label(root, text="Learning rate (B/W 0.0 to 1.0):").place(x=30,y=100)
l_rate=Entry(root)
l_rate.place(x=250, y=100)

Label(root, text="Discount factor (B/W 0.0 to 1.0):").place(x=30,y=150)
d_rate=Entry(root)
d_rate.place(x=250, y=150)

Label(root, text="Environment Variables:").place(x=30, y=200)
env_var = Scale(root, from_=1, to=10, orient=HORIZONTAL)
env_var.place(x=250, y=180)

Label(root, text="Environment Actions:").place(x=30, y=250)
env_action = Scale(root, from_=4, to=10, orient=HORIZONTAL)
env_action.place(x=250, y=230)

Label(root, text="Training Epochs:").place(x=30, y=300)
t_epochs = Scale(root, from_=1, to=10, orient=HORIZONTAL)
t_epochs.place(x=250, y=280)

Label(root, text="No. of games to play:").place(x=30, y=350)
no_games = Scale(root, from_=1, to=100, orient=HORIZONTAL)
no_games.place(x=250, y=330)

Label(root, text="Load previous weights:").place(x=30, y=400)
var1 = IntVar()
Checkbutton(root, text="YES", variable=var1).place(x=250, y=400)
var2 = IntVar()
Checkbutton(root, text="NO", variable=var2).place(x=300, y=400)

Label(root, text="Save weights:").place(x=30, y=450)
var3 = IntVar()
Checkbutton(root, text="YES", variable=var3).place(x=250, y=450)
var4 = IntVar()
Checkbutton(root, text="NO", variable=var4).place(x=300, y=450)

Label(root, text="Frames per second:").place(x=450, y=100)
fps = Scale(root, from_=1, to=50, orient=HORIZONTAL)
fps.place(x=650, y=80)

Label(root, text="Simulation speed:").place(x=450, y=150)
sim_speed = Scale(root, from_=1, to=50,orient=HORIZONTAL)
sim_speed.place(x=650, y=130)

Label(root, text="Landing surface friction:").place(x=450, y=200)
Label(root, text="/ 10").place(x=760, y=200)
l_friction = Scale(root, from_=1, to=10,orient=HORIZONTAL)
l_friction.place(x=650, y=180)

Label(root, text="Leg spring torque:").place(x=450, y=250)
spring_tq = Scale(root, from_=1, to=100,orient=HORIZONTAL)
spring_tq.place(x=650, y=230)

Label(root, text="Spacecraft density").place(x=450, y=300)
rocket_den = Scale(root, from_=1, to=100,orient=HORIZONTAL)
rocket_den.place(x=650, y=280)

startbtn = Button(root, 
                   text="START", 
                   fg="green",
				   width=50,
                   command=quit)
startbtn.place(x=190, y=500)
stopbtn = Button(root,
                   text="STOP",
				   fg="red",
				   width=50,
                   command=quit)
stopbtn.place(x=190, y=550)
root.mainloop()

