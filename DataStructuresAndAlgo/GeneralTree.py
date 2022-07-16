class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def addChild(self,child):
        child.parent = self
        self.children.append(child)


    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def printTree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
