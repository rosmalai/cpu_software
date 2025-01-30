#Register actually act as a memory for temporary data store this we can create using array or list or stack...

class Register:
    def __init__(self):
        self.registers={
            "R0":0,
            "R1":0,
            # ..
            "PC":0,    #Program Counter
            "SP":0     #Stack Pointer
        }
        
    def get(self, reg):
        self.registers[reg]
    def set(self, reg, value):
        self.registers[reg] = value
    def move(self, reg1, reg2):
        self.registers[reg2] = self.registers[reg1]
    def clear(self, reg):
        self.registers[reg] = 0
    