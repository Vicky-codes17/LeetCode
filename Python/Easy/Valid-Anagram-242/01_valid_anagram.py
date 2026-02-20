class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if not d.get(j):
                return False
            else:
                d[j] = d.get(j) - 1
        return True
print(Solution().isAnagram("anagram", "nagaram"))