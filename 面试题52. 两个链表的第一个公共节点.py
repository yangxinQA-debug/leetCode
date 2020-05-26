# -*- coding:utf-8
"""
输入两个链表，找出它们的第一个公共节点。

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB
        countp = 0
        countq = 0
        while p != None:
            countp += 1
            p = p.next
        while q != None:
            countq += 1
            q = q.next
        gap = countp - countq

        p, q = headA, headB
        if gap > 0:
            for i in range(gap):
                p = p.next
        elif gap < 0:
            for j in range(-gap):
                q = q.next
        while p != None and q != None and p != q:
            p = p.next
            q = q.next
        if p == q:
            return p
        else:
            return None
