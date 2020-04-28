# -*-coding:utf-8
"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

 

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
题解：https://leetcode-cn.com/problems/course-schedule/solution/course-schedule-tuo-bu-pai-xu-bfsdfsliang-chong-fa/
"""

from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        que = deque()
        courses = [[] for _ in range(numCourses)]
        innode = [0 for _ in range(numCourses)]
        nums = numCourses
        for cur, pre in prerequisites:
            # 构造邻接矩阵
            courses[pre].append(cur)
            # 构造入度矩阵
            innode[cur] += 1
        for i in range(len(innode)):
            if innode[i] == 0:
                que.append(i)
                nums -= 1
        while len(que) != 0:
            pre = que.popleft()
            for cur in courses[pre]:
                innode[cur] -= 1
                if innode[cur] == 0:
                    que.append(cur)
                    nums -= 1
        if nums != 0:
            print(False)
            return False
        else:
            print(True)
            return True


if __name__ == "__main__":
    solution = Solution()
    solution.canFinish(2, [[1, 0], [0, 1]])
