'''
Runtime: 653 ms
Memory Usage: 25.8 MB
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet =  set(nums)
        if len(nums) == len(numsSet):
            return False
        return True
