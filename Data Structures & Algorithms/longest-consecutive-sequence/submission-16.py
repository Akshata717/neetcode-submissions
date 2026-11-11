class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        longest = 0

        for num in new:

            # num is the start of a sequence
            if num - 1 not in new:
                count = 1
                current = num

                # Keep going while the next number exists
                while current + 1 in new:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest