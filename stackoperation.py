class Stack:
    def __init__(self):
        self.__arr=[]


    def push(self,value):
        if not self.overflow():
            self.__arr.append(value)
        else:
            print("Stack Overflow!")


    def pop(self):
        if not self.empty():
            return self.__arr.pop()
        else:
            print("Stack Empty!")


    def overflow(self):
        if len(self.__arr)==10:
            return True
        else:
            return False


    def empty(self):
        if len(self.__arr)==0:
            return True
        else:
            return False


    def display(self):
        return self.__arr


    def peek(self):
        if not (self.overflow() and self.empty()):
            return self.__arr[-1]


stack = Stack()
stack.push(1)
stack.push(10)
stack.push(7)
print(stack.pop())
print("The peek element is:",stack.peek())
print("The stack elements are: ",stack.display())


