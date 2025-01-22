#File Handling

import os
file = open("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt", "r")
print(file.read())
file.close()

import os
file = open("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt", "r")
print(file.read(7))
file.close()

import os
file = open("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt", "r")
print(file.readlines())
file.close()

import os
file = open("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt", "r")
print(file.readline())
file.close()

import os
file = open("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt", "r")
print(file.read())
file.close()

import os
file = open("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt", "w")
file.write("Today is Monday\n")
file.write("Thursday is my birthday\n")
file.close()

import os
file = open("C:/Users/Dell/Downloads/Sirisha Allarapu/nani.txt", "x")
file.write("Sunday is Republic day")
file.close()

import os 
os.remove("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt")

import os
if os.path.exists("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt"):
    os.remove("C:/Users/Dell/Downloads/Sirisha Allarapu/mynote.txt")
else:
    print("file not exists")

