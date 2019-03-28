#!/usr/bin/env python3
import math
import random


def write_to_file(file_path):
    # It is good practice to use the "with" keyword when dealing with file objects.
    # The advantage is that the file is properly closed after its suite finishes, 
    # even if an exception is raised at some point.
    with open(file_path, "w") as file:
        for i in range(100000):
            v = math.sin(i * math.pi/80000) * 300 + random.randint(0, 40) + 280
            v = max(v, 0)
            v = int(min(v, 600))
            file.write("{}\n".format(v))
    # You should close the file and immediately free up any system resources used by it. 
    # If you don’t explicitly close a file, Python’s garbage collector will eventually 
    # destroy the object and close the open file for you, but the file may stay open 
    # for a while. Another risk is that different Python implementations will do this 
    # clean-up at different times.
    file.close()
