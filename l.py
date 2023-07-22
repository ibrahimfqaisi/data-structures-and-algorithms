

def palindrome(self):
    curr =self.head
    ll1=linklist()
    ll2=linklist()
    
    count =0
    while curr:
        count+=1
        curr=curr.next
    
    curr=self.head
    count =count//2
    count2=0
    curr1=ll1.head
    curr2=ll2.head
    while curr:
        if count2<=count :
            curr1= curr
            curr1.next=curr.next 
        else :
            curr2= curr
            curr2.next=curr.next 
        curr=curr.next    
        
        return (curr1,curr1)
            
            
             

        
