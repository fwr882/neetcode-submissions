class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first_dict = {}
        second_dict = {}

        for char in s:
            first_dict[char] = 1 + first_dict.get(char, 0)
        for char in t:
            second_dict[char] = 1 + second_dict.get(char, 0)
        return first_dict == second_dict
            
        


        
