import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()

        for p in string.punctuation:
            paragraph = paragraph.replace(p, " ")

        m = paragraph.split()
        c = {}

        for x in range(len(m)):
            if m[x] in c:
                c[m[x]] += 1
            else:
                c[m[x]] = 1

        ma = 0
        mcw = ""

        for key, value in c.items():
            if key not in banned:
                if value > ma:
                    ma = value
                    mcw = key

        return mcw