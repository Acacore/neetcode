class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_track = 0
        if len(nums) == 0:
            return long_track

        num_set = set(nums)
        

      
        for num in nums:
            if num-1 not in num_set:
                current_num = num
                count = 1

                while current_num +1 in num_set:
                    current_num = current_num + 1
                    count += 1
                if long_track < count:
                    long_track = count
        return long_track
                

        