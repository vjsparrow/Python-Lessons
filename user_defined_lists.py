# User Defined Lists

class UserDefinedList:

    def __init__(self, initval = None):
        self.value = initval
        self.next = None


    def isempty(self):
        if self.value == None:
            return True
        else:
            return False


    def append(self, v):
        if self.isempty():
            self.value = v
            return
        elif self.next == None:
            newnode = UserDefinedList(v)
            self.next = newnode
        else:
            self.next.append(v)
        return


    def __str__(self):
        selflist = []
        if self.value == None:
            return (str(selflist))

        temp = self
        selflist.append(temp.value)

        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return (str(selflist))


    def insert(self, v):
        if self.isempty():
            self.value = v

        newnode = UserDefinedList(v)

        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)

        return


    def delete(self, v):
        if self.isempty():
            return
        elif self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return
