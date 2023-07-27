from .node import Node


class SLL(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.head is None

    def print_all(self):
        curr = self.head
        while curr is not None:
            print(curr.val,end=" -> ")
            curr = curr.next
        print("None")

    def add_to_head(self, val):
        new = Node(val)
        new.next = self.head
        self.head = new
        self.length += 1

    def add_to_tail(self, val):
        new = Node(val)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new
        self.length+=1

    def delete_from_head(self):
        if self.is_empty():
            return None
        curr = self.head
        self.head = curr.next
        curr.next = None
        self.length -= 1
        return curr.val

    def delete_nodes_with_value(self, key: int):
        prev = None
        curr = self.head

        while curr:
            if curr.val == key:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next
                curr = curr.next
                self.length -= 1
            else:
                prev = curr
                curr = curr.next

