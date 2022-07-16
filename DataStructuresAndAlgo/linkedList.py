'''a python representation of a linkedList. Instantiate the class to test'''

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data,None)
            return
    
    def getLength(self):
        count = 0
        itr = self.head
        while itr.next:
            itr = itr.next
            count +=1
        return count

    def removeAt(self,index):
        if index< 0 or index > self.getLength():
            raise Exception ("Invalid index")
            
        if index == 0:
            self.head = self.head.next
            return
    
        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insertAt(self,index,data):

        if index< 0 or index > self.getLength():
            raise Exception ("Invalid index")
        
        if index == 0:
            self.insertAtBegining(data)
            return
        
        itr = self.head
        count = 0 
        while itr.next:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                return
            itr = itr.next
            count +=1

    def insertAfterValue(self,value,data):

        if self.head == None:
            return

        itr = self.head
        count = 0
        while itr.next:
            if itr.data == value:
                self.insertAt(count + 1,data)
                return
            
            if itr ==  None:
                print("value not found")
                return
            itr = itr.next
            count += 1

    def removwByValue(self,value):
        if self.head == None:
            return
             
        itr = self.head
        count = 0
        while itr.next:
            if itr.data == value:
                self.removeAt(count)
                return
            
            if itr ==  None:
                print("value not found")
                return
            itr = itr.next
            count += 1

    
    def print(self):
        if self.head is None:
            print("LinkedLis is empty")
            return
        else:
            itr = self.head
            out =""
            while itr:
                out += str(itr.data) + "---->"
                itr=itr.next
            print(out)


