'''
Runtime: 60 ms
Memory Usage: 14 MB
'''

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(word.split()) for word in sentences)
