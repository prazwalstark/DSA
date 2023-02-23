def postfixevaluation(stri):
    i=0
    final=0
    stack=[]
    operators=['+','-','*','/','^']
    while(i!=len(stri)):
        if(stri[i].isnumeric()):
            stack.append(stri[i])
        elif(len(stack)!=0 and  stri[i] in operators):
            num1=int(stack.pop())
            num2=int(stack.pop())
            if (stri[i]=='+'):
                final = num2 + num1
                stack.append(final)
            elif(stri[i]=='-'):
                final = num2 - num1
                stack.append(final)
            elif(stri[i]=='*'):
                final = num2 * num1
                stack.append(final)
            elif(stri[i]=='/'):
                final = num2 / num1
                stack.append(final)
            else:
                final = num2 ^ num1
                stack.append(final)
        i+=1
    return final
stri = list(input("Enter the expression without space in-between: "))
print("The final value of the postfix evaluation is: "+str(postfixevaluation(stri)))