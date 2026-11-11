from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)

        # If more than one zero → everything is zero
        if zero_count > 1:
            return [0] * len(nums)

        total = 1
        for num in nums:
            if num != 0:
                total *= num

        res = []

        for num in nums:
            if zero_count == 1:
                # only one zero exists
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                # no zeros
                res.append(total // num)

        return res