class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenset = []
        for n in nums:
            if n in seenset:
                return True
            seenset.append(n)      
        return False