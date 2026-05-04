class Solution:
    def threeSum(self, nums):
        index_hashmap = dict(enumerate(nums))

        return index_hashmap


nums = [-1,0,1,2,-1,-4]
solution = Solution()
answer = solution.threeSum(nums)
print(answer)
        