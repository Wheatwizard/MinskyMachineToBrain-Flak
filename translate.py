a = """
D 1 2 4
"""


def wrap(code, lineno):
	return "(({})[(())%s]){((<{}{}>))}{}{%s}{}"%("()"*lineno,code)
	

if __name__ == "__main__":
	result = ""
	instructions = a.strip().split("\n")
	for lineno,instruction in enumerate(instructions):
		print instruction
		if instruction == "H":
			#Halt is the same thing as goto 0
			code = "((<{}{}>))"
		elif instruction[0] == "I":
			register = int(instruction.split(" ")[1])
			nextInstruction = int(instruction.split(" ")[2])
			code = "(<{}{}%s>)"%("({}<"*(register)+"({}())"+">)"*(register)+"("+"()"*nextInstruction+")")
		elif instruction[0] == "D":
			register = int(instruction.split(" ")[1])
			fInstruction = int(instruction.split(" ")[2])
			tInstruction = int(instruction.split(" ")[3])
			code = "(<{}{}%s>)"%("({}<"*register+"(({}[()]))"+">)(({}({}))[({}[{}])])"*register+"({}(<()>)){(<{}({}%s[%s])>)}{}({}%s)"%("()"*fInstruction,"()"*tInstruction,"()"*tInstruction))
		result += wrap(code,lineno)

print "(()){"+result+"}{}"
