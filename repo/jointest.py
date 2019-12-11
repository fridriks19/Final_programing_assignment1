str1 = ""
listlist = [["aaa,sss,ddd,fff,ggg,hhh,jjj"],["qqq,uuu,iii,ttt,fff,ccc,sss"]]
for line in listlist:
    line = "".join(line)
    str1 += line+"\n"
print(str1)