# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for str in strs:
            arr = [0] * 26
            for c in str:
                arr[ord(c) - 97] += 1
            if tuple(arr) in dic:
                dic[tuple(arr)].append(str)
            else:
                dic[tuple(arr)] = [str]
        return dic.values()
