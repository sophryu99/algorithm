# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        res = set()
        for i in range(len(emails)):
            splitidx = emails[i].index('@')
            local = emails[i][0:splitidx]
            domain = emails[i][splitidx:]
            local = local.replace('.', '')
            if '+' in local:
                local = local[0: local.index('+')]
            
            address = local + domain
            res.add(address)
        
        return (len(res))

"""
Runtime: 48 ms, faster than 79.05% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 14.5 MB, less than 29.59% of Python3 online submissions for Unique Email Addresses."""