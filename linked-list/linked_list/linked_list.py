class Node :
    def __init__(self,value,next_=None) :
        self.value=value
        self.next=next_
    
class linked_list:
    def __init__(self,head=None) :
       self.head=head
    
        
    def insert (self,value):
       
       new_node =Node(value)
       new_node.next=self.head
       self.head= new_node
    
    def includes(self,value):
        current=self.head
        while current.value!=value:
           current=current.next
           if current==None:
               return False
        if current.value==value :
            return True
        
    def to_string (self):
        current=self.head
        string=""
        while current!=None:
            string+= "{ "+f"{current.value}"" }"+" -> "
            current=current.next
        string+= " None "
        return string
    
            
            
    


