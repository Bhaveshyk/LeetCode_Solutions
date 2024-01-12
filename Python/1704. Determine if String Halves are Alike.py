'''
Runtime: 40ms
Memory: 17.39MB
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        vowels = set('aeiou')
        
        count_a = sum(1 for char in s[:mid].lower() if char in vowels)
        count_b = sum(1 for char in s[mid:].lower() if char in vowels)
        
        return count_a == count_b
        
