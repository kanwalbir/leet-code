// https://leetcode.com/problems/two-sum/description/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
  let nums_map = new Map();

  nums.forEach((elem, idx) => {
    nums_map.has(elem)
      ? nums_map.set(elem, nums_map.get(elem).concat([idx]))
      : nums_map.set(elem, [idx]);
  });

  if (nums_map.has(target / 2) && nums_map.get(target / 2).length > 1) {
    return nums_map.get(target / 2).slice(0, 2);
  }

  for (let [key, val] of nums_map) {
    if (nums_map.has(target - key)) {
      return [val[0], nums_map.get(target - key)[0]];
    }
  }

  return null;
};

nums1 = [7, 2, 15, 11];
console.log(twoSum(nums1, 9));

nums2 = [-2, 7, 11, 13, -3];
console.log(twoSum(nums2, 10));

nums3 = [3, 3, 3];
console.log(twoSum(nums3, 6));

nums4 = [4, 5, 6];
console.log(twoSum(nums4, 15));
