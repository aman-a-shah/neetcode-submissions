class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted(word)

        chars_map = {}
        for wrd in strs:
            char_map = ''.join(sorted(wrd))
            if char_map in chars_map:
                chars_map[char_map].append(wrd)
            else:
                chars_map[char_map] = [wrd]
        return list(chars_map.values())