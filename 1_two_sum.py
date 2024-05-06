class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, value in enumerate(nums):
            try:
                second_index=nums[index+1:].index(target-value)
                return [index, index+second_index+1]
            except:
                pass
