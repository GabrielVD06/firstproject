import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(" ")
    result = ""
    for i in range(0,len(words)):
        letras = words[i]
        letras = letras.replace(letras[0],letras[0].upper())
        result += letras + " "

    return(result)
    
if __name__ == '__main__':


    s = input()

    result = solve(s)

    print(result)