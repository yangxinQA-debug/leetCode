# -*- coding:utf-8
"""
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l3 = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            elif l2.val < l1.val:
                p.next = l2
                l2 = l2.next
            elif l1.val == l2.val:
                p.next = l2
                l2 = l2.next
                p = p.next
                p.next = l1
                l1 = l1.next
            p = p.next

        if l1 != None:
            p.next = l1
        if l2 != None:
            p.next = l2
        return l3.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    soluton = Solution()
    soluton.mergeTwoLists(l1, l2)
