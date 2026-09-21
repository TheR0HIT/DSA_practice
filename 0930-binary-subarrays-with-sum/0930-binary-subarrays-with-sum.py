class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        seen={0:1}
        get_goal=0
        count=0
        for i in nums:
            get_goal+=i
            sum_get=get_goal-goal
            count+=seen.get(sum_get,0)
            seen[get_goal]=seen.get(get_goal,0)+1
        return count
            

        

            
            
       
        