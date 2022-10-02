"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        x = str(items[i])
        if(frequencies[x] == None):
            frequencies[x] = 1;
        else:
            frequencies[x] = frequencies[x] + 1;
    
    return frequencies
