## Code Challenge / Algorithm
### arguments: 2 link list



## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/240038134-b244f2d4-f537-4701-974a-d5f865ebfbc5.jpg)
## Approach & Efficiency

The provided code implements an approach to merge two linked lists into a single linked list. Here's an analysis of the approach and its efficiency:

1. The code iterates over both input lists simultaneously, alternating between adding elements from `list1` and `list2` to the `lst` list. This ensures that the elements are merged in the desired order.

2. After merging the elements into the `lst` list, a new linked list `llZip` is created. The elements from `lst` are inserted into `llZip` in reverse order using the `insert` method.

3. Finally, the string representation of `llZip` is printed and returned.

The time complexity of this approach can be analyzed as follows:

- Merging the elements from `list1` and `list2` into the `lst` list takes O(N) time, where N is the total number of elements in both lists. This is because the code iterates over each element in both lists once.

- Inserting the elements from `lst` into the `llZip` linked list also takes O(N) time, as each element in `lst` is inserted once.

Therefore, the overall time complexity of the approach is O(N), where N is the total number of elements in both lists.

The space complexity of the approach is also O(N), as the `lst` list is used to store the merged elements before inserting them into the `llZip` linked list.

## Solution
    ```
        def zipLists(list1, list2):
                lst = []
                curr_01 = list1.head
                curr_02 = list2.head
                x=1
                while x==1:
                    check2=0
                    check1=0
                    if curr_01 != None:
                        lst.append(curr_01.value)
                        curr_01 = curr_01.next
                    else:
                        check1 = 1
                    if curr_02 != None:
                        lst.append(curr_02.value)
                        curr_02 = curr_02.next       
                    else:
                        check2 = 1
                        
                    if check1== 1 and check2 == 1:
                        x= 0
                llZip=linked_list()          
                for x in lst[::-1]:
                    llZip.insert(x)
            
                print(llZip.to_string())
                return (llZip.to_string())
            ```
