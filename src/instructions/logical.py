#Logical operationsBit      
from src.cpu.alu import ALU
class LogicInstructions:
    def __init__(self, register):
        self.alu = ALU()         
        self.register = register

    def alu_AND(self, reg1, reg2):                
        a = self.register.get(reg1)
        b = self.register.get(reg2)
        result = self.alu.AND_op(a, b)
        self.register.set(reg1, result)
    def alu_OR(self, reg1, reg2):                 
        a = self.register.get(reg1)
        b = self.register.get(reg2)
        result = self.alu.OR_op(a, b)
        self.register.set(reg1, result)
    def alu_NOT(self, reg):                    
        a = self.register.get(reg)
        result = self.alu.NOT_op(a)
        self.register.set(reg, result)
    def alu_XOR(self, reg1, reg2):                  
        a = self.register.get(reg1)
        b = self.register.get(reg2)
        result = self.alu.XOR_op(a, b)
        self.register.set(reg1, result)
    def alu_SHL(self, reg, shift_by):
        a = self.register.get(reg)
        result = self.alu.SHL_op(a, shift_by)
        self.register.set(reg, result)
    def alu_SHR(self, reg, shift_by):
        a = self.register.get(reg)
        result = self.alu.SHR_op(a, shift_by)
        self.register.set(reg, result)

    

