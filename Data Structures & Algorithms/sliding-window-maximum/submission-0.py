class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        len_nums = len(nums)
        left = 0
        output = []

        for i in range(len_nums-k +1):
            output.append(max(nums[i:i+k]))
        return output
        