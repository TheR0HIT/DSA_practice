class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i


# ---- Run & Test ----
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    print(sol.twoSum(nums, target))

        