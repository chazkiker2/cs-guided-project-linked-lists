class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({repr(self.value)})"


head = None


def insert_at_front(val):
    pass


insert_at_front(45)
insert_at_front(88)

# Driver Code
n = Node(45)  # construct a node with a value of 45
print(n.value)
print(n.next)
print(n)
