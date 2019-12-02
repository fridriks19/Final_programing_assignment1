def change(newlist, user_input):
    change = user_input
    if user_input == "1":
        change = newlist[0]
    if user_input == "2":
        change = newlist[1]
    if user_input == "3":
        change = newlist[2]
    if user_input == "4":
        change = newlist[3] 
    if user_input == "5":
        change = newlist[4] 
    while change != "r":
        print(change)


a_list = [3009907461,"William Carillo","Pilot","Captain","NAFokkerF100","Fellsmúli 1",8998801]

user_input = "1"
new_list =change(a_list, user_input)

# ssn,name,role,rank,licence,address,phonenumber