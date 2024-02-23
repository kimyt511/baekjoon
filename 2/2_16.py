# 2971 Find Polygon with the Largest Perimeter
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums)
        arr.reverse()
        sums = sum(nums)
        for i in range(len(nums) - 2):
            sums -= arr[i]
            if sums > arr[i]:
                return sums + arr[i]
        return -1
