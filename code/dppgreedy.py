import time
import tkinter as tk
import pandas as pd
from numpy import random
from matplotlib import pyplot as plt


class Chopstick(object):
    def __init__(self, taken):
        self.taken = taken

class Philosopher(object):
    def __init__(self, name, isthinking, rchops, lchops, iseating, hunglevel, counteat):
        self.name = name
        self.isthinking = isthinking
        self.rchops = rchops
        self.lchops = lchops
        self.iseating = iseating
        self.hunglevel = hunglevel
        self.counteat = counteat


One = Chopstick(False)
Two = Chopstick(False)
Three = Chopstick(False)
Four = Chopstick(False)
Five = Chopstick(False)

Aristotles = Philosopher("Aristotles", True, Five, One, False, 3, 0)
Socrates = Philosopher("Socrates", True, One, Two, False, 3, 0)
Thales = Philosopher("Thales", True, Two, Three, False, 3, 0)
Democritus = Philosopher("Democritus", True, Three, Four, False, 3, 0)
Zeno = Philosopher("Zeno", True, Four, Five, False, 3, 0)

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

count = 0

def issame(philointerface, philobject):
    getnumber = random.randint(0, 5)
    philo = philosophers[getnumber]
    uiphilo = uiphilosophers[getnumber]
    window.after(250, play)
    if philo.lchops.taken == False and philo.rchops.taken == False:
        print(philo.name, "eating")
        uiphilo.config(bg="red", fg="white")
        philo.lchops.taken = True
        philo.rchops.taken = True
        philo.iseating = True
        philo.thinking = False
        philo.counteat += 1
    elif philo.iseating == True:
        philo.hunglevel -= 1
        if philo.hunglevel == 0:
            philo.hunglevel = 3
            philo.lchops.taken = False
            philo.rchops.taken = False
            philo.iseating = False
            philo.thinking = True
            print(philo.name, "Thinking again.")
            uiphilo.config(bg="green", fg="white")
    else:
        philo.isthinking = False
        print(philo.name, "hungry")
        uiphilo.config(bg="yellow", fg="blue")


def play():
    issame(uiphilosophers, philosophers)

window.after(250, play)
window.mainloop()

df = pd.DataFrame({
    "aristotles" : [Aristotles.counteat],
    "socrates" : [Socrates.counteat],
    "thales" : [Thales.counteat],
    "democritus" : [Democritus.counteat],
    "zeno" : [Zeno.counteat]
}, index= [0])

data = [
    Aristotles.counteat, Socrates.counteat,
    Thales.counteat, Democritus.counteat,
    Zeno.counteat
]
xval = range(len(data))

labels = [
    Aristotles.name, Socrates.name,
    Thales.name, Democritus.name,
    Zeno.name
]
print(df)
# plt.bar(xval, data)
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.show()
# while True:
#     getnumber = random.randint(0, 5)
#     philo = philosophers[getnumber]
#     time.sleep(1)
#     if philo.lchops.taken == False and philo.rchops.taken == False:
#         print(philo.name, "eating")
#         philo.lchops.taken = True
#         philo.rchops.taken = True
#         philo.iseating = True
#         philo.thinking = False
#     elif philo.iseating == True:
#         philo.hunglevel -= 1
#         if philo.hunglevel == 0:
#             philo.hunglevel = 3
#             philo.lchops.taken = False
#             philo.rchops.taken = False
#             philo.iseating = False
#             philo.thinking = True
#             print(philo.name, "Thinking again.")
#     else:
#         philo.isthinking = False
#         print(philo.name, "hungry")