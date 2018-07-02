# https://leetcode.com/problems/two-sum/description/

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
            
        if (target / 2 in nums_map) and (len(nums_map[target / 2]) > 1):
            return nums_map[target / 2][:2]
        
        for key in nums_map:
            if (target - key in nums_map):
                return [nums_map[key][0], nums_map[target - key][0]]
            
        return None


nums1 = [7, 2, 15, 11]
print(Solution().twoSum(nums1, 9))

nums2 = [-2, 7, 11, 13, -3]
print(Solution().twoSum(nums2, 10))

nums3 = [3, 3, 3]
print(Solution().twoSum(nums3, 6))

nums4 = [4, 5, 6]
print(Solution().twoSum(nums4, 15))
