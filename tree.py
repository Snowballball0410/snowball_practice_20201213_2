# define a tree
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


root = Tree()
root.data = "root"
root.left = Tree()
root.left.data = "left"
root.right = Tree()
root.right.data = "right"

print(root.left.data)
print(root.right.data)

# further create the tree
root.left.left = Tree()
root.left.left.data = "left 2"
root.left.right = Tree()
root.left.right.data = "left-right"


# ---------------------------------------------------------------------------------------------------
# create root
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printtree(self):
        print(self.data)


root = Node(10)

root.printtree()

# Compare the new value with the parent node
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data),
        if self.right:
            self.right.printtree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printtree()


# A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties
# − The left sub-tree of a node has a key less than or equal to its parent node's key.
# The right sub-tree of a node has a key greater than to its parent node's key.
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + " is found")

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
