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
	return output