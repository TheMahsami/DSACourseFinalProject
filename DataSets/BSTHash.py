#for licenseplates
class BSTNode:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    # in func faqat number haye plate ro extract mikone b bar asas oonha add mikone to bst
    def _extract_numbers(self, number):
        digits = ''.join(char for char in number if char.isdigit())
        result = int(digits)
        return result
    
    def insert(self, number ,data):
        new_node = BSTNode(data)
        if self.root == None:
            self.root = new_node
            return
        
        curr = self.root
        while curr:
            if self._extract_numbers(number) < self._extract_numbers(curr.data.number):
                if curr.left is None:
                    curr.left = new_node
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new_node
                    return
                curr= curr.right
        
    def search(self , number):
        curr = self.root
        while curr is not None:
            if self._extract_numbers(number) == self._extract_numbers(curr.data.number):
                return curr.data
            
            if self._extract_numbers(number) < self._extract_numbers(curr.data.number):
                curr = curr.left
            elif self._extract_numbers(number) > self._extract_numbers(curr.data.number):
                curr = curr.right
            
        return None
    
    def traverse(self , root):
        if root is None:
            return None
        yield from self.traverse(root.left)
        yield root
        yield from self.traverse(root.right)
        
class HashTable:
    def __init__(self , size=100):
        self.size = size
        # self.table = [BST() for _ in range(size)]
        self.table = [None] * size
        
    def _hash_function(self, citycode):
        return int(citycode) % self.size
    
 
    def insert(self ,number, data):
        parts = number.split('-')
        citycode = parts[1]
        index = self._hash_function(citycode)
        # self.table[index] = BST().insert(number , data)
        if self.table[index] is None:
            self.table[index] = BST()       
        self.table[index].insert(number, data) 
        
    def search(self , number):
        try:
            numbers , citycode = str(number).split('-')
            citycode = citycode.strip()
            index = self._hash_function(citycode)
            return self.table[index].search(number)
        except:
            return None
    def tarverse(self):
        for item in self.table:
            # return self.table[item].traverse()
            if item is None:
                yield 'None'
            else:
                yield (node.data for node in item.traverse(item.root))
                
        
hash = HashTable()
hash.insert('22f333-66' , 'data1')
hash.insert('44t843-90' , 'data2')
res = hash.tarverse()
# for bucket in res :
#     print(bucket)
# print(res)

