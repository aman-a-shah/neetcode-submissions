class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        acc_s = ''
        for let in s:
            if let.isalnum():
                acc_s+=let

        acc_s = acc_s.lower()

        return acc_s == acc_s[::-1]