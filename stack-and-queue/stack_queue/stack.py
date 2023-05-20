class Node :
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self,top=None):
        self.top = top

    def push(self,value):

            node = Node(value)
            node.next = self.top
            self.top = node
            # print (self.top.next,"dddd")

    def pop(self):
        if self.top==None:
            raise Exception("the stack is empty")
            
        else :
            temp= self.top
            self.top = temp.next
            temp.next = None
            return temp.value

    def peek(self):
        if self.top==None:
            raise Exception("the stack is empty")
        else:
            return self.top.value
    def is_empty(self):
            return self.top==None

    def __str__(self):
        current=self.top
        string=""
        while current:
            string+=f"{current.value}"
            string+=" -> "
            current=current.next
        return string+"None"    


if __name__ ==  "__main__":
    stack_01= Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    # print(stack_01.peek())
    print (stack_01.is_empty())
    print(stack_01)
    # print(stack_01.top.value)