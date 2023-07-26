# class Node :
#     def __init__(self,value,next_=None) :
#         self.value=value
#         self.next=next_
    
# class linked_list:
#     def __init__(self,head=None) :  
#        self.head=head
    
        
#     def insert (self,value):
       
#        new_node =Node(value)
#        new_node.next=self.head
#        self.head= new_node
    
#     def includes(self,value):
#         current=self.head
#         while current.value!=value:
#            current=current.next
#            if current==None:
#                return False
#         if current.value==value :
#             return True
        
#     def to_string (self):
#         current=self.head
#         string=""
#         while current!=None:
#             string+= "{ "+f"{current.value}"" }"+" -> "
#             current=current.next
#         string+= " None "
#         return string
    
#     def append(self,value):
#         current=self.head
#         if current==None :
#             self.insert(value)
            
#         else:
#             while current!=None:
#                 if current.next==None:
#                     current.next= Node(value)
#                     return
#                 current=current.next
        
#     def after(self,value,_next):
#         current=self.head
#         if current==None :
#             self.insert(value)
            
#         else:
#             while current!=None:   
#                 if current.value== str(value):
#                     print("gffu")
#                     old_current_next=current.next
#                     current.next= Node(_next,old_current_next)
#                     break 
                
#                 current=current.next
            

#     def Before(self,value,_next):
#         current=self.head
#         if current.value == str(value):
#            self.insert(_next) 
#            return
#         while current.next!=None:   
#             if current.next.value== str(value):
#                 old_current_next=current.next
#                 current.next= Node(_next,old_current_next)
                
#                 break 
#             current=current.next                
                    
                
                
#     def kth(self, k):
#         current = self.head
#         lst = []

#         while current is not None:
#             lst.insert(0, current.value)
#             current = current.next


#         if  k<0:
#              raise Exception("Index is negative.")
#         elif k < len(lst):
#             return lst[k]
#         else:
#             raise Exception("Index out of range.")

        
class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(str(current.value))
            current = current.next
        return " -> ".join(nodes) + " -> None"

    def append(self, value):
        current = self.head
        if current is None:
            self.insert(value)
        else:
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def insert_after(self, value, _next):
        current = self.head
        if current is None:
            self.insert(value)
        else:
            while current is not None:
                if current.value == value:
                    old_current_next = current.next
                    current.next = Node(_next, old_current_next)
                    break
                current = current.next

    def insert_before(self, value, _next):
        current = self.head
        if current.value == value:
            self.insert(_next)
            return
        while current.next is not None:
            if current.next.value == value:
                old_current_next = current.next
                current.next = Node(_next, old_current_next)
                break
            current = current.next

    def kth(self, k):
        if k < 0:
            raise Exception("Index is negative.")
        size = self.size()
        if k >= size:
            raise Exception("Index out of range.")
        current = self.head
        count = size - k - 1
        while count > 0:
            current = current.next
            count -= 1
        return current.value



# Create a linked list
my_list = LinkedList()

# Test insert and to_string methods
my_list.insert(3)
my_list.insert(2)
my_list.insert(1)
print(my_list.to_string())  # Output: 1 -> 2 -> 3 -> None

# Test includes method
print(my_list.includes(2))  # Output: True
print(my_list.includes(4))  # Output: False

# Test append method
my_list.append(4)
my_list.append(5)
print(my_list.to_string())  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Test insert_after method
my_list.insert_after(3, 6)
print(my_list.to_string())  # Output: 1 -> 2 -> 3 -> 6 -> 4 -> 5 -> None

# Test insert_before method
my_list.insert_before(6, 7)
print(my_list.to_string())  # Output: 1 -> 2 -> 7 -> 3 -> 6 -> 4 -> 5 -> None

# Test kth method
print(my_list.kth(0))  # Output: 1
print(my_list.kth(3))  # Output: 3
print(my_list.kth(6))  # Output: 4

# Test exceptions
try:
    print(my_list.kth(-1))
except Exception as e:
    print(e)  # Output: Index is negative.

try:
    print(my_list.kth(7))
except Exception as e:
    print(e)  # Output: Index out of range.







    def reverse(self):
        current = self.head
        NEW_linklist= LinkedList()
        if current is None:
           return  None
        else:
            while current is not None:
                temp = NEW_linklist.head
                NEW_linklist.head =current
                NEW_linklist.head.next= temp

                
                current = current.next
            return NEW_linklist







        # NEW_linklist= LinkedList()
        # if current is None:
        #    return  None
        # else:
        #     while current is not None:
        #         temp = NEW_linklist.head
        #         NEW_linklist.head =current
        #         NEW_linklist.head.next= temp

                
        #         current = current.next
        #     return NEW_linklist




# Implement a function to delete a node from a linked list given the value of the node to be deleted.


def delete(ll,possition):
    curr = ll.head
    possition_node = 0
    while curr:
        possition_node+=1
        if possition_node == possition:
            deleteed = curr.next
            curr.next = deleteed.next
        curr = curr.next
        
    return ll
  
[0,1,2,3,4]            
[5,6,8,10]
