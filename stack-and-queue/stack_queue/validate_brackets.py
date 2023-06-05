try:
    from stack import Stack
except:
    from stack_queue.stack import Stack
    
def validateBrackets(str):
    lst=[]
    def check(x):
        if x== ")" and lst[0]=="(":
            del lst[0] 
        elif x== "}" and lst[0]=="{":
            del lst[0] 
        elif x== "]" and lst[0]=="[":
            del lst[0] 
        elif  x== "]" or x== "}" or x== ")":
            lst.insert(0,x)

    for char  in str:
        if char  == "(" or char =="{" or char  == "[":
            lst.insert(0,char) 
        check(char)
      
    if lst==[]:
        return True
    else:
       return False 
       
print(validateBrackets("[]"))