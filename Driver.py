from random import randint
import Node as node
import LinkedList as linkedList

LINKEDLIST = linkedList.LinkedList()
ALLIDS = []

for x in range(0, 10):
    NEXTNODE = node.Node(x, randint(0, 100))
    LINKEDLIST.addnode(NEXTNODE)
    ALLIDS.append(NEXTNODE.id_)

print "All values\n"
CURVAL = LINKEDLIST.getroot()
while CURVAL is not None:
    print "Value: {} Id: {}".format(CURVAL.value_, CURVAL.id_)
    CURVAL = CURVAL.getnextnode()

print "Value by id\n"
for x in range(0, 10):
    NODE = LINKEDLIST.getnode(x)
    print "Value: {} Id: {}".format(NODE.value_, NODE.id_)

print "Removing nodes by value\n"
LINKEDLIST.printallnodes()
for x in range(0, 10):
    print "Removing node {}:".format(x)
    LINKEDLIST.removenode(x)
    LINKEDLIST.printallnodes()
    print ""
