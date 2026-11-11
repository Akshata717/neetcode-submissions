class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []

        for i in range(len(nums)):
            x = 1
            for j in range(len(nums)):
                if (i != j):
                    x = x*nums[j]
                
            new_arr.append(x)
        
        return new_arr
        