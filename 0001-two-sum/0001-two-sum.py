class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # memo = {}
        # for index, num in enumerate(nums):
        #     diff = target - num
        #     if diff in memo:
        #         return [memo[diff],index]
        #     memo[num] = index
        # return
    #brute force
        count = len(nums)
        for i in range(count-1):
            for j in range(i+1,count):
                if (nums[i]+nums[j]==target):
                    return [i,j]
