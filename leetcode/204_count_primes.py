# https://leetcode.com/problems/count-primes/

"""
Brute Force O(n^2) Approach: Time Limit Exceeded
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        
        def isPrime(num):
            for i in range(2, num):
                if num % i == 0:
                    return False
            
            return True
        cnt = 0
        
        for i in range(2, n):
            if isPrime(i):
                cnt += 1
                
        return cnt    
            

"""
Used Sieve of Eratosthenes algorithm
Referred to : https://leetcode.com/problems/count-primes/discuss/435363/Python3-Simple-Code-How-to-Make-Your-Code-Faster
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0     ###// No prime number less than 2
        lst = [1] * n          ###// create a list for marking numbers less than n
        lst[0] = lst[1] = 0    ###// 0 and 1 are not prime numbers
        m = 2
        while m * m < n:       ###// we only check a number (m) if its square is less than n
            if lst[m] == 1:    ###// if m is already marked by 0, no need to check its multiples.
			
			    ###// If m is marked by 1, we mark all its multiples from m * m to n by 0. 
			    ###// 1 + (n - m * m - 1) // m is equal to the number of multiples of m from m * m to n
                lst[m * m: n: m] = [0] *(1 + (n - m * m - 1) // m)
				
			###// If it is the first iteration (e.g. m = 2), add 1 to m (e.g. m = m + 1; 
			### // which means m will be 3 in the next iteration), 
            ###// otherwise: (m = m + 2); This way we avoid checking even numbers again.	
            m += 1 if m == 2 else 2
        return sum(lst)


"""
Runtime: 316 ms, faster than 97.90% of Python3 online submissions for Count Primes.
Memory Usage: 103.6 MB, less than 21.31% of Python3 online submissions for Count Primes.
"""