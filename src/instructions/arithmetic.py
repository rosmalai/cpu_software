#Arithmatic operations 
from src.cpu.alu import ALU
class ArithmeticInstructions:
    def __init__(self, register):
        self.alu = ALU()
        self.register = register
        
    def alu_add(self, reg, value):
        current_value = self.register.get(reg)
        result = self.add(current_value, value)
        self.register.set(reg, current_value)
    def alu_sub(self, reg, value):
        current_value = self.register.get(reg, value)
        result = self.sub(current_value, value)
        self.register.set(reg, result)
    def alu_div(self, reg, value):
        current_value = self.register.get(reg, value)
        result = self.div(current_value, value)
        self.register.set(reg, result)
    def alu_mul(self, reg, value):
        current_value = self.register.get(reg, value)
        result = self.mul(current_value, value)
        self.register.set(reg, result)