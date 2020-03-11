# -*-coding:utf-8
"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def buildLink(self, l):
        i = 0
        head = ln = ListNode(l[i])
        while i < len(l) - 1:
            rn = ListNode(l[i + 1])
            ln.next = rn
            ln = rn
            i+=1
        return head

    def addTwoNumbers(self, l1_arr, l2_arr):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        i = 0
        carry_flag = 0
        l1 = self.buildLink(l1_arr)
        l2 = self.buildLink(l2_arr)
        result = []
        while (l1 is not None) and (l2 is not None):
            this = 0
            add = l1.val + l2.val
            if carry_flag == 1:
                this += 1
            if (l1.val + l2.val < 10):
                this += add
                carry_flag = 0
            else:
                this += add % 10
                carry_flag = 1
            # sum += pow(10, i) * this
            result.append(this)
            i += 1
            l1 = l1.next
            l2 = l2.next
        if (l1 is None):
            while (l2 is not None):
                # sum += pow(10, i) * l2.val
                result.append(this)
                i += 1
                l2 = l2.next
        if (l2 is None):
            while (l1 is not None):
                # sum += pow(10, i) * l1.val
                result.append(this)
                i += 1
                l1 = l1.next
        print(result)
        return sum


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    solution = Solution()
    solution.addTwoNumbers(l1, l2)
