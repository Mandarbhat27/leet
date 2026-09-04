
class Solution(object):
    def myAtoi(self, s):
        b = ""
        
        for c in s:
            if c == " " and b == "":
                continue

            if c in "+-" and b == "":
                b = b + c

            elif c in "1234567890":
                b = b + c

            elif b != "":
                break

            else:
                return 0

        if b == "" or b == "+" or b == "-":
            return 0

        num = 0

        if b[0] == "-":
            for c in b[1:]:
                num = num * 10 + (ord(c) - ord("0"))
            num = -num

        elif b[0] == "+":
            for c in b[1:]:
                num = num * 10 + (ord(c) - ord("0"))

        else:
            for c in b:
                num = num * 10 + (ord(c) - ord("0"))

        if num > (2**31) - 1:
            return (2**31) - 1
        elif num < -(2**31):
            return -(2**31)
        else:
            return num

