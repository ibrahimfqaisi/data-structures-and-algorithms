## append
### arguments: new value
### adds a new n

## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/238453626-ea57dca8-adcb-4a93-92aa-63c3805d1283.jpg)
## Approach & Efficiency

The append method in the provided code snippet is used to add a value to the end of a linked list. It iterates through the list until it reaches the last node and then appends a new node with the given value. The time complexity of this method is O(n) and the space complexity is O(1), where n is the number of nodes in the linked list.
## Solution
    ```
       def append(self,value):
                current=self.head
                if current==None :
                    self.insert(value)
                    
                else:
                    while current!=None:
                        if current.next==None:
                            current.next= Node(value)
                            return
                        current=current.next
    ```

### insert after
## arguments: value, new value
## adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/238453699-6b1431cc-d806-427d-8450-7a598cda9216.jpg)
## Approach & Efficiency

The after method in the provided code snippet is used to insert a new node with a given value after a specific node in a linked list. It iterates through the list to find the desired node, and then inserts the new node immediately after it. The time complexity of this method is O(n), and the space complexity is O(1), where n is the number of nodes in the linked list.
## Solution
    ```
        def after(self,value,_next):
                current=self.head
                if current==None :
                    self.insert(value)
                    
                else:
                    while current!=None:   
                        if current.value== str(value):
                            print("gffu")
                            old_current_next=current.next
                            current.next= Node(_next,old_current_next)
                            break 
                        
                        current=current.next
    ```


### insert after
## arguments: value, new value
## adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/238453699-6b1431cc-d806-427d-8450-7a598cda9216.jpg)
## Approach & Efficiency


The Before method in the provided code snippet is used to insert a new node with a given value before a specific node in a linked list. It traverses the list to find the node just before the desired node and inserts the new node before it. The time complexity of this method is O(n), and the space complexity is O(1), where n is the number of nodes in the linked list.
## Solution
```
   def Before(self,value,_next):
        current=self.head
        if current.value == str(value):
           self.insert(_next) 
           return
        while current.next!=None:   
            if current.next.value== str(value):
                old_current_next=current.next
                current.next= Node(_next,old_current_next)
                
                break 
            current=current.next                
```                    


### kth from end
## arguments: a number, k, as a parameter.
## Return the node’s value that is k places from the tail of the linked list.


## Whiteboard Process
![photo](https://user-images.githubusercontent.com/125550572/238771864-7db8c603-de0d-48b1-a00d-799c406599b5.jpg)
## Approach & Efficiency

### Approach:

Traverse the linked list from the head to the tail, storing the values in a list.
Check if the value of k is within the range of the list's indices.
If it is within the range, return the value at index k in the list.
If it is out of range, raise an exception.

Efficiency:

Time complexity: The time complexity of this approach depends on the length of the linked list. Let's assume the length of the linked list is n. The traversal of the linked list takes O(n) time, and the insertion at the beginning of the list in each iteration using list.insert(0, value) takes O(n) time as well. Therefore, the overall time complexity of the approach is O(n^2).
Space complexity: The space complexity is also O(n) because the values of the linked list are stored in a list, which requires additional space proportional to the length of the linked list.
## Solution
```
      def kth(self, k):
        current = self.head
        lst = []

        while current is not None:
            lst.insert(0, current.value)
            current = current.next

        if k < len(lst):
            return lst[k]
        else:
            raise Exception("Index out of range.")              
```                    
                
                
                    
            
        
                       
            
    