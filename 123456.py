import math
class BTNode(object):
    def __init__(self, data):
        self.data=data
        self.leftChild=None 
        self.rightChild=None
def InsertElementBinaryTree (root, node):
    if root:
        if node.data<root.data:
            if root.leftChild:
                InsertElementBinaryTree(root.leftChild,node) 
            else:
                root.leftChild=node
        else:
            if root.rightChild:
                InsertElementBinaryTree(root.rightChild,node) 
            else:
                root.rightChild=node
    else:
        return 0
def InitBinaryTree(dataSource, length):
    root=BTNode(dataSource[0]) 
    for x in range(1,length):
        node=BTNode(dataSource [x])
        InsertElementBinaryTree (root,node) 
    return root 
print('Done...')
def PreorderTraversalBinaryTree(root):
    if root:
        print('%d|'%root.data,)
        PreorderTraversalBinaryTree(root.leftChild) 
        PreorderTraversalBinaryTree(root.rightChild)
def InorderTraversalBinaryTree(root):
    if root:
        InorderTraversalBinaryTree(root.leftChild) 
        print('%d|'%root.data,)
        InorderTraversalBinaryTree (root.rightChild)
def PostorderTraversalBinaryTree (root):
    if root:
        PostorderTraversalBinaryTree(root.leftChild) 
        PostorderTraversalBinaryTree(root.rightChild) 
        print('%d|'%root.data,)
def TraversalByLayer (root, length):
    stack=[]
    stack.append(root)
    for x in range(length):
            node=stack [x]
            print('%d|'%node.data,) 
            if node.leftChild:
                stack.append(node.leftChild) 
            if node.rightChild:
                stack.append(node.rightChild)
if __name__== '__main__' : 
    dataSource=[3,4, 2,6, 7, 1, 8,5] 
    length=len(dataSource)
    BTree=InitBinaryTree(dataSource, length) 
    print ('****NLR:')
    PreorderTraversalBinaryTree (BTree) 
    print('\n****LNR:')
    InorderTraversalBinaryTree(BTree) 
    print('\n****LRN:')
    PostorderTraversalBinaryTree (BTree) 
    print('\n****LayerTraversal:') 
    TraversalByLayer (BTree, length)
