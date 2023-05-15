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
                    
                
                
                    
            
        
                       
            
    


