# Challenge Title
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process

![photo](https://user-images.githubusercontent.com/125550572/236331981-66a10767-7bf1-4eec-bd26-fab28f2f7c82.jpg)

## Approach & Efficiency
### insertShiftArray:
 Calculates the middle index of an array and creates a new list with the given value inserted at that index. Time complexity is O(n) where n is the length of the input array.
### removesElementMiddle:
 Calculates the middle index of an array and creates a new list with the middle element(s) removed. Time complexity is also O(n) where n is the length of the input array.

 ## Solution
 ```
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

```
 