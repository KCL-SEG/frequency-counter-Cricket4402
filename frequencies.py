"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(len(items)):
        x = str(items[i])
        if not(x in frequencies.keys()):
            frequencies.update(x, 1);
        else:
            frequencies.update(x, frequencies[x] +1);
    
    return frequencies
