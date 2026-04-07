class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_extended = nums
        nums_extended.extend(nums)
        return nums_extended