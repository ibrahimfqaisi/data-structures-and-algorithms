def intersection( link1, link2):

    curr1 = link1.head
    check =0
    global check1 ,check2 ,sol
    list1=[]
    list2=[]
    check1=0
    check2=0
    while curr1:
        curr2 = link2.head
        while curr2:
            if check1==0 :
                if curr1.data == curr2.data:
                    check1=1
                    check =1
                    sol=curr1.data
                    
            if check2==0:
                if check== 1 :
                    list2.append(curr2.data)
            curr2=curr2.next

        if check ==1 :
            check2=1
            list1.append(curr1.data)

        curr1=curr1.next

    if len(list1)==len(list2) and len(list2) != 0 :
        for x in range(len(list1)):
            if list1[x]!=list2[x]:
                return "ther is no"
        
        return sol   

    return "ther is no"    


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# # Test case 1
# # Intersecting lists with one common node
# link1 = LinkedList()
# link1.head = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# link1.head.next = node2
# node2.next = node3

# link2 = LinkedList()
# link2.head = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# link2.head.next = node4
# node4.next = node5

# print(intersection(link1, link2))  # Expected output: 3

# Test case 2
# Non-intersecting lists
link1 = LinkedList()
link1.head = Node(1)
node2 = Node(2)
node3 = Node(3)
link1.head.next = node2
node2.next = node3

link2 = LinkedList()
link2.head = Node(1)
node4 = Node(5)
node5 = Node(3)
link2.head.next = node4
node4.next = node5

print(intersection(link1, link2))  # Expected output: "ther is no"

# Test case 3
# Intersecting lists with multiple common nodes
# link1 = LinkedList()
# link1.head = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# link1.head.next = node2
# node2.next = node3

# link2 = LinkedList()
# link2.head = Node(1)
# node4 = Node(3)
# node5 = Node(5)
# link2.head.next = node4
# node4.next = node5

# print(intersection(link1, link2))  # Expected output: 1

# Test case 4
# Empty lists
link1 = LinkedList()
link2 = LinkedList()

# print(intersection(link1, link2))  # Expected output: "ther is no"
