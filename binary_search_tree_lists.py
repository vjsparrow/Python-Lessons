#Binary Search Tree - list implementation

class BSearchTree:

    def __init__(self, v = None):
        self.value = v

        if self.value:
            self.right = BSearchTree()
            self.left = BSearchTree()
        else:
            self.right = None
            self.left = None


    def isempty(self):
        return(self.value == None)


    def isleaf(self):
        return (self.right.isempty() and self.left.isempty())


    def makeempty(self):
        self.value = None
        self.right = None
        self.left = None
        return


    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return


    def find(self, v):
        if self.isempty():
            return False
        if self.value == v:
            return True
        if self.value < v:
            return (self.right.find(v))
        if self.value > v:
            return (self.left.find(v))


    def insert(self, v):
        if self.isempty():
            self.value = v
            self.left = BSearchTree()
            self.right = BSearchTree()

        if self.value == v:
            return

        if self.value < v:
            self.right.insert(v)
            return

        if self.value > v:
            self.left.insert(v)
            return


    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return (self.right.maxval())


    def delete(self, v):
        if self.isempty():
            return

        if v < self.value:
            self.left.delete(v)
            return

        if v > self.value:
            self.right.delete(v)
            return

        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isempty():
                self.copyright()
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return


    def inorder(self):
        if self.isempty():
            return
        else:
            return(self.left.inorder() + [self.value] + self.right.inorder())

    def __str__(self):
        return (str(self.inorder()))
    
