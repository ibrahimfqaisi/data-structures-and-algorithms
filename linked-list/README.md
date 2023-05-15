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
                
                
                    
            
        
                       
            
    