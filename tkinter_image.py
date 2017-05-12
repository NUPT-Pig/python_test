from Tkinter import *
from PIL import Image, ImageTk
root = Tk()

img=PhotoImage(file='/home/anshun/python/excise/1.png')
#image = Image.open('2.jpg')
#img = ImageTk.PhotoImage(image)

button = Button(root, image=img, height=100, width=50)
button.image = img

button.pack()

root.mainloop()