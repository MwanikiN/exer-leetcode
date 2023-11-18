# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode()
        current = head
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, out = divmod(val1 + val2 + carry, 10)
            current.next = ListNode(out)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
    

# alternative approach
class ListNode: #ListNode class defines a node in a linked list, where each node has a value (val) and a reference to the next node (next).
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2): #The addTwoNumbers function takes two linked lists l1 and l2 as input.
    dummy = ListNode() #dummy node is created to initialize the result linked list.
    current = dummy #current points to the current node in the result list.
    carry = 0 #carry is used to store the carry over from the addition of two digits.
    
    while l1 or l2 or carry: #The while loop iterates until both l1 and l2 are None, and there is no carry.
        if l1:   #Inside the loop, the values of l1 and l2 (if they exist) are added to carry.
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        
        current.next = ListNode(carry % 10)#A new node with the value carry % 10 is created and added to the result list. carry % 10 keeps the value between 0-9.
        current = current.next
        carry //= 10 #carry //= 10 updates the carry for the next iteration.
    
    return dummy.next
