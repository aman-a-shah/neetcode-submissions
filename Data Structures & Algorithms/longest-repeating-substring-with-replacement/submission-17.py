class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        state = {}

        for right in range(len(s)):
            if s[right] in state:
                state[s[right]] += 1
            else:
                state[s[right]] = 1
            
            max_occ = max(state.values())

            while (right-left+1) - max_occ > k:
                state[s[left]] -= 1
                left += 1

            result = max(result, right-left+1)


        return result