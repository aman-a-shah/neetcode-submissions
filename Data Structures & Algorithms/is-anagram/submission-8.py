class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_lets = sorted(s)
        t_lets = sorted(t)

        return s_lets == t_lets