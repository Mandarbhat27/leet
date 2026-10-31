class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"



        while len(word)<k:
            nextw=""
            for x in word:
                nextw+=chr(ord(x)+1)
        
            word=word+nextw

        return word[k-1]

