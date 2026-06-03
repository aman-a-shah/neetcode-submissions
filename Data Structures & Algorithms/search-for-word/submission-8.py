class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def helper(row, col, index):
            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                return False
            if (row, col) in visited:
                return False
            if word[index] != board[row][col]:
                return False
            if index == len(word) - 1:
                return True

            visited.add((row, col))
            result = (helper(row-1, col, index+1) or
                      helper(row, col-1, index+1) or
                      helper(row+1, col, index+1) or
                      helper(row, col+1, index+1))
            visited.remove((row, col))
            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if helper(row, col, 0):
                    return True
        return False