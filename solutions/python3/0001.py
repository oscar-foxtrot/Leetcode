class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}  # Let's have a dict of pairs "number: index_of_this_number"
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            else:
                hashmap[nums[i]] = i
        exit(1)
