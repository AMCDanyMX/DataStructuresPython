class Node:  
    def __init__(self,raiz=None,left=None,right=None):  
        self.raiz=raiz  
        self.left = left #hijo izquiero
        self.right = right #hijo derecho
        

def preOrder(root):  
    '''
        Recorrido preorden
    '''
    if root==None:  
        return  
    print(root.raiz)  
    preOrder(root.left)  
    preOrder(root.right)  
    
def inOrder(root): 
    '''
        Recorrido inorder
    '''
    if root==None:  
        return  
    inOrder(root.left)  
    print(root.raiz)  
    inOrder(root.right)  

def postOrder(root):  
    '''
        Recorrido postorden
    '''
    if root==None:  
        return  
    postOrder(root.left)  
    postOrder(root.right)  
    print(root.raiz)
    

root=Node('D',Node('B',Node('A'),Node('C')),Node('E',Node('F'),Node('G')))
print ('Recorrido preOrder:')
preOrder(root)
    
print('\n')
print ('Recorrido inOrder:')
inOrder(root)
print('\n')
    
print ('Recorrido postOrder:')
postOrder(root)
print('\n')
    


