from Tkinter import *
root = Tk()
root.title('first test window')
#root.geometry('300x200')

frm = Frame(root)

frm_l = Frame(frm)
Label(frm_l, text='left_top').pack(side=TOP)
Label(frm_l, text='left_bottom').pack(side=BOTTOM)
frm_l.pack(side=LEFT)

frm_r = Frame(frm)
Label(frm_r, text='right_top').pack(side=TOP)
Label(frm_r, text='right_bottom').pack(side=BOTTOM)
frm_r.pack(side=RIGHT)

frm.pack(side=TOP)
##########################################################
frm1 = Frame(root)

var = StringVar()
Entry(frm1, textvariable=var).pack(side=TOP)
var.set('entry text')

t = Text(frm1)
t.pack(side=TOP)

def print_entry():
    t.insert(END, var.get())

Button(frm1, text='copy', command=print_entry).pack(side=TOP)

frm1.pack(side=TOP)
##########################################################
frm2 = Frame(root)

redbutton = Button(frm2, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frm2, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frm2, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(frm2, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

frm2.pack(side=TOP)
######################################################
frm3 = Frame(root)

b = Button(frm3, text='move')
b.place(bordermode=OUTSIDE, height=100, width=100, x=50, y=50)
b.pack()

frm3.pack(side=TOP)
root.mainloop()
