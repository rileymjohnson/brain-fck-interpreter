from Tkinter import *
import tkMessageBox
import tkFileDialog
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
from tkFileDialog import asksaveasfilename
import sys
import webbrowser
import os

"""global variables"""
###############################################################
current_file = ""
cell_values = {}
"""the function for interpreting"""
###############################################################
def start(code="", inp="",output=""):
	cells = [0] * 2000 #sets the cells
	pointer = 0 #sets the pointer
	code_increment = -1 #used to iterate through the code
	value_increment = 0 #used to iterate through the input
	front_brackets = [] #lists the positions of all the front brackets
	forward_pairs = {} #matches the front brackets with the back brackets
	backward_pairs = {} #matches the back brackets with the front brackets
	while code_increment < len(code) -1:
		code_increment += 1
		if code[code_increment] == "[":
			front_brackets.append(code_increment)
		if code[code_increment] == "]":
			forward_pairs.update({front_brackets[len(front_brackets) - 1]:code_increment})
			backward_pairs.update({code_increment:front_brackets[len(front_brackets) - 1]})
			front_brackets.pop(len(front_brackets) - 1)
	code_increment = -1 #resets the incrementer
	while code_increment < len(code) -1:
		code_increment += 1
		if code[code_increment] == "+":
			cells[pointer] += 1
		elif code[code_increment] == "-":
			cells[pointer] -= 1
		elif code[code_increment] == "<":
			pointer -= 1
		elif code[code_increment] == ">":
			pointer += 1
		elif code[code_increment] == ",":
			if value_increment <= len(inp) - 1:
				cells[pointer] = ord(inp[value_increment])
				value_increment += 1
		elif code[code_increment] == ".":
			if cells[pointer] <= 255:
				output += chr(cells[pointer])
		elif code[code_increment] == "]":
			code_increment = backward_pairs[code_increment] - 1
		elif code[code_increment] == "[":
			if cells[pointer] == 0:
				code_increment = forward_pairs[code_increment]
	cell_values.clear()
	cell_it = -1
	while cell_it < len(cells) - 1:
		cell_it += 1
		if cells[cell_it] != 0:
			cell_values.update({cell_it:cells[cell_it]})
	return output
###############################################################

"""part of the program where the functions for interacting with the guis are made"""
###############################################################
def select_all():
	text.tag_add("sel","1.0","end")

def set_value():
	code = text.get("1.0",'end-1c')
	inp = txtinput.get()
	answertext.delete(1.0,END)
	answertext.insert(1.0,start(code, inp))
	txtinput.delete(0, END)

def undo():
	code = text.get("1.0",'end-1c')
	text.delete(1.0, END)
	text.insert(1.0, code[:len(code) - 1])


def save_as():
	 direc = asksaveasfilename()
	 if direc:
		f = file(direc,'w')
		f.write(text.get("1.0",'end-1c'))
		f.close()
		statustext.set(direc + "...")
		global current_file
		current_file = direc

def open():
	ans = askopenfilename()
	if ans:
		f = file(ans, 'r')
		text.delete(1.0,END)
		text.insert(1.0,f.read())
		f.close()
		statustext.set(ans + "...")
		global current_file
		current_file = ans
		cell_values.clear()

def save():
	if current_file != "":
		file(current_file, 'w').close()
		f = file(current_file,'w')
		f.write(text.get("1.0",'end-1c'))
		f.close()
	else:
		save_as()

def new():
	global current_file
	current_file = ""
	clear()
	cell_values.clear()

def clear():
	answertext.delete(1.0,END)
	text.delete(1.0,END)
	txtinput.delete(0, END)

def view_cells():
	cell_inp = ""
	for i in cell_values:
		cell_inp += str(i) + " : " + str(cell_values[i]) + "\n"
	cell_inp = cell_inp[:len(cell_inp) - 1]
	if cell_inp == "":
		cell_inp = "All cells are 0"
	to = Toplevel()
	to.resizable(width=FALSE, height=FALSE)
	to.title("Cells")
	cell_label = Label(to, text=cell_inp)
	cell_label.pack()
	button = Button(to, text="Close", command=to.destroy)
	button.pack()

def view_ascii():
	top = Toplevel()
	top.resizable(width=FALSE, height=FALSE)
	top.title("Ascii Table")
	ascii_label = Label(top, image=ascii_table_image)
	ascii_label.pack()
	button = Button(top, text="Close", command=top.destroy)
	button.pack()

def wiki():
	webbrowser.open('http://en.wikipedia.org/wiki/Brainfuck')
def further():
	webbrowser.open('http://skilldrick.co.uk/2011/02/why-you-should-learn-brainfuck-or-learn-you-a-brainfuck-for-great-good/')
def information():
	webbrowser.open('http://esolangs.org/wiki/Brainfuck')

def close():
	root.destroy()

def minimize():
	root.wm_state('iconic')

def explained():
	execfile("explain.py")

def nothing():
	print "I did something"

"""status bar changers"""
def eopen(event):
	statustext.set("open...")
def esave(event):
	statustext.set("save...")
def ecopy(event):
	statustext.set("copy...")
def epaste(event):
	statustext.set("paste...")
def ecut(event):
	statustext.set("cut...")
def eclear(event):
	statustext.set("clear...")
def normal(event):
	statustext.set("nothing abnormal...")

#tkinter window declare and format
###############################################################
root = Tk()
root.configure(background='#000099')
root.wm_title("brain**** interpreter")
root.geometry('{}x{}'.format(1000, 550))
root.resizable(width=FALSE, height=FALSE)

#tkinter global images
###############################################################
ascii_table_image = PhotoImage(file="images/ascii.gif")

#menu area
##############################################################
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="save as", command=save_as)
filemenu.add_command(label="save", command=save)
filemenu.add_separator()
filemenu.add_command(label="open", command=open)
filemenu.add_command(label="new", command=new)
filemenu.add_separator()
filemenu.add_command(labe="exit", command=close)


editmenu = Menu(menu)
menu.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label="undo", command=undo)
editmenu.add_separator()
editmenu.add_command(label="copy", command=lambda: root.event_generate('<Control-c>'))
editmenu.add_command(label="cut", command=lambda: root.event_generate('<Control-x>'))
editmenu.add_command(label="paste", command=lambda: root.event_generate('<Control-v>'))
editmenu.add_separator()
editmenu.add_command(label="select all", command=select_all)

viewmenu = Menu(menu)
menu.add_cascade(label="view", menu=viewmenu)
viewmenu.add_command(label="view ascii table", command=view_ascii)
viewmenu.add_command(label="view cells", command=view_cells)

windowmenu = Menu(menu)
menu.add_cascade(label="window", menu=windowmenu)
windowmenu.add_command(label="minimize", command=minimize)
windowmenu.add_command(label="close", command=close)

helpmenu = Menu(menu)
menu.add_cascade(label="help", menu=helpmenu)
helpmenu.add_command(label="brain**** explained",command=explained)

linksmenu = Menu(helpmenu)
helpmenu.add_cascade(label="helpful links", menu=linksmenu)
linksmenu.add_command(label="wikipedia", command=wiki)
linksmenu.add_command(label="information", command=information)
linksmenu.add_command(label="furthter reading", command=further)
##############################################################

#toolbar
##############################################################
toolbar = Frame(root)

openbutton=Button(toolbar, command=open)
openbutton.bind("<Enter>", eopen)
openbutton.bind("<Leave>", normal)
openphoto=PhotoImage(file="images/open.gif")
openbutton.config(image=openphoto,width="20",height="20")
openbutton.pack(side=LEFT, padx=0)

savebutton=Button(toolbar, command=save)
savebutton.bind("<Enter>", esave)
savebutton.bind("<Leave>", normal)
savephoto=PhotoImage(file="images/save.gif")
savebutton.config(image=savephoto,width="20",height="20")
savebutton.pack(side=LEFT, padx=0)

copybutton=Button(toolbar, command=lambda: root.event_generate('<Control-c>'))
copybutton.bind("<Enter>", ecopy)
copybutton.bind("<Leave>", normal)
copyphoto=PhotoImage(file="images/copy.gif")
copybutton.config(image=copyphoto,width="20",height="20")
copybutton.pack(side=LEFT, padx=0)

pastebutton=Button(toolbar, command=lambda: root.event_generate('<Control-v>'))
pastebutton.bind("<Enter>", epaste)
pastebutton.bind("<Leave>", normal)
pastephoto=PhotoImage(file="images/paste.gif")
pastebutton.config(image=pastephoto,width="20",height="20")
pastebutton.pack(side=LEFT, padx=0)

cutbutton=Button(toolbar, command=lambda: root.event_generate('<Control-x>'))
cutbutton.bind("<Enter>", ecut)
cutbutton.bind("<Leave>", normal)
cutphoto=PhotoImage(file="images/cut.gif")
cutbutton.config(image=cutphoto,width="20",height="20")
cutbutton.pack(side=LEFT, padx=0)

clearbutton=Button(toolbar, command=clear)
clearbutton.bind("<Enter>", eclear)
clearbutton.bind("<Leave>", normal)
clearphoto=PhotoImage(file="images/clear.gif")
clearbutton.config(image=clearphoto,width="20",height="20")
clearbutton.pack(side=LEFT, padx=0)

toolbar.pack(side=TOP, fill=X)
##############################################################

#text area and button
##############################################################
textspace = Frame(root, highlightbackground="#AEFCFC")
scrollbar = Scrollbar(textspace)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(textspace, wrap=WORD, yscrollcommand=scrollbar.set, height=15, width=135)
text.pack()
scrollbar.config(command=text.yview)
textspace.pack(pady=25)

inputlabel = Label(root, text="Input:")
inputlabel.pack()

txtinput = Entry(root)
txtinput.pack(pady=10)

gobutton = Button(root, text="go", command=set_value)
gobutton.pack(pady=15)

answerspace = Frame(root, highlightbackground="#AEFCFC")

answertext = Text(answerspace, height=5, width=135)
answertext.pack()
answerspace.pack(pady=25)
##############################################################

#status bar
##############################################################
statustext = StringVar()
statustext.set("nothing abnormal...")
status = Label(root, textvariable=statustext, bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
##############################################################

root.mainloop()
