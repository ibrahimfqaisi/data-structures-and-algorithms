def intro():
    print('''
          **************************************
**    reverseArray app   **
 write  an array as an argument. 
          and write arry as this 
          1, 2, 3, 4, 5, 6
**
** To quit at any time, type "quit" **
**************************************
          ''')
def user_insertion():
    user_input=input(">")
    if user_input.lower() == "quit":
        return user_input.lower()
    else :
        user_input = user_input.split(',')
        return user_input
def main():
    user_input = user_insertion()
    reverseArray = [] 
    while user_input != "quit":
        if type(user_input) == list:
            long =len(user_input)-1
            x = range(long+1)
            for n in x:
                reverseArray.append(user_input[long-n])
            print(reverseArray)   
        else:
            print("sorry you did not enter a valid array!")
        user_input = user_insertion()
    end_application()
def end_application():
    print("thanks for using reverseArray app !")
if __name__=="__main__": 
    intro()  
    main()
