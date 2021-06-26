# https://leetcode.com/problems/valid-palindrome/

"""
1. 문자열을 소문자로 치환해준다.
2. 알파벳과 숫자를 제외한 문자열을 삭제해준다.
3. 문자열을 join해서 리턴한 후, 뒤집은 문자열과 비교해서 결과를 리턴한다.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))
        return s == s[::-1]


"""
Runtime: 36 ms, faster than 95.55% of Python3 online submissions for Valid Palindrome.
Memory Usage: 15.4 MB, less than 31.79% of Python3 online submissions for Valid Palindrome.
"""