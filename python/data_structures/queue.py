class _Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:
    def __init__(self):
        self._front=None
        self._rear=None 
        self.length=0
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        cur=self._front
        values=[]
        while cur:
            values.append(str(cur.value))
            cur=cur.next
        return f"Front {' <- '.join(values)} <- Rear"
    
    def __len__(self):
        return self.length

    def enqueue(self,value):
        new_node=_Node(value)
        if self.is_empty():
            self._front=new_node
            self._rear=new_node
        else:
            self._rear.next=new_node
            self._rear=new_node

        self.length +=1
        return True
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        _value=self._front.value
        self._front=self._front.next

        if self._front is None:
            self._rear=None
        self.length -=1
        return _value
    
    def peek(self):
        if self.is_empty():
            return None
        return self._front.value
        
    def is_empty(self):
        return self._front is None
    
    def clear(self):
        self._front=None
        self._rear=None
        self.length=0
