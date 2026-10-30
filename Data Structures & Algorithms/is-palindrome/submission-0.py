class Solution:
    def isPalindrome(self, s: str) -> bool:
        normal = []
        for char in s.lower():
            if char.isalnum():
                normal.append(char)

        opposite = normal[::-1]
        return normal == opposite