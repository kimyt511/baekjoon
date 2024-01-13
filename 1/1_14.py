# 1347 Minimum Number of Steps to Make Two Strings Anagram
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        arr = [0] * 26
        for i in s:
            arr[ord(i) - 97] += 1
        for i in t:
            arr[ord(i) - 97] -= 1
        ans = 0
        for i in arr:
            ans += abs(i)
        return ans // 2
