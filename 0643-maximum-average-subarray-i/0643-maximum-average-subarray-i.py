class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum=sum(nums[:k])
        max_average=window_sum/k
        for right in range(k,len(nums)):
            window_sum+=nums[right]-nums[right-k]
            max_average=max(max_average,window_sum/k)
        return max_average





        