# insert_value_into_sorted_linked_list(list_node, value)
"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in list_node, since this is what you will be asked to accomplish in an interview.

You have a singly linked list list_node, which is sorted in strictly increasing order, and an integer value. Add value to the list list_node, preserving its original sorting.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node list_node of the linked list

Example

For list_node = [1, 3, 4, 6] and value = 5, the output should be
insert_value_into_sorted_linked_list(list_node, value) = [1, 3, 4, 5, 6];
For list_node = [1, 3, 4, 6] and value = 10, the output should be
insert_value_into_sorted_linked_list(list_node, value) = [1, 3, 4, 6, 10];
For list_node = [1, 3, 4, 6] and value = 0, the output should be
insert_value_into_sorted_linked_list(list_node, value) = [0, 1, 3, 4, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer list_node

A singly linked list of integers sorted in strictly increasing order. Thus, all integers in the list are pairwise distinct.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer value

A single integer value to be inserted into list_node. It is guaranteed that there is not an element equal to value in list_node before the insertion is performed.

Guaranteed constraints:
-109 ≤ value ≤ 109.

[output] linkedlist.integer

Return list_node after inserting value into it, with the original sorting preserved.


"""


def insert_value_into_sorted_linked_list(list_node, value):
    new_node = ListNode(value)  # node to be inserted
    if list_node is None:
        list_node = new_node
        return list_node

    if list_node.value > value:
        new_node.next = list_node
        list_node = new_node
        return list_node

    current_node = list_node
    while current_node.next is not None:
        if current_node.next.value > value and current_node.value <= value:
            new_node.next = current_node.next
            current_node.next = new_node
            return list_node

        current_node = current_node.next

    current_node.next = new_node

    return list_node


#
#
#
#
# merge_two_sorted_linked_lists(head1, head2):
"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing order.
"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def merge_two_sorted_linked_lists(l1, l2):
    # iterate through each node in each linked list
    # if l1 == l2, append l1 and l2
    # else if l1 < l2, append l1 then l2
    # else if l2 > l1, append l2 then l1
    dummy_node = ListNode(0)

    tail = dummy_node  # tail stores our final node
    while True:  # need loop so we can break out
        if l1 is None:  # l1 is empty
            tail.next = l2  # add all of l2 to our tail
            break  # EXIT LOOP

        if l2 is None:  # l2 is empty
            tail.next = l1  # add all of l1 to our tail
            break  # EXIT LOOP

        if l1.value <= l2.value:  # if l1 element is less than or equal to l2 element
            tail.next = l1  # then add l1 to our list
            l1 = l1.next  # advance l1

        else:  # l2 element is greater than l1 element
            tail.next = l2  # add l2 to our list
            l2 = l2.next  # advance l2

        tail = tail.next  # advance our tail

    return dummy_node.next


# reverse_nodes_in_k_groups(list_node, k)
#
#
#
#
#
#
#
# reverse_nodes_in_k_groups(list_node, k)
"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in list_node, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list list_node, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of list_node. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

EXAMPLE CALLS
For list_node = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(list_node, k) = [2, 1, 4, 3, 5];
For list_node = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(list_node, k) = [1, 2, 3, 4, 5];
For list_node = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(list_node, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer list_node

A singly linked list of integers.

Guaranteed constraints:
1 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer k

The size of the groups of nodes that need to be reversed.

Guaranteed constraints:
1 ≤ k ≤ list_node size.

[output] linkedlist.integer

The initial list, with reversed groups of k elements.


"""


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def check_remaining_node_count(list_node, k):
    idx = 0
    current_node = list_node
    failed = False
    while idx < k and not failed:
        if current_node is None:
            failed = True
        else:
            current_node = current_node.next
        idx += 1

    return failed


def reverse_nodes_in_k_groups(list_node, k):
    current_node = list_node
    next_node = None
    prev_node = None
    count = 0

    while current_node is not None and count < k:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
        count += 1

    if next_node is not None:
        multiples_avail = check_remaining_node_count(next_node, k)
        if not multiples_avail:
            list_node.next = reverse_nodes_in_k_groups(next_node, k)
        else:
            list_node.next = next_node

    return prev_node
