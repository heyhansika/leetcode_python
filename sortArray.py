class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j]>nums[j+1]:
                   temp = nums[j]
                   nums[j]= nums[j+1]
                   nums[j+1]=temp
        return nums        
