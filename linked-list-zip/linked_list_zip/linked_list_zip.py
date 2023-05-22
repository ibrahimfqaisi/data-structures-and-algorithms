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
        
    def to_string (self):
        current=self.head
        string=""
        while current!=None:
            string+= "{ "+f"{current.value}"" }"+" -> "
            current=current.next
        string+= " None "
        return string
    def zipLists (self):
        current=self.head
        list=[]
        while current!=None:
            list.append(current.value)
            current=current.next
        
        return list
    
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
if __name__ == "__main__":
    ll_ = linked_list(Node(5))
    ll_.insert(6)
    ll_.insert(9)
    ll_2 = linked_list(Node(10))
    ll_2.insert(11)
    ll_2.insert(12)
    ll_2.insert(13)
    ll_2.insert(14)
    zipLists(ll_,ll_2)    
            
            
                       
            
    


