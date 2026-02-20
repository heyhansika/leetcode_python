class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Convert digits
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        # Clamp to 32-bit range
        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647

        return num
