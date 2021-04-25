import tkinter as tk
from numpy import random

class Chopstick(object):
    def __init__(self, taken):
        self.taken = taken

class Philosopher(object):
    def __init__(self, name, isthinking, rchops, lchops, iseating, stilleating):
        self.name = name
        self.isthinking = isthinking
        self.rchops = rchops
        self.lchops = lchops
        self.iseating = iseating
        self.stilleating = stilleating
    
    def hungry(self):
        # if self.rchops.taken == True and self.lchops.taken == True:
        if self.iseating == True:
            isover = random.randint(0, 3)
            over = random.randint(0, 3)
            if isover == over:
                self.rchops.taken = False
                self.lchops.taken = False
                self.iseating = False
                self.isthinking = True
                self.stilleating = False
                print(f"{self.name} {self} : put down both of chopstick and start to think again")
        else:
            if self.rchops.taken == False:
                self.rchops.taken = True
                self.isthinking = False
                print(f"{self.name} {self} : picked up right chopstick")
            else:
                if self.lchops.taken == False:
                    self.lchops.taken = True
                    self.iseating = True
                    self.stilleating = True
                    print(f"{self.name} {self} : picked up left chopstick and start to eat pasta...")

One = Chopstick(False)
Two = Chopstick(False)
Three = Chopstick(False)
Four = Chopstick(False)
Five = Chopstick(False)

Aristotles = Philosopher("Aristotles", True, Five, One, False, False)
Socrates = Philosopher("Socrates", True, One, Two, False, False)
Thales = Philosopher("Thales", True, Two, Three, False, False)
Democritus = Philosopher("Democritus", True, Three, Four, False, False)
Zeno = Philosopher("Zeno", True, Four, Five, False, False)

chopsticks = [One, Two, Three, Four, Five]
philosophers = [Aristotles, Socrates, Thales, Democritus, Zeno]

window = tk.Tk()
window.title("Philosopher Dining Hall")

frame = tk.Frame(master=window, width=500, height=500)
frame.pack()

uidemocritus = tk.Label(
    master=frame, 
    text="Democritus", 
    bg="green",
    fg="white",
    width=25,
    height=5
)
uidemocritus.place(x=125, y=0)

uithales = tk.Label(
    master=frame,
    text="Thales",
    bg="green",
    fg="white",
    width=25,
    height=5
)
uithales.place(x=0, y = 130)

uizeno = tk.Label(
    master=frame,
    text="Zeno of Elea",
    bg="green",
    fg="white",
    width=25,
    height=5
)
uizeno.place(x=250, y = 130)

uisocrates = tk.Label(
    master=frame,
    text="Socrates",
    bg="green",
    fg="white",
    width=25,
    height=5
)
uisocrates.place(x=0, y = 230)

uiaristotles = tk.Label(
    master=frame,
    text="Aristotles",
    bg="green",
    fg="white",
    width=25,
    height=5
)
uiaristotles.place(x=250, y = 230)

uiphilosophers = [uiaristotles, uisocrates, uithales, uidemocritus, uizeno]

uinote = tk.Message(
    master=frame,
    text="Note"
)
uinote.place(x=0, y=343)

uithinking = tk.Message(
    master=frame,
    text="thinking",
    bg="green",
    fg="white",
    width=50
)
uithinking.place(x=0, y=380)

uihungry = tk.Message(
    master=frame,
    text="hungry",
    bg="yellow",
    fg="blue"
)
uihungry.place(x=70, y=380)

uieating = tk.Message(
    master=frame,
    text="eating",
    bg="red",
    fg="white",
    width=50
)
uieating.place(x=140, y=380)

def issame(philointerface, philobject, m, n):
    window.after(500, play)
    getnumber = random.randint(0, 5)
    # print(getnumber)
    if m == n:
        if philobject[getnumber].rchops == True:
            philobject[getnumber].hungry()
            if philobject[getnumber].stilleating == True:
                philointerface[getnumber].config(bg="red", fg="white")
            else:
                philointerface[getnumber].config(bg="green", fg="white")
        else:
            philobject[getnumber].hungry()
            philointerface[getnumber].config(bg="yellow", fg="blue")
    elif m != n and philobject[getnumber].isthinking == True:
        philointerface[getnumber].config(bg="green", fg="white")
        print(f"{philobject[getnumber].name} {philobject[getnumber]} : Thinking")

def play():
    stnumber = random.randint(0, 3)
    ndnumber = random.randint(0, 3)
    issame(uiphilosophers, philosophers, stnumber, ndnumber)

window.after(500, play)
window.mainloop()