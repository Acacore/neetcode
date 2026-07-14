class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = []
        q = deque()
        right = 0

        while right < len(nums):
            if q and q[0] < right - k + 1:
                q.popleft()

            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            if right >= k-1:
                count.append(nums[q[0]])
            right += 1
        
        return count

        