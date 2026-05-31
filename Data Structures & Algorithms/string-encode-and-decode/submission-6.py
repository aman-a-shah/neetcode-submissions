class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i, wrd in enumerate(strs):
            if wrd == "":
                encoded_str += '~'
            else:
                encoded_str += wrd + '`'

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        j = 0

        for i, let in enumerate(s):
            if let == '`':
                decoded_strs.append(s[j:i])
                j = i+1
            elif let == '~':
                j = i+1
                decoded_strs.append("")

        return decoded_strs