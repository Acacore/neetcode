class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_track = 0
        if len(nums) == 0:
            return longest_track

        num_set = set(nums)
        
        for num in nums:
            if (num - 1) not in num_set:
                next_num = num + 1
               

                while next_num in num_set:
                    next_num += + 1
                   
                longest_track = max(longest_track, next_num - num)
        return longest_track