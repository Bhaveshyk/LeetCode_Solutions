'''
Level: Medium
Runtime: 31 ms
Memory Usage: 13.8 MB
'''

class Solution:
    def reverse(self, x: int) -> int:
        r = int(str(abs(x))[::-1])
        return (-r if x < 0 else r) if r.bit_length() < 32 else 0
