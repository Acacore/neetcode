class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix = 1

        sol = []
        for i in range(n):
            output[i]=prefix
            prefix *= nums[i]
        # print("Hello")
        # print(output)
       
        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]


    
        return output