"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in items:
        str = string(items[i])
        if(frequencies[str] == None):
            frequencies[str] = 1;
        else:
            frequencies[str] = frequencies[str] + 1;
    
    return frequencies
