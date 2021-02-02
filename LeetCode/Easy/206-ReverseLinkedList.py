"""
LINK: https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList_iterative(head):
    if head is None:
        return None
    
    new_head = ListNode(val=head.val, next=None)
    
    while head.next is not None:
        head = head.next
        new_head = ListNode(val=head.val, next=new_head)
        
    return new_head


def reverseList_recursive(head):
    if head is None or head.next is None:
        return head
    
    new_head = reverseList_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head