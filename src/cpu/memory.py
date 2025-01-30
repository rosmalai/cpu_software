class Memory:
    def __init__(self, size = 1000):
        self.memory = [0] * size         #Initialize memory with a fixed size locations & all set to

        def read(self, address):
            if 0<= address < len(self.memory):
                return self.memory[address]
            else:
                raise ValueError("Invalid address")
        def write(self, address, value):
            if 0 <= address < len(self.memory):
                self.memory[address] = value
            else:
                raise ValueError("Invalid address")
        def clear(self, address):
            self.memory[address] = 0
        def dump(self):
            for address, value in enumerate (self.memory):
                print(f"Address:{address}: {value}")            #Print the entire   memory content
