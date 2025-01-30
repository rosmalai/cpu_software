#Arithmatic operations 
from cpu.alu import ALU
class ArithmeticInstructions:
    def __init__(self, register):
        self.alu = ALU()
        self.register = register
    def alu_add(a, b):
        return a + b
    def alu_sub(a, b):
        return a - b
    def alu_div(a, b):
        return a // b
    def alu_mul(a, b):
        return a * b