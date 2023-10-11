import math

class Main():
    def __init__(self):
        self.input = str(input("Input to be converted into binary: "))
        self.binary_conversion = []
        self.ascii_to_bits = {}
        self.powers_two = [1,2,4,8,16,32,64,128,256]
        return None

    def calculate_size(self) -> None:
        for char in self.input:
            ascii_code = ord(char)
            size_in_bytes = math.ceil(math.log2(ascii_code))
            self.ascii_to_bits[ascii_code] = size_in_bytes
        return None
    
    def convert(self) -> None:
        for key, value in self.ascii_to_bits.items():
            result = "0" * value
            max_value = self.powers_two.index(int(math.pow(2, value)))
            while key > 0:
                if (key - self.powers_two[max_value] > 0):
                    key -= self.powers_two[max_value]
                    result[-max_value] = "1"
                    max_value -= 1
                else:
                    max_value -= 1
                    continue
            self.binary_conversion.append(result)        
        return None

main = Main()
main.calculate_size()
main.convert()
for value in main.binary_conversion:
    print(value)
