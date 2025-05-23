class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Easier to Start from the end of the statement
        #Skipping any trailing whitespaces at the end of the string
        #Count the characters in the last word
        #Then Return the length of the last word
        i, length = len(s) - 1, 0
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length


       

        
