curr_fn = "NA022"
curr_fn = curr_fn.split("A")

counter = int(curr_fn[1]) + 1

flug_list = [["f1"],["f2"],["f3"],["f4"],["f5"],["f6"]]
for i in flug_list:
    flight_num = "NA{0:0=3d}".format(counter)
    i.append(flight_num)
    counter += 1
print(flug_list)