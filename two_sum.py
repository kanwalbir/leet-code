# https://leetcode.com/problems/two-sum/description/

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums_map = {}
        
        for idx, elem in enumerate(nums):
            if elem in nums_map:
                nums_map[elem].append(idx)
            else:
                nums_map[elem] = [idx]
            
        if (target/2 in nums_map) and (len(nums_map[target/2]) > 1):
            return [nums_map[target/2][0], nums_map[target/2][1]]
        
        for key in nums_map:
            if (target - key in nums_map):
                return [nums_map[key][0], nums_map[target-key][0]]
            
        return None


nums1 = [7, 2, 15, 11]
print(Solution().twoSum(nums1, 9))

nums2 = [-2, 7, 11, 13, -3]
print(Solution().twoSum(nums2, 10))

nums3 = [3, 3]
print(Solution().twoSum(nums3, 6))
