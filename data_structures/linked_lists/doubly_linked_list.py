class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self,value=None):
        self.head=None
        self.tail=None
        self.length=0
        if value is not None:
            self.append(value)

    def __str__(self):
        values=[]
        cur=self.head
        while cur:
            values.append(str(cur.value))
            cur=cur.next
        return "None <- " + " <-> ".join(values) + " -> None"
    
    def clear(self):
        self.head=None
        self.tail=None
        self.length=0
        return True

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        cur=self.head
        if index < self.length / 2:
            for _ in range(index):
                cur=cur.next
        else:
            cur=self.tail
            for _ in range(self.length -1, index,-1):
                cur=cur.prev
        return cur 
    
    def set_value(self,index,value):
        node=self.get(index)
        if node is not None:
            node.value=value
            return True
        return False
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail 
            self.tail=new_node
        self.length +=1
        return True

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length +=1
        return True
    
    def insert(self,index,value):
        if index < 0 or index >self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node=Node(value)
        prev_node=self.get(index -1)
        next_node=prev_node.next
  
        new_node.prev=prev_node
        new_node.next=next_node

        prev_node.next=new_node
        next_node.prev=new_node
        self.length +=1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        old_tail=self.tail
        if self.length ==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            old_tail.prev=None
        self.length -=1
        return old_tail
    
    def pop_first(self):
        if self.head is None:
            return None
        cur=self.head
        if self.length == 1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            cur.next=None
        self.length -=1
        return cur 
    
    def remove(self,index):
        if index < 0 or index >=self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        cur=self.get(index)

        cur.next.prev=cur.prev
        cur.prev.next=cur.next
        cur.next=None
        cur.prev=None

        self.length -=1
        return cur

    def print_list(self):
        print(self)
    
