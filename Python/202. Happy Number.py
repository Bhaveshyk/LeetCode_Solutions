''' 
Runtime: 49 ms
Memory Usage: 13.8 MB 
'''
    
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            if n in seen:
                return False
            elif n == 1:
                return True
            else:
                seen.add(n)
                n = sum([int(x) ** 2 for x in str(n)])
