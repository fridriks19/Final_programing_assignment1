WITDH = 30
LENGTH = 10
PAGE = "*"
HEADER = "NaN Air"
CHANGE = "'1' - Change"
MAKE_NEW = "'2' - Make new"
HEADER_PLACEMENT =WITDH- len(HEADER) 
USER_INPUT= ("Users input:")


def line_placement(WITDH, line):
    space = int((WITDH- len(line))/2)
    return space




################Fyrri gerð af blaðsíðu######################################## ########################## ########################## ########################## 
# print("*"*WITDH)
# for i in range(LENGTH):
#     print("{}{:>29}".format(PAGE,PAGE))  # geri 29 því 30 gerir einum of mörg bil    WITDH = 30// 
# print(PAGE*WITDH)



##############Seinni gerð########################## ########################## ########################## ########################## ########################## 

#########HEADER
print(PAGE*30 + "\n" #Efsta línan
    + PAGE + " "* int(HEADER_PLACEMENT/2) + HEADER +    #HEADER gætum inputað eh inn í hann  // Header placement bæði fyrir framan og aftan til að fá rétt magn af bilum
                " "* int((HEADER_PLACEMENT/2)-1)        #Geri -1 því án þess kemur auka bil! og                        
                + PAGE + "\n"   # endin á miðju línu 
    + PAGE*30)  #Neðsta lína                              

            #  " "*(WITDH-2-len(HEADER)*2)

# #rest of page
# for i in range(LENGTH):
#     print(PAGE + " "*(WITDH-2) + PAGE)      # Geri -2 því án þess koma tvo auka bil!
#     print(CHANGE)
# print(PAGE*WITDH)



######EFRI HLTUI BLAÐSÍÐUNAR        
for i in range(int(LENGTH/2)):
    print(PAGE + " "*(WITDH-2) + PAGE)      # Geri -2 því án þess koma tvo auka bil!

#Change textinn
print(PAGE + " "* (line_placement(WITDH, CHANGE)) + CHANGE +    # ntoum def falliuð í staðinn fyrir að hard codea þetta 
        " "* (line_placement(WITDH, CHANGE)-2)        # -2 til að losna við bilin                       
        + PAGE)
#input textinn
print(PAGE + " "* (line_placement(WITDH, MAKE_NEW)) + MAKE_NEW +    # ntoum def falliuð í staðinn fyrir að hard codea þetta 
        " "* (line_placement(WITDH, MAKE_NEW)-2)        # -2 til að losna við bilin                       
        + PAGE)

######NEÐRI HLUTI AF Blaðsíðunni 
for i in range(int(LENGTH/2)):   
    print(PAGE + " "*(WITDH-2) + PAGE)
print(PAGE*30)


###################################################################################################################### ########################## ########################## 
