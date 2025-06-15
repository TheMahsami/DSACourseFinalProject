class OpenHashTable:
    def __init__(self , capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity
        #usefull data
        self.size = 0
        
    def _hash(self,key):
        return key % self.capacity
    
    def _resize(self):
        old_table = self.table
        new_capacity = self.capacity * 2
        self.table = [None] * new_capacity
        self.size = 0
        
        for index in old_table:
            if index is not None and index != 'DELETED':
                self.Insert(index[0],index[1])
                
    
    def _probing(self , key):
        index = self._hash(key)
        final_index = index
        
        while self.table[index] is not None and self.table[index]== 'DELETED' and self.table[index][0] != key:
            final_index = (index +1) % self.capacity
            if final_index == index:
                return "Hash Table is Overflow"
        return final_index
    
            
            
    def Insert(self, key , value):
        if self.size / self.capacity >= 0.7:
            self._resize()
            
        index = self._probing(key)
        if self.table[index] is None:
            self.table[index] = (key , value)
            self.size +=1
            return f'the key {key} with value {value} inserted successfully'
        
    
    def Delete(self , key):
        index = self._probing(key)
        if self.table[index] is None or self.table[index] == 'DELETED':
            raise KeyError("key not founded!")
        
        self.table[index] = 'DELETED'
        self.size -+ 1
        return f'key {key} deleted from table successfully'
    
    def Search(self,key):
        index = self._probing(key)
        if self.table[index] is None or self.table[index] == 'DELETED':
            raise KeyError(f'key {key} not founded!')
        
        return self.table[index][1]
    
    def Traverce(self):
        for item in self.table:
            if item is not None and item != 'DELETED':
                yield item