class Node:
    def __init__(self, val, nxt=None):  # Constructor
        self.value = val
        self.next = nxt

    def __repr__(self):
        return f'Node({repr(self.value)})'


class LinkedList:
    def __init__(self):  # constructor
        self.head = None

    def insert_at_front(self, val):
        # Make a new node
        new_node = Node(val)
        # Point new node next at head
        new_node.next = self.head
        # Point head to new node
        self.head = new_node

    def print_list(self):
        str_to_print = "\nLIST=["
        # Set cur to head
        cur = self.head

        # Loop while cur.next is not None
        while cur is not None:
            # Print value at cur
            str_to_print += f"{cur.value} "
            # Set cur to cur.next
            cur = cur.next

        str_to_print = str_to_print[:-1] + "]\n"
        # str_to_print += "]\n"
        print(str_to_print)

    def delete_head(self):
        old_next = self.head.next
        self.head.next = None
        self.head = old_next

    def delete_node(self, value):
        # Special case: empty list
        if self.head is None:
            return

        # Special case: delete the head
        if self.head.value == value:
            self.delete_head()
            return

        # General case of deleting something in the middle
        prev = self.head
        cur = self.head.next

        while cur is not None:
            if cur.value == value:
                # print(f"Found it! {prev.value}, {cur.value}")
                prev.next = cur.next
                cur.next = None
                return

            cur = cur.next
            prev = prev.next

        print("Didn't find it")

    def reverse(self, head_of_list):
        current_node = self.head
        previous_node = None
        next_node = None

        # Until we have 'fallen off' the end of the list
        while current_node:
            # Copy a pointer to the next element
            # before we overwrite current_node.next
            next_node = current_node.next

            # Reverse the 'next' pointer
            current_node.next = previous_node

            # Step forward in the list
            previous_node = current_node
            current_node = next_node

        return previous_node

    def reverse_02(self):
        current_node = self.head.next  # second el
        # self.head.next = None
        prev_node = self.head  # head (first el)
        next_node = current_node.next  # third el

        while current_node.next is not None:  # while current_node has a next
            print("---before changes")
            print(f"prev_node={prev_node}")
            print(f"current_node={current_node}")
            print(f"next_node={next_node}")
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = next_node.next
            print("---after changes")
            print(f"prev_node={prev_node}")
            print(f"current_node={current_node}")
            print(f"next_node={next_node}\n")
            # current_node.next = prev_node
            # prev_node = current_node
            # current_node = next_node
            # next_node = next_node.next


ll = LinkedList()
ll.insert_at_front(45)
ll.insert_at_front(88)
ll.insert_at_front(24)
ll.insert_at_front(12)

ll.print_list()

# delete_node(88)
# ll.delete_node(12)

# ll.print_list()

ll.reverse_02()
ll.print_list()

# delete_head()

# print_list()
