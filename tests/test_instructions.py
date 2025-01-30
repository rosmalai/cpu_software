from src.instructions.arithmetic import ArithmeticInstructions
from src.instructions.logical import LogicInstructions
from src.cpu.registers import Register


#Initialize Registers, Arithmatic Instruction and Logical Instruction 
register = Register()
arithmatic = ArithmeticInstructions(register)
logical = LogicInstructions(register)

register.set("R0", 10)
arithmatic.alu_add("R0", 5)