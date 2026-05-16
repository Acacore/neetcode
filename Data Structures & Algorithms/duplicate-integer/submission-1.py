class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy_num = nums
        if len(set(nums)) == len(copy_num):
            return False
        return True
