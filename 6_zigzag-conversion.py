class Solution:
    def convert(self,s: str, numRows: int) -> str:
        """
        Converts a string to a zigzag pattern.

        Args:
            s: The string to convert.
            numRows: The number of rows in the zigzag pattern.

        Returns:
            The converted string.
        """
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        cur_row, going_down = 0, False

        for char in s:
            rows[cur_row] += char
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1


        return ''.join(rows)