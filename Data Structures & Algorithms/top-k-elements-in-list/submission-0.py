class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        for i in range(len(nums)):
            groups[nums[i]] = groups.get(nums[i], 0) + 1
        groups = dict(sorted(groups.items(),key=lambda item: item[1], reverse=True))
        return list(groups.keys())[:k]
        