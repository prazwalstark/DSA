class Infix_Postfix:
    def __init__(self):
        self.__postfix = []
        self.__stack = []

    def priority(self, alpha):
        if (alpha == '+' or alpha == '-'):
            return 1
        elif (alpha == '*' or alpha == '/'):
            return 2
        elif (alpha == '^'):
            return 3
        else:
            return 0


    def conversion(self, stri):
        i = 0
        #str = list(string)
        while (i < len(stri)):
            if (stri[i].isalnum()):
                self.__postfix.append(stri[i])

            elif (stri[i] == '('):
                self.__stack.append(stri[i])

            elif (stri[i] == ')'):
                ch = self.__stack.pop()
                while (ch != '('):
                    self.__postfix.append(ch)
                    ch = self.__stack.pop()

            else:
                    while (len(self.__stack)!=0 and (self.priority(stri[i]) <= self.priority(self.__stack[-1]))):
                        self.__postfix.append(self.__stack.pop())
                    self.__stack.append(stri[i])
                    
            i += 1

        while (len(self.__stack) != 0):
            self.__postfix.append(self.__stack.pop())

        return self.__postfix


stri = list(input("Enter the expression without space in between:"))
inf = Infix_Postfix()
print("The infix to postfix operation resulted in: ", ''.join(inf.conversion(stri)))
