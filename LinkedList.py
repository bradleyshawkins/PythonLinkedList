
class LinkedList(object):
    """LinkedList"""
    root = None
    nodelist = {}

    def addnode(self, node):
        """Adds a node to the linked list"""
        if self.root is None:
            self.root = node
        elif self.root.value_ > node.value_:
            node.setnextnode(self.root)
            self.root = node
        else:
            curnode = self.root
            while curnode.getnextnode() is not None and node.value_ > curnode.getnextnode().value_:
                curnode = curnode.getnextnode()
            curnode.setnextnode(node)
        self.nodelist[node.id_] = node

    def removenode(self, nodeid):
        """Removes a node from the linked list"""
        if self.root.id_ == nodeid:
            self.root = self.root.getnextnode()
        else:
            curnode = self.root
            while curnode.getnextnode().id_ != nodeid:
                curnode = curnode.getnextnode()
            curnode.removenextnode()
        del self.nodelist[nodeid]

    def getnode(self, nodeid):
        """Retrives the node based on the id"""
        return self.nodelist[nodeid]

    def getroot(self):
        """Returns the root of the list"""
        return self.root

    def printallnodes(self):
        """Prints all of the nodes in the linked list"""
        curnode = self.root
        while curnode != None:
            print "Value: {} Id: {}".format(curnode.value_, curnode.id_)
            curnode = curnode.getnextnode()
    