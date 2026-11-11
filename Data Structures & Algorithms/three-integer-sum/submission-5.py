class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since nums is sorted, no later triplet can sum to 0
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            while left < right:
                cur = nums[i] + nums[left] + nums[right]

                if cur == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate left/right values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif cur < 0:
                    left += 1

                else:
                    right -= 1

        return result