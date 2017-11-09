"""
__module__:stack implementation
__description__:A basic implementation of stack using python(LIFO)
__author__:Prateek Kumar
"""

class node():
    def __init__(self,data):
        self.data = data
        self.pNext = None
        self.pPrev = None
    
class stackImplementation():
    def __init__(self):
        self.pHead = None
     
    def insertElement(self,num):
        """
        This function will be used to insert elements in the stack
        """
        #creating a new node
        nNode = node(num)

        #Just making a copy of the pHead
        self.pTail = self.pHead
        
        if self.pTail:
            while self.pTail.pNext != None:
                self.pTail = self.pTail.pNext
            #at this point we have reached the last element in the stack.
            self.pTail.pNext = nNode
            self.pTail = self.pTail.pNext
            self.pTail.pPrev = self.pHead
        else:
            #Adding the first head in the stack
            self.pHead = nNode


    def pop(self):
        """
        This will remove an item from the stack using LIFO
        """
        self.pTail = self.pHead
        if self.pTail:
            while(self.pTail.pPrev !=None):
                self.pTail = self.pTail.pPrev
            print "Popping the element : %s" % self.pTail.data    
            self.pTail = self.pTail.pNext
            self.pTail.pPrev = None
            self.pHead = self.pTail
        else:
            print "Stack Empty !!"

    def print_Items(self):
        self.pTail = self.pHead
        if self.pTail:
            while self.pTail != None:
                print "The element in the stack is:%s" % self.pTail.data
                self.pTail = self.pTail.pNext
        else:
            print "There are no items in the stack !!"

if __name__ == "__main__":
    #Create the object
    obj = stackImplementation()
    for x in range(20):
        obj.insertElement(x)
    obj.print_Items()
    for i in range(10):
        obj.pop()
    obj.print_Items()









