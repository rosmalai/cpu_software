# ALU which actually handle all the arithmetic and logical operations

class ALU:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def div(self, a, b):
        if b ==0:
            raise ZeroDivisionError("Division by zero")
        return a // b
    def mul(self, a, b):
        return a * b
    def AND_op(self, a, b):                
        return a and b
    def OR_op(self, a, b):                 
        return a or b
    def NOT_op(self, a):                    
        return not a
    def XOR_op(self, a, b):                  
        return a ^ b