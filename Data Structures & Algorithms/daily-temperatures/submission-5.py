class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_i, stack_t = stack.pop()
                res[stack_i] = index - stack_i
            stack.append((index, temp))

        return res

        
