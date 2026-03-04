class Solution:
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = True

        for ch in s:
            rows[current_row] += ch

            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False

            current_row += 1 if going_down else -1

        return "".join(rows)


# test
if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
