class _Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class Stack:
    def __init__(self):
        self._top=None
        self._height=0

    def __str__(self):
        values=[]
        cur=self._top
        while cur:
            values.append(str(cur.value))
            cur=cur.next
        return " -> ".join(values)

    def is_empty(self):
        return self._top is None
    
    def push(self,value):
        new_node=_Node(value)
        new_node.next=self._top
        self._top=new_node
        self._height +=1

    def pop(self):
        if self.is_empty():
            return None
        
        cur = self._top
        self._top = cur.next   
        cur.next = None 
        self._height -= 1
        return cur.value
    
    def peek(self):
        if self.is_empty():
            return None
        return self._top.value
    
    def clear(self):
        self._top=None
        self._height=0

