"""
You’re given the pointer to the head node of a doubly linked list. Reverse the order of the nodes in the list. The head node might be NULL to indicate that the list is empty. Change the next and prev pointers of all the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Function Description

Complete the reverse function in the editor below. It should return a reference to the head of your reversed list.

reverse has the following parameter(s):

    head: a reference to the head of a DoublyLinkedList

Input Format

The first line contains an integer

, the number of test cases.

Each test case is of the following format:

    The first line contains an integer 

, the number of elements in the linked list.
The next

    lines contain an integer each denoting an element of the linked list.

Constraints

Output Format

Return a reference to the head of your reversed list. The provided code will print the reverse array as a one line of space-separated integers for each test case.

Sample Input

1
4
1
2
3
4

Sample Output

4 3 2 1 

Explanation

The initial doubly linked list is:
The reversed doubly linked list is: 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):

    temp = None
    curr = head

    while curr != None:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp

        curr = curr.prev

    if temp != None:
        head = temp.prev

    return head

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input())

    # for t_itr in range(t):
    #     llist_count = int(input())

    #     llist = DoublyLinkedList()

    #     for _ in range(llist_count):
    #         llist_item = int(input())
    #         llist.insert_node(llist_item)

    #     llist1 = reverse(llist.head)

    #     print_doubly_linked_list(llist1, ' ', fptr)
    #     fptr.write('\n')

    # fptr.close()

    

    t = 1

    n = [4]

    for t_itr in range(t):
        llist_count = n[t_itr]

        llist = DoublyLinkedList()

        array = [1, 2, 3, 4]

        for _ in range(llist_count):
            llist_item = array[_]
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        while llist1:
            print(llist1.data)

            llist1 = llist1.next

