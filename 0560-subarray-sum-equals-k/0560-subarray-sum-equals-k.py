class Solution(object):
    def subarraySum(self, nums, k):
        seen={0:1}
        target_sum=0
        count=0
        for i in nums:
            target_sum+=i
            target=target_sum-k
            count+=seen.get(target,0)
            seen[target_sum]=seen.get(target_sum,0)+1
        return count
        