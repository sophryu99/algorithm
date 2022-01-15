import sys


def solution(S: str) -> str:
  
  d = {}
  # Loop from the back and store the last occuring index
  for i in range(len(S) - 1, -1, -1):
    if S[i] not in d:
      d[S[i]] = i
  
  maxlen = float("-infinity")
  index = 0 
  
  for i in range(len(S)):
    currlen = d[S[i]] + 1 - i
    print(currlen, maxlen, 'before')
    if currlen > maxlen:
      index = i
      maxlen = currlen
    print(currlen, maxlen, 'after')
  return S[index: d[S[index]] + 1]