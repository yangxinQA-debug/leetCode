import collections

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        visited = set()
        que = collections.deque()
        que.append((0, 0))
        visited.add((0, 0))
        while len(que):
            node = que.popleft()
            a, b = node
            if a == z or b == z or a + b == z:
                print(True)
                return True
            # if node not in visited:
            states = self.generate_nodes(a, b, x, y)
            for state in states:
                if state not in visited:
                    visited.add(state)
                    que.append(state)
        print(False)
        return False

    def generate_nodes(self, a, b, x, y):
        states = []
        # 装满水
        state1 = (x, b)
        states.append(state1)
        state2 = (a, y)
        states.append(state2)
        # 倒出水
        state3 = (0, b)
        states.append(state3)
        state4 = (a, 0)
        states.append(state4)
        # A->B
        if a + b > y:
            state5 = (a + b - y, y)
            states.append(state5)
        else:
            state6 = (0, a + b)
            states.append(state6)
        # B->A
        if a + b > x:
            state7 = (x, a + b - x)
            states.append(state7)
        else:
            state8 = (a + b, 0)
            states.append(state8)
        return states


if __name__ == "__main__":
    solution = Solution()
    solution.canMeasureWater(x=2, y=6, z=5)