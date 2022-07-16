#solving colision by chaining
class HashTableByChain:
     
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def getHash(self,key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX 

    def __setitem__(self,key,value):
        h = self.getHash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

     
    def __getitem__(self,key):
        h = self.getHash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return

    def __delitem__(self,key):
        h = self.getHash(key)
        for index, el in self.arr[h]:
            if el[0] == key:
                del self.arr[h][index]

#solving collision by linear probing
class HashTableByLinProb:
    def __init__(self):
        self.MAX = 10 
        self.arr = [None for i in range(self.MAX)]
    
    def getHash(self,key):
        for char in key:
            hash += ord(char) #convert to unicode
        return hash % self.MAX

    def __getitem__(self,key):
        hash = self.getHash(key)
        if self.arr[hash] is None: # check if key exist
            return
        probRange = self.getProbRange(hash)
        for element in probRange:
            element = self.arr[element]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self,key,value):
        hash = self.getHash(key)
        if self.arr[hash] is None:
            self.arr[hash] = (key,value)
        else:
            newHash = self.findFreeSlot(hash,key)
            self.arr[newHash] = (key,value)

    def __delitem__(self, key):
        h = self.getHash(key)
        probRange = self.getProbRange(h)
        for probIndex in probRange:
            if self.arr[probIndex] is None:
                return # item not found so return
            if self.arr[probIndex][0] == key:
                self.arr[probIndex]=None

    def findFreeSlot(self,index,key):
        probRange =self.getProbRange(index)
        for probIndex in probRange:
            if self.arr[probIndex] is None:
                return probIndex
            if self.arr[probIndex][0] == key:
                return probIndex
        raise Exception("Hashmap is full")


    def getProbRange(self,index):
        return [*range(index, len(self.arr))] + [*range(0,index)] #return the index of the whole array starting from index


l = HashTableByChain()
l["w"] = 5
l["w"] = 6
print(l["w"])
 
 