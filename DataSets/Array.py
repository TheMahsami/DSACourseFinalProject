class Array:
    def __init__(self, size):
        self.size = size
        self.MainArray = [None] * size
        self.usefulldata = 0
        
        
    def __len__(self):
        return self.usefulldata
    
    def appendfirst(self, data):
        if self.usefulldata < self.size:
            for i in range(self.usefulldata, 0 , -1):
                self.MainArray[i]= self.MainArray[i - 1]
            self.MainArray[0] = data
            self.usefulldata +=1

        else:
            raise Exception('array overflow')
    
    def appendlast(self, data):
        if self.usefulldata == 0:
            self.MainArray[self.usefulldata] = data
            self.usefulldata += 1
        else:
            if self.usefulldata < self.size:
                self.MainArray[self.usefulldata] = data
                self.usefulldata +=1
            else:
                raise Exception('array overflow') 

    def insert(self, index, data):
        index = int(index)
        if 0 <= index <= self.size:
            if self.MainArray[index] == None:
                self.usefulldata += 1
                self.MainArray[index] = data
            else:
                self.MainArray[index] = data
        else:
            raise IndexError("Index out of range")
        
    def search(self, data):
        for i in range(len(self.MainArray)):
            if self.MainArray[i] == data:
                return i
            
        return None
    
    def delete(self, data):
        if data in self.MainArray:
            index = self.search(data)
            for i in range(index , self.usefulldata):
                self.MainArray[i] = self.MainArray[i+1]
                self.usefulldata-=1
        else:
            raise ValueError("data not founded")
            
        
    def traverse(self):
        for item in self.MainArray:
            if item is not None:
                yield(item)