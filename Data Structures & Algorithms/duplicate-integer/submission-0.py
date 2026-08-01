class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       #check each value in array nums
        someset = set()
        for n in nums:
            if n in someset:
                return True
            someset.add(n)
            
        return False
                


       #match each one 
       #if seen before then return true 
       

