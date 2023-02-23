def check(stri):
    stack=[]
    i=0
    while(i!=len(stri)):
        if(stri[i]=='('):
            stack.append(stri[i])
        elif(stri[i]==')'):
            if(len(stack)==0):
                print("Stack Empty!(Closing Paranthesis doesn't has a matching paranthesis!)")
                return 0
            else:
                stack.pop()
        i+=1
    if(len(stack)==0):
        print("Balanced Paranthesis Condition!")
    else:
        print("Unbalance Paranthesis Condition!","Error: "+str(len(stack))+" paranthesis doesn't have closing Paranthesis!")
    return 0 

stri=list(input("Enter the expression without space in between: "))
check(stri)
