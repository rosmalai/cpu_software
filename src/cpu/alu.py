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
        return a & b
    def OR_op(self, a, b):                 
        return a | b
    def NOT_op(self, a):                    
        return  ~a
    def XOR_op(self, a, b):                  
        return a ^ b
    def SHL_op(a, b):   #a -> the data 
        return a << b   #b -> no of bit position  we want to shift
    def SHR_op(a, b):
        return a >> b