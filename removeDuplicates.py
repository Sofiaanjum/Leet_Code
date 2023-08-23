# Code to Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        return left

# Ex
solution = Solution()
nums = [1,2,2,4,5,5,5,5,6,7,7,7,8,8,9]
ans = solution.removeDuplicates(nums)
print(ans)