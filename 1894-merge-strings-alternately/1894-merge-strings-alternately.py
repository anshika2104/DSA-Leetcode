class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged=[]
        minlen=min(len(word1),len(word2))
        for i in range(minlen):
            merged.append(word1[i])
            merged.append(word2[i])
        merged.extend(word1[minlen:])
        merged.extend(word2[minlen:])
        return "".join(merged)
        