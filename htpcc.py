import sys
import argparse
import os
from instructionlist import *
from string import ascii_lowercase


def asm_compile(input_file,output_file):

	reader = open(input_file,"r")
	instructions = reader.read().lower().replace(' ','').split("\n")
	writer = open(output_file,"w")
	writer.write("v2.0 raw\n")
	
	initialize_end=0
	registers_set=0
	initial_vars = {}
	
	for initializer in instructions:
		if initializer in INSTRUCTION_LIST:
			initialize_end=instructions.index(initializer)
			break 
		else:
			if not initializer=="":
				initial_vars[initializer[0]]=initializer[2:]
				registers_set+=1
				
			if registers_set==7:
				initialize_end=instructions.index(initializer)
	
			
	for i in ascii_lowercase[0:8]:
		try:
			if int(initial_vars[i])<16:
				writer.write("0")
			writer.write(hex(int(initial_vars[i])).split("x")[1]+"\n")
		except KeyError:
			writer.write("00\n")
			
	
	for i in range(initialize_end,len(instructions)):
		instruction = instructions[i]
		try:	
			if not instruction == "":
				writer.write(INSTRUCTION_LIST[instruction]+"\n")
		except KeyError:
			#os.remove(output_file)
			try:
				writer.write(hex(int(instruction)+191).split("x")[1].upper()+"\n")
			except ValueError:
				print(input_file+':'+str(i)+': parse error on \"'+instruction+'\"' )
				sys.exit()
			
		
			
def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("input_file")
	parser.add_argument("output_file")
	args = parser.parse_args()
	asm_compile(args.input_file,args.output_file)


if __name__ == "__main__":
	main()