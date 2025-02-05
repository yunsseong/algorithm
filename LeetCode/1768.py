class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = ''.join([word1[i] + word2[i] for i in range(min(len(word1), len(word2)))])
        if len(word1) > len(word2):
            return sol + word1[len(word2) - len(word1):]
        elif len(word1) < len(word2):
            return sol + word2[len(word1) - len(word2):]
        return sol