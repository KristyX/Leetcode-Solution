class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        else:
            id = 1
            i =1
            while i < len(nums): 
                if nums[i] != nums[i-1]:
                    nums[id] = nums[i]
                    id += 1
                i += 1
            return id
