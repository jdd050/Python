import matplotlib.pyplot as plt
import re, math

class Main:
    def __init__(self, equation):
        # define equation strings
        self.equation = re.sub(r" ", r"", equation)
        return None
    
    # retrieve vWin size
    def getDomain(self):
        # get canvas
        window = plt.get_current_fig_manager()
        vWinCanvas = window.canvas
        # get dimensions
        dimensions = vWinCanvas.get_width_height()
        xCoorIter = -dimensions[0]
        # create xCoord list
        self.domain = []
        while xCoorIter <= dimensions[0]:
            self.domain.append(xCoorIter)
            xCoorIter += 0.05
        return self.domain
    
    # translate operators
    def translateOps(self):
        # initial conditions
        matchDict = {"nestedMatches":re.findall(r"\d+" + r"[a-zA-Z]", self.equation),
                     "distNumMatches":re.findall(r"\d+\(", self.equation),
                     "distVarMatches":re.findall(r"[a-zA-Z]+\(", self.equation),
                     "powMatches":re.findall(r"\^" + r"\d+", self.equation),
                     "factorialMatches":re.findall(r"\d+\!", self.equation)
                     }
        
        # loop until cleaned
        while matchDict.values() != []:
            # nested multiplication w/ coeff
            matchDict["nestedMatches"] = re.findall(r"\d+" + r"[a-zA-Z]", self.equation)
            print(matchDict["nestedMatches"], " nested")
            for match in matchDict["nestedMatches"]:
                nestedMatchStr = f"{match[-2]}*{match[-1]}"
                self.equation = re.sub(match, nestedMatchStr, self.equation)
            
            # distributive property number
            matchDict["distNumMatches"] = re.findall(r"\d+\(", self.equation)
            print(matchDict["distNumMatches"], " distributive num")
            for match in matchDict["distNumMatches"]:
                distMatchStr = f"{match[-2]}*{match[-1]}"
                self.equation = re.sub(re.escape(match), distMatchStr, self.equation)

            # distributive property variable
            matchDict["distVarMatches"] = re.findall(r"[a-zA-Z]+\(", self.equation)
            print(matchDict["distVarMatches"], " distributive var")
            for match in matchDict["distVarMatches"]:
                distMatchStr = f"{match[-2]}*{match[-1]}"
                self.equation = re.sub(re.escape(match), distMatchStr, self.equation)
            
            # pow
            matchDict["powMatches"] = re.findall(r"\^" + r"\d+", self.equation)
            print(matchDict["powMatches"], " pow")
            for match in matchDict["powMatches"]:
                powMatchStr = f"**{match[-1]}"
                self.equation = re.sub(re.escape(match), powMatchStr, self.equation)
                
            # factorial
            matchDict["factorialMatches"] = re.findall(r"\d+\!", self.equation)
            print(matchDict["factorialMatches"], " factorial")
            for match in matchDict["factorialMatches"]:
                cleanFactorial = re.sub("!", "", match)
                # calculate any operations and convert to int
                try:
                    clearOp = int(eval(cleanFactorial))
                    calcFactorial = math.factorial(clearOp)
                except OverflowError:
                    print("Overflow Error. Factorial args entered exceed 2_147_383_647 in value.")
                    exit()
                # replace with calculated value
                self.equation = re.sub(match, str(calcFactorial), self.equation)
                
            return self.equation

    # find variable letter for eval() global declaration
    def findVar(self):
        for char in self.equation:
            if char.isalpha() == True:
                self.eqVar = char
                break
            

    # calculate values given f(x)
    def evalFunction(self):
        # create dictionary of values and find var char
        Main.findVar(self)
        self.funcValues = {}
        # calculate func value and add to dict
        for coord in self.domain:
            value = eval(self.equation, {}, {self.eqVar: coord}) 
            self.funcValues[coord] = value
            
        return self.funcValues 


# get equation
equation = input("Enter equation:\n")
while equation == "":
    equation = input("Enter equation:\n")
    pass

# func calls
main = Main(equation)
domain = main.getDomain()
cleanedEq = main.translateOps()
funcValues = main.evalFunction()
print(funcValues)
print(cleanedEq)