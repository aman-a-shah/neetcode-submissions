class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        formed = 0          # chars whose frequency in window satisfies need
        required = len(need)  # distinct chars we must satisfy

        left = 0
        best = ""

        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1

            # check if this char now meets its required frequency
            if c in need and have[c] == need[c]:
                formed += 1

            # shrink from left while window is valid
            while formed == required:
                window = s[left:right + 1]
                if not best or len(window) < len(best):
                    best = window

                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    formed -= 1
                left += 1

        return best