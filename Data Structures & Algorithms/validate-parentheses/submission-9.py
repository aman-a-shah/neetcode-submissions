class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        track_open = {'(':')', '{':'}', '[':']'}

        for let in s:
            if let in track_open:
                stack.append(let)
            else:
                if len(stack) <= 0:
                    return False
                if let != track_open[stack.pop()]:
                    return False

        return len(stack) == 0
        