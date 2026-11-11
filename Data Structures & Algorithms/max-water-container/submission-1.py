class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        m = 0
        while(left < right):
            if m < (right - left) * min(heights[left], heights[right]):
                m = (right - left) * min(heights[left], heights[right])

            elif heights[left] <= heights[right]:
                left+=1
            else:
                right-=1     
        
        return m

        