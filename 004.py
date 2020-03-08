# -*-coding:utf-8
"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        时间要求log(m+n)，所以使用二分查找的方法
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 0:
            # 偶数找第k 和 k+1个数
            k = (len1 + len2) / 2
            k1 = (len1 + len2) / 2 + 1
        else:
            # 奇数找第k个数
            k = (len1 + len2) / 2 + 1
        flag = 0
        flag1 = 0
        flag2 = 0
        while (k != 1 and len(nums1) != 0 and len(nums2) != 0):
            mid = k / 2
            if (len(nums1) < mid):
                index1 = len(nums1) - 1
            else:
                index1 = k / 2 - 1
            if (len(nums2) < mid):
                index2 = len(nums2) - 1
            else:
                index2 = k / 2 - 1
            if (nums1[index1] < nums2[index2]):
                # nums1里的[0:index1]不会是第k个数，去掉这些数字
                flag1 = 0
                flag2 = index2
                nums1 = nums1[index1 + 1:]
                k -= index1 + 1
            else:
                flag1 = index1
                flag2 = 0
                nums2 = nums2[index2 + 1:]
                k -= index2 + 1
        if (len(nums1) == 0):
            kth = nums2[k - 1]
            if(len(nums2) >1):
              kth1 = nums2[k]
        elif(len(nums2) == 0):
            kth = nums1[k - 1]
            if (len(nums1) >1):
               kth1 = nums1[k]
        elif (k == 1):
            ## 两个数组都未走到最长结尾
            if (nums1[flag1] < nums2[flag2]):
                kth = nums1[flag1]
                if (len(nums1) <= flag1 + 1):
                    kth1 = nums2[flag2]
                else:
                    kth1 = min(nums1[flag1 + 1], nums2[flag2])
            else:
                kth = nums2[flag2]
                kth1 = -1
                if (len(nums2) <= flag2 + 1):
                    kth1 = nums1[flag1]
                else:
                    kth1 = min(nums1[flag1], nums2[flag2 + 1])
        if (len1 + len2) % 2 == 0:
            print (kth, kth1)
            return float(kth+kth1)/2
        else:
            print (kth)
            return kth


if __name__ == "__main__":
    # nums1 = [1, 3]
    # nums2 = [2]
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    nums1 = []
    nums2 = [1]
    solution = Solution()
    solution.findMedianSortedArrays(nums1, nums2)
