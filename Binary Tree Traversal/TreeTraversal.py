
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
def BFS(root):
    queue=[root]
    while(queue):
        temp=queue.pop(0)
        print(temp.data,end=" ")
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.data,end=" ")
        inorder(root.left)
        inorder(root.right)

def postorder(root):
    if root is not None:
        inorder(root.left)
        inorder(root.right)
        print(root.data,end=" ")


root=Node(1)
node1=root.left=Node(2)
node2=root.right=Node(3)
node3=node1.left=Node(4)
node4=node1.right=Node(5)
node6=node2.left=Node(6)
node7=node2.right=Node(7)
print("BFS")
BFS(root)
print()
print("Inorder")
inorder(root)
print()
print("Preorder")
preorder(root)
print()
print("Postorder")
postorder(root)



        
        
        
