from Tkinter import *

root = Tk()
frame = Frame(root, height=500, width=500)
frame.pack()

def move():
    print (redbutton.winfo_y())
    redbutton.flash()
    redbutton.place(x=0, y=redbutton.winfo_y()+5)

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack()
redbutton.place(bordermode=OUTSIDE, height=100, width=100, x=0, y=0)


greenbutton = Button(frame, text="Green", fg="green", command=move)
greenbutton.pack()
greenbutton.place(bordermode=OUTSIDE, height=100, width=100, x=100, y=0)

root.mainloop()