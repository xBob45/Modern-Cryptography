#!/usr/bin/python3

__author__ = "Vojtech Moravec"
__email__ = "xmorav45@vutbr.cz"

from math import gcd

class DecisionalDiffieHellman():
    def __init__(self, modulo : int, generator : int, j_instance : tuple):
        self.modulo = modulo
        self.generator = generator
        self.j_instance = j_instance

        self.computation()
    
    def computation(self):

        # 1) We calculate order of the group (number of its elements) -> φ({n} and establish pool of values from which we'll be drawing x and y.
        available_values = []
        
        for number in range(1,self.modulo):
            if gcd(number, self.modulo) == 1: # If that's the case a number and the modulo are coprime and thus number is a member of the group.
                available_values.append(number)
            else : continue

        
        # 2) Now, we'll try every combination of x and y from our pool of available values and check whether the pair yilds the given instance j.
        is_yes_instance = False
        for x in available_values:
            for y in available_values:
                a = (self.generator**x) % self.modulo
                b = (self.generator**y) % self.modulo
                c = (self.generator**(x*y)) % self.modulo

                if(tuple((a,b,c)) == tuple(self.j_instance)):
                    is_yes_instance = True
                    print(f"j is yes-instance, certificate is: {tuple((x,y))}.")
                    break
        
        if not is_yes_instance:
            print(f"j is no-instance.")



if __name__ == "__main__":
    obj = DecisionalDiffieHellman(11,6,(9,3,4))

