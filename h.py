class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def delete(self,node):
        if node.next == None:
            raise Exception("fff")
        curr = node.next
        node.next = curr.next
        return curr
        
    def mid(self):
        curr = self.head
        prev = None
        while curr:
            next_node=curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head =prev
        return self

    def repet(self):

        curr = self.head
        while curr:
            temp = curr
            while temp.next:
                if curr.data == temp.next.data:
                    temp1=temp.next
                    temp.next = temp1.next
                temp = temp.next
            
                
            curr = curr.next   


    def merg(self,ll1,ll2):
        newll= LinkedList()
        curr1 = ll1.head
        curr2=ll2.head
        curr3=newll.head
        while curr1:
            keeper=  curr3
            curr3.data=curr1.data
            curr3.next=keeper
            curr3.head.data=curr2.data
            curr3.next=keeper
                
            curr1 = curr1.next   
            curr2 = curr2.next  
            curr3 = curr3.next
    

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

# Test the delete function
def test_delete():
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(1)
    third = Node(3)
    fourth = Node(4)

    ll.head.next = second
    second.next = third
    third.next = fourth

    print("Before deletion:")
    ll.display()

    # Delete node with value 3
    ll.mid()

    print("After deletion:")
    ll.display()

test_delete()
