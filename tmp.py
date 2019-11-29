WITDH = 30
LENGTH = 20
PAGE = "*"
page = ""


#Fyrri gerð af blaðsíðu
print("*"*WITDH)
for i in range(LENGTH):
    print("{}{:>29}".format(PAGE,PAGE))
print(PAGE*WITDH)
    

#Seinni gerð 
print(PAGE*WITDH)
for i in range(LENGTH):
    print(PAGE + " "*(WITDH-2) + PAGE)      # Geri -2 því án þess koma tvo auka bil 
print(PAGE*WITDH)
    

