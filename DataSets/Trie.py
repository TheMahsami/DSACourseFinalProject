<<<<<<< HEAD
=======
#for users
>>>>>>> first
class TrieNode:
    def __init__(self):
        self.child = 10 * [None]
        self.data = None
        self.IsEnd = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def Insert(self,id,data):
        strid = str(id)
        curr = self.root
        
        for digit in strid:
            index = int(digit)
            if curr.child[index] is None:
                curr.child[index] = TrieNode()
            curr = curr.child[index]
        
        curr.IsEnd = True
        curr.data = data
        
        return f'{id} adeded successfully'
    
    def Delete(self , id):
        # strid = str(id)
        # cur = self.root
        pass
        
    def Search(self , id):
        strid = str(id)
        curr = self.root
        
        for digit in strid:
            index = int(digit)
            if curr.child[index] is None:
<<<<<<< HEAD
                return False
            
            curr = curr.child[index]
             
        return curr.IsEnd
=======
                return None
            #return none ha dar soorari hast ke chizi peyda nashavad
            curr = curr.child[index]
        if curr.IsEnd is True:
            return curr.data
        else:
            return None
>>>>>>> first
    
    def _recursive_traverse(self, node , prefix):
        if node is None:
            return
        if node.data:
            yield prefix , {node.data}
        
        for index , child_node in enumerate(node.child):
            if child_node is not None:
                yield from self._recursive_traverse(child_node , prefix + str(index))
    def Traverse(self):
        
        yield from self._recursive_traverse(self.root , '')
        