# https://leetcode.com/problems/reverse-vowels-of-a-string/


class Solution:
    
    def reverseVowels(self, s):
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)