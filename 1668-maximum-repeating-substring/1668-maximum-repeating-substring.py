class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        co=0
        while word*(co+1) in sequence:
            co+=1

        return co
        