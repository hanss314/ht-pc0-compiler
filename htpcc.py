import sys
import argparse
import os
from instructionlist import *


def asm_compile(input_file,output_file):
	reader = open(input_file,"r")
	instructions = reader.read().lower().replace('\n','').replace(' ','').split(";")
	writer = open(output_file,"w")
	for instruction in instructions:
		try:
			if not instruction == "":
				writer.write(INSTRUCTION_LIST[instruction]+"\n")
		except KeyError:
			#os.remove(output_file)
			print(input_file+':'+str(instructions.index(instruction))+': parse error on \"'+instruction+'\"' )
			sys.exit()
			
		
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file")
	parser.add_argument("output_file")
	args = parser.parse_args()
	asm_compile(args.input_file,args.output_file)


if __name__ == "__main__":
	main()