import tkinter as tk

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

uinote = tk.Message(
    master=frame,
    text="Note",
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

window.mainloop()