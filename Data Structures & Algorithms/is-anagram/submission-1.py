class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    #Two string inputted by user
    #if the first string has the same characters as the other string return true
    #if the they dont return false
        first_word = []
        second_word = []
        for ch in s:
            first_word.append(ch)
        for ch in t:
            second_word.append(ch)
        first_word.sort()
        second_word.sort()
        if first_word == second_word:
            return True
        else:
            return False

my_word = Solution()
print(my_word.isAnagram("racecar","carrace"))

#I put my logic inside the isAnagram function
#I created two different lists for the first and second string
#Then I created a for loop for both of these and appended each 
#character since the characters will be seperated then sorted then do they become alphabetical order
#Then compared them to each other if the sorted version matched then the same characters were used, if not then false is returned.
#As I wrote this I realized that I could've just split the two strings then compared would've been easier
#But this is the point of writing the description after I complete the question so I can learn to approach things better next time.



        