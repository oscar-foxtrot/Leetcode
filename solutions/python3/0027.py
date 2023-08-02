class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        def spec_compare(a: int) -> bool:
            if a == val:
                return True
            else:
                return False

        nums.sort(key=spec_compare)
        counter = len(nums) - nums.count(val)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del(nums[i])
            else:
                break
        return counter
