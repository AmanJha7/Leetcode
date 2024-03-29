#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    

# } Driver Code Ends
#User function Template for python3

class Solution:
    # Check if the binary tree is isomorphic or not 
    def isIsomorphic(self, n1, n2): 
          
        # Both roots are None, trees isomorphic by definition 
        if n1 is None and n2 is None: 
            return True
      
        # Exactly one of the n1 and n2 is None, trees are not 
        # isomorphic 
        if n1 is None or n2 is None: 
            return False
      
        if n1.data != n2.data : 
            return False
        # There are two possible cases for n1 and n2 to be isomorphic 
        # Case 1: The subtrees rooted at these nodes have NOT 
        # been "Flipped". 
        # Both of these subtrees have to be isomorphic, hence the && 
        # Case 2: The subtrees rooted at these nodes have 
        # been "Flipped" 
        return ((self.isIsomorphic(n1.left, n2.left)and 
                self.isIsomorphic(n1.right, n2.right)) or
                (self.isIsomorphic(n1.left, n2.right) and 
                self.isIsomorphic(n1.right, n2.left)) 
                ) 

#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s1=input()
        s2=input()
        root1=buildTree(s1)
        root2=buildTree(s2)
        if Solution().isIsomorphic(root1,root2):
            print('Yes')
        else:
            print('No')
# } Driver Code Ends