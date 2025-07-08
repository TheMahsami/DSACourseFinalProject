#ownership history
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
     
    #add to first of a list(prepend)   (o(1))
    def insert(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
        else:
            self.head = new_node
            self.tail = new_node
            
    def delete(self, data):
        pass
    
    def search(self , data):
        curr = self.head
        while curr:
            if  curr.data == data:
                return curr.data
            else:
                curr = curr.next
        
        return None
    
    def traverse(self):
        curr = self.head
        try:
            while curr:
                yield curr.data
                curr = curr.next
                
        except:
            raise Exception('there is no data for show')
        