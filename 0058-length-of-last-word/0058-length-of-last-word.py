class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.strip().split(' ')
        n = len(new[-1])
        return n
