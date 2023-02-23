class Infix_Prefix:
    def __init__(self):
        self.__prefix=[]
        self.__stack=[]
    
    def conversion(self,stri):
        i = 0 
        while(len(stri)!= i):
            if(stri[i].isalnum()):
                self.__prefix.append(stri[i])
            
            elif(stri[i]==')'):
                self.__stack.append(stri[i])
            
            elif(stri[i]=='('):
                while(self.__stack[-1]!=')'):
                    self.__prefix.append(self.__stack.pop())
                self.__stack.pop()
            
            else:
                while(len(self.__stack)!=0 and (self.priority(stri[i])<self.priority(self.__stack[-1]))):
                    self.__prefix.append(self.__stack.pop())
                self.__stack.append(stri[i])

            i+=1


        while(len(self.__stack)!=0):
            self.__prefix.append(self.__stack.pop())


        convert = self.__prefix[::-1]
        return convert
    

    def priority(self,alpha):
        if (alpha == '-' or alpha == '+'):
            return 1
        elif (alpha =='*' or alpha == '/'):
            return 2
        elif (alpha == '^'):
            return 3
        else:
            return 0


inf = Infix_Prefix()
string = list(input("Enter the expression without space in-between them: "))
stri = string[::-1]
print("The converted expression(Prefix Operated) is: ",''.join(inf.conversion(stri)))