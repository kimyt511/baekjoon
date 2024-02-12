# 169 Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        curr_num = 0
        curr_count = 0
        for num in nums:
            if curr_num == num:
                curr_count += 1
            else:
                curr_count -= 1
                if curr_count < 0:
                    curr_num = num
                    curr_count = 1
        return curr_num
