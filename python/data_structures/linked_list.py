class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def __str__(self):
        values=[]
        current=self.head
        while current:
            values.append(str(current.value))
            current=current.next
        return " -> ".join(values) + "-> None"

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
        return True

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return removed

        current = self.head
        while current.next.next:
            current = current.next

        removed = current.next
        current.next = None
        self.tail = current
        self.length -= 1
        return removed

    def pop_first(self):
        if self.length == 0:
            return None
        current = self.head
        self.head = self.head.next
        current.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current

    def print_list(self):
        values=[]
        current=self.head
        while current:
            values.append(str(current.value))
            current=current.next
        print (" -> ".join(values) + "-> None")

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return node
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        node = Node(value)
        prev = self.get(index - 1)
        node.next = prev.next
        prev.next = node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

