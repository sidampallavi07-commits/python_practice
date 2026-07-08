# file handling
# mode: r - read ,w -write, a - append

#open file
#file = open ("example.txt","r") # how to open a file


#file = open ("example.txt","r") 
#content = file.read()#read entire data
#print(content)
#file.close() # best practice

#file=open("example2.txt","r")
#content=file.readlines() # read first line 
#print(content)
#file.close()

#write to a file

#file=open("example2.txt","w") # this is wite mode --over writes
#file.write("hi..this is pallavi, sidam here")

#file.close()

from ast import With
from tkinter.filedialog import Open


file=open("example2.txt","a") # append mode - incremental line add in next line 
file.write("\nagain good evning")

file.close()

# close a file
# using with statement
with open ("example2.txt","r") as file:
    content=file.readline()
    print(content)