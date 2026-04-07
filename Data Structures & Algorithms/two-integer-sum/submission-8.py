class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # left = 0
        # right = left + 1

        # for i in nums:
        #     while right < len(nums) -1:
        #         if nums[left]+ nums[right] == target:
        #             return [left, right]
        #         left += 1
        #         right = left + 1 

        dict1 = {}
        for i in range(len(nums)):
            partner = target - nums[i]

            if partner in dict1 :
                return [dict1[partner], i]

            dict1[nums[i]]= i

        