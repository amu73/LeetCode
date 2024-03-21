class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # maxSum = nums[0]
        # curSum = 0
        # for i in range(len(nums)):
        #     curSum = max(curSum+nums[i],nums[i])
        #     maxSum = max(curSum, maxSum)
        # return maxSum
        
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(curSum, maxSub)
        return maxSub
        