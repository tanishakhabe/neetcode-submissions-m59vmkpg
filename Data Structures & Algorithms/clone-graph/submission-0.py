
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        # we're actually storing: 
        ''' {old_1: new_1, 
             old_2: new_2}

        '''

        """
        1. Have I cloned this node already?
       ↓ yes → return its clone
       ↓ no
        2. Create its clone
        3. Save old → new mapping
        4. Clone each neighbor
        5. Attach cloned neighbors
        6. Return the clone
        """
        
        def dfs(og_node):
            if og_node in cloned:
                return cloned[og_node]  #visiting its neighbors
            
            # else: we need to clone the node
            copy_node = Node(og_node.val)
            cloned[og_node] = copy_node

            for nei in og_node.neighbors: #get the original neighbors, copy them over
                copy_node.neighbors.append(dfs(nei))
            return copy_node
        
        return dfs(node) if node else None


            

            


    
        
        
        
        