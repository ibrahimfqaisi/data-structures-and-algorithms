def insertShiftArray(arrr, val):
    if (len(arrr) % 2) == 1:
        middle_index = (int(len(arrr) / 2)) + 1
    else:
        middle_index = int(len(arrr) / 2)
    new_list = arrr[:middle_index] + [val] + arrr[middle_index:]
    print(new_list)
insertShiftArray([2,4,6,-8], 5)
insertShiftArray([42,8,15,23,42], 16)

def removesElementMiddle(arrr):
    if (len(arrr) % 2) == 1:
        middle_index = (int(len(arrr) / 2)) 
    else:
        middle_index = int(len(arrr) / 2)
    new_list = arrr[:middle_index]+ arrr[middle_index+1:]
    print(new_list)
removesElementMiddle([2,4,6,-8])
removesElementMiddle([42,8,15,23,42])
