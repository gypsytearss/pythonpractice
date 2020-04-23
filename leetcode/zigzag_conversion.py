class Solution(object):
    """
    https://leetcode.com/problems/zigzag-conversion/
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for i in range(0, numRows)]
        direction = -1
        current_row = 0

        for c in s:
            rows[current_row].append(c)
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            current_row += direction

        return "".join([i for x in rows for i in x])