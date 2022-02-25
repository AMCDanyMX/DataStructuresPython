class Tree:
    def __init__(self, val = None):
        if val != None:
            self.val = val
        else:
            self.val = None
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Tree(val)
            else:
                self.right.insert(val)
        else:
            self.val = val
            

    def printValues(self):
        if self.left:
            self.left.printValues()
        print(self.val)
        if self.right:
            self.right.printValues()

tree = Tree(20)
tree.left = Tree(18)
tree.right = Tree(22)
tree.insert(19)
tree.insert(24)
tree.insert(5)
tree.insert(21)

tree.printValues()