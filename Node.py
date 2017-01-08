
class Node(object):
    """Contains a node of information"""
    id_ = None
    value_ = None
    nextnode_ = None

    def __init__(self, nodeid, value):
        self.id_ = nodeid
        self.value_ = value

    def setnextnode(self, node):
        """Sets the a pointer to the next node"""
        if self.nextnode_ is None:
            self.nextnode_ = node
        else:
            nextnode = self.nextnode_
            node.nextnode_ = nextnode
            self.nextnode_ = node

    def removenextnode(self):
        """Removes a node from the list"""
        self.nextnode_ = self.getnextnode().getnextnode()

    def getnextnode(self):
        """Returns the next node in the list"""
        return self.nextnode_
