try:
    from stack import Stack
except:
    from stack_queue.stack import Stack
    
def validateBrackets(str):
    def check(x):
        if x== ")" and stack.top.value=="(":
            stack.pop() 
        elif x== "}" and stack.top.value=="{":
            stack.pop()
        elif x== "]" and stack.top.value=="[":
            stack.pop()
        elif  x== "]" or x== "}" or x== ")":
            stack.push(x)

    stack= Stack()
    
    for char  in str:
        if char  == "(" or char =="{" or char  == "[":
            stack.push(char ) 
        check(char)
      
    if stack.is_empty():
        return True
    else:
       return False 
       
print(validateBrackets("[]"))