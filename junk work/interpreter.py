"""This is an interpreter for the language brain****"""
import sys

#declares the cells (2000 of them from 0 - 1999)
cells = [0] * 2000

#pointer for which cell it's at
pointer = 0

#adds one to the current cell
#equivalent: +
def up():
   cells[pointer] += 1

#subtracts one from the current cell
#equivalent: -
def down():
   cells[pointer] -= 1
   
#moves over one cell to the left
#equivalent: >
def left():
   global pointer
   pointer += 1

#moves over one cell to the right
#equivalent: >
def right():
   global pointer
   pointer -= 1
   
#accepts an input from the user and inserts it into the current cell
#equivalent: ,
insnum = 0
def insert():
   global insnum
   if insnum > len(input) -1:
      return
   else:
      cells[pointer] = ord(input[insnum])
      insnum += 1

#outputs to the screen the value of the cell the pointer is on
#equivalent: .
def output():
   if cells[pointer] <= 255:
      a = chr(int(cells[pointer]))
      return a

code = []
input = []

def start(usercode, userinput=""):
   code[:] = [] #empties the lists so the function can be reused
   input[:] = [] #empties the lists so the function can be reused
   code1 = ""
   input1 = ""
   #takes the user inputted code and the inputs
   code1 = usercode #this gets the code
   input1 = userinput # this gets the inputs

   #appends the inputs in arrays
   for i in code1:
      code.append(i)
   for i in input1:
      input.append(i)

   #makes the dictionaries that allow the loops to know where to go
   front_brackets = []
   forward_pairs = {}
   backward_pairs = {}
   x = -1
   while x < len(code) -1:
      x += 1
      if code[x] == "[":
         front_brackets.append(x)
      if code[x] == "]":
         forward_pairs.update({front_brackets[len(front_brackets) - 1]:x})
         backward_pairs.update({x:front_brackets[len(front_brackets) - 1]})
         front_brackets.pop(len(front_brackets) - 1)

   out = ""
#starts the actual body and cli part of the program exluding the inputs
#these loops append code1 and input1 into arrays
   x = -1
   while x < len(code) - 1:
      x += 1
      #print "\n" + code[x] + str(x)
      #print "\npointer: " + str(pointer) + " number: " + str(cells[pointer]) + " value: " + str(code[x])
      if code[x] == ">":
         left()
      elif code[x] == "<":
         right()
      elif code[x] == "+":
         up()
      elif code[x] == "-":
         down()
      elif code[x] == ",":
         insert()
      elif code[x] == ".":
         a = output()
         if a:
            out += a
      elif code[x] == "[":
         if cells[pointer] == 0:
            x = forward_pairs[x]
      elif code[x] == "]":
         x = backward_pairs[x] - 1
      else:
         pass
   cells[:] = [0]
   return out
print start("++++++++[>+++++++++<-]>.")
print pointer
print start("++++++++[>+++++++++<-]>.")

