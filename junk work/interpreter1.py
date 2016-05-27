cells = [0] * 2000 #makes the cells
pointer = 0 #sets the pointer equals to zero

def up(): #adds one to the current cell; equivalent: +
	cells[pointer] += 1

def down(): #subtracts one from the current cell; equivalent: -
	cells[pointer] -= 1

def left(): #moves one cell to the left; equivalent: <
	global pointer
	pointer -= 1

def right(): #moves one cell to the right; equivalent: >
	global pointer 
	pointer += 1

def out(): #returns the ascii value of the current cell; equivalent: .
	if cells[pointer] <=255:
		return chr(cells[pointer])

def put(inp): #set the current cell equal to the input; equivalent: ,
	cells[pointer] = ord(inp)

def start(code, value):
	code_increment = -1
	value_increment = 0
	output = ""
	while code_increment < len(code) -1:
		code_increment += 1
		if code[code_increment] == "+":
			up()
		elif code[code_increment] == "-":
			down()
		elif code[code_increment] == "<":
			left()
		elif code[code_increment] == ">":
			right()
		elif code[code_increment] == ",":
			if value_increment < len(value):
				put(value[value_increment])
				value_increment += 1
		elif code[code_increment] == ".":
			output = output + out()
	return output
print start("+++++++++++++++++++++++++++++++++.>,.", "riley")