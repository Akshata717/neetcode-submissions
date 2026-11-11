class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest = 0

        for num in new_set:

            if num - 1 not in new_set:
                current = num
                count = 1

                while current + 1 in new_set:
                    count +=1
                    current +=1
                longest = max(longest, count)

        return longest

