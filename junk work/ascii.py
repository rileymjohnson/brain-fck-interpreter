from Tkinter import *

root = Tk()
root.wm_title("ascii table")
root.resizable(width=FALSE, height=FALSE)
ascii_table = PhotoImage(file="images/ascii.gif")
label = Label(image=ascii_table)
label.image = ascii_table
label.pack()
root.mainloop()