
#for cars

class OpenHashTable:
    def __init__(self , capacity=100):
        self.capacity = capacity
        self.table = [None] * capacity
        #usefull data
        self.size = 0
        
    def _hash(self,key):
        return int(key) % self.capacity
    
    def _resize(self):
        old_table = self.table
        new_capacity = self.capacity * 2
        self.table = [None] * new_capacity
        self.capacity = new_capacity
        self.size = 0
        
        for index in old_table:
            if index is not None and index != 'DELETED':
                self.Insert(index[0],index[1])
                
   #HAS ERROR        #############################################
    # def _probing(self , key):
    #     index = self._hash(key)
    #     start_index = index
    #     # baraye peyda kardan yek khane khali / mahsa deqat kon khane ba mark 'DELETED' ham khali hesab mishe
    #     while self.table[index] is not None and self.table[index] != 'DELETED' and self.table[index][0] != key:
    #         index = (index +1) % self.capacity
    #         if index == start_index:
    #             raise Exception('Hash Table Overflow!!')
    #     return index
    
            
            
    def Insert(self, key , value):
        if self.size / self.capacity >= 0.7:
            self._resize()
            

        index = self._hash(int(key))
        start_index = index
        
        while self.table[index] is not None and self.table[index] != 'DELETED':
            if self.table[index][0] == key:
                self.table[index] = (key , value)
                return f'The key {key} is updated successfully'
            
            index = (index + 1) % self.capacity
            if index == start_index:
                raise Exception('Hash Table OVERFLOW!')
            
        self.table[index] = (key , value)
        self.size +=1
        return f'the key {key} with value {value} inserted successfully'
        
    
    def Delete(self , key):
        index = self._hash(int(key))
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index] != 'DELETED' and self.table[index][0] == key:
                self.table[index] = 'DELETED'
                self.size -= 1
                return f'key {key} deleted from table successfully'
        
            index = (index + 1) % self.capacity
            if start_index == index:
                break      
        raise KeyError("key not founded!")
    
    def Search(self,key):
        index = self._hash(int(key))
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index] != 'DELETED' and self.table[index][0] == key:
                return self.table[index][1]
            
            index = (index + 1) % self.capacity
            if start_index == index:
                break
        
        raise KeyError(f'key {key} not founded!')

    
    def Traverse(self):
        for item in self.table:
            if item is not None and item != 'DELETED':
                yield item
                
