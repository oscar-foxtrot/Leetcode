# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        tmp = ListNode((l1.val + l2.val) % 10)
        toadd = (l1.val + l2.val) // 10
        res = tmp
        l1 = l1.next
        l2 = l2.next
        while l1 != None and l2 != None:
            tmp.next = ListNode((toadd + l1.val + l2.val) % 10) # cant to .. = .. = ..
            tmp = tmp.next
            toadd = (toadd + l1.val + l2.val) // 10
            l1 = l1.next
            l2 = l2.next
        if l1 == None:
            l1 = l2
        while l1 != None:
            tmp.next = ListNode((l1.val + toadd) % 10)
            tmp = tmp.next
            toadd = (l1.val + toadd) // 10
            l1 = l1.next
        if toadd:
            tmp.next = ListNode(1) # toadd is always 1 if not 0
        
        return res
            
