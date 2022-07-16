from torch import minimum


class BST:
    def __init__(self, data):
        self.node = data
        self.right = None
        self.left = None

    def addChild(self,data):
        if data == self.node:
            return
        elif data < self.node:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BST(data)
        


    def inOrder(self):
        elements = []
        if self.left:
            elements += self.left.inOrder()#add all left subtree

        elements.append(self.node)#add root data
        
        if self.right:
            elements += self.right.inOrder()#add all right
        
        return elements

    def preOrder(self):
        elements = []
        if self.node:
            elements.append(self.node)

        if self.left:
            elements += self.left.preOrder()
        
        if self.right:
            elements += self.right.preOrder()
        return elements

    def postOrder(self):
        elements = []
        if self.left:
            elements += self.left.preOrder()
        if self.right:
            elements += self.right.preOrder()
        elements.append(self.node)
        return elements
    
    def delete(self,val):
        if val < self.node:
            if self.left:
                self.left = self.delete(val)
        if val > self.node:
            if self.right:
                self.right = self.delete(val)
        
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            minVal = self.minimum()
            self.node = minVal
            self.right.delete(minVal)
        return self


    def search(self,element):
        
        if element == self.node:
            return True

        if element < self.node:
            if self.left:
                return self.left.search(element)
            else:
                return False

        if element > self.node:
            if self.right:
                return self.right.search(element)
            else:
                return False

    def maximum(self):
        maximum = self.node
        if self.right:
             maximum = self.right.maximum()
        return maximum
    
    def minimum(self):
        minimum = self.node
        if self.left:
            minimum = self.left.minimum()
        return minimum 
        
    def calSum(self):
        total = self.node
        if self.left:
            total += self.left.calSum()
        if self.right:
            total += self.right.calSum()
        return total
        
    
def buildtree(elements):
    root = BST(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
    return root
    
numbers = [15,12,27,7,14,20,88,23]
tree = buildtree(numbers)
val = tree.delete(15)
print(val)