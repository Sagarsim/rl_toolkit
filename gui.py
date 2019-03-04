from tkinter import *
from threading import Thread
import os
import sys

''' 
+str(fps.get())+" "
+str(sim_speed.get())+" "
+str(spring_tq.get())+" "
+str(l_friction.get())+" "
+str(rocket_den.get())+" "
+str(l_rate_val.get())+" "
+str(d_rate_val.get())+" "
+str(env_var.get())+" "
+str(env_action.get())+" "
+str(t_epochs.get())+" "
+str(no_games.get())+" "
'''    
#control = Controller()
root = Tk()
root.geometry("800x700+30+30")



class Controller(object):
    def __init__(self):
        self.param=None
        self.my_thread=None
        self.par_array=[]
    def start_in_thread(self):
        self.my_thread = Thread(target=self.start_training)
        self.my_thread.daemon = True
        self.my_thread.start()
        startbtn.configure(state=DISABLED)
    def start_training(self):
        self.par_array = [str(fps.get())+" ",
        str(sim_speed.get())+" ",
        str(spring_tq.get())+" ",
        str(l_friction.get()/10)+" ",
        str(rocket_den.get())+" ",
        str(l_rate_val.get())+" ",
        str(d_rate_val.get())+" ",
        str(t_epochs.get())+" ",
        str(no_games.get())+" "]
        
        if var1.get() == 1:
            self.par_array.append(str(1)+" ")
        else: self.par_array.append(str(0)+" ")
        if var3.get() == 1:
            self.par_array.append(str(1)+" ")
        else: self.par_array.append(str(0)+" ")    
        self.param="python3 env.py "+"".join(self.par_array)
        print(self.param)
        os.system(self.param)
    def stop_training(self):
        sys.platform == "win32" and os.system("taskkill /f /IM env.py") or os.system("pkill -f env.py")
        startbtn.configure(state=NORMAL)
    def default_params(self):
        fps.set(50)
        sim_speed.set(30)
        l_friction.set(1)
        spring_tq.set(40)
        rocket_den.set(5)
        l_rate_val.set(0.003)
        d_rate_val.set(0.99)
        t_epochs.set(3)
        no_games.set(100)
        var1.set(1)
        var3.set(1)
    def model(self):
        imgwin = Tk()
        img = PhotoImage(master = imgwin, file="model_plot.png")
        panel = Label(imgwin, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        imgwin.mainloop()


control=Controller()	

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
l_rate_val=DoubleVar()
l_rate=Entry(root, textvariable=l_rate_val)
l_rate.place(x=250, y=100)

Label(root, text="Discount factor (B/W 0.0 to 1.0):").place(x=30,y=150)
d_rate_val=DoubleVar()
d_rate=Entry(root, textvariable=d_rate_val)
d_rate.place(x=250, y=150)

Label(root, text="Training Epochs:").place(x=30, y=200)
t_epochs = Scale(root, from_=1, to=10, orient=HORIZONTAL)
t_epochs.place(x=250, y=180)

Label(root, text="No. of games to play:").place(x=30, y=250)
no_games = Scale(root, from_=1, to=500, orient=HORIZONTAL)
no_games.place(x=250, y=230)

Label(root, text="Load previous weights:").place(x=30, y=300)
var1 = IntVar()
Checkbutton(root, text="YES", variable=var1).place(x=250, y=300)
var2 = IntVar()
Checkbutton(root, text="NO", variable=var2).place(x=300, y=300)

Label(root, text="Save weights:").place(x=30, y=350)
var3 = IntVar()
Checkbutton(root, text="YES", variable=var3).place(x=250, y=350)
var4 = IntVar()
Checkbutton(root, text="NO", variable=var4).place(x=300, y=350)

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
                   command=control.start_in_thread)
startbtn.place(x=190, y=500)

stopbtn = Button(root, 
                   text="STOP", 
                   fg="red",
				   width=50,
                   command=control.stop_training)
stopbtn.place(x=190, y=550)

defbtn = Button(root,
                   text="SET DEFAULT PARAMETERS",
				   fg="blue",
				   width=50,
                   command=control.default_params)
defbtn.place(x=190, y=600)
defbtn = Button(root,
                   text="NEURAL NETWORK MODEL",
				   fg="blue",
				   width=50,
                   command=control.model)
defbtn.place(x=190, y=650)



root.mainloop()

