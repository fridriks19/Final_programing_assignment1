import os 
fd = "fd.txt"
  
# popen() is similar to open() 
file = open(fd, 'a') 
file.write("\nHelloaa") 
file.close() 
file = open(fd, 'r') 
text = file.read() 
print(text) 
  
