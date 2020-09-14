# 가운데 글자 가져오기

# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.

""" ---------- 내 풀이 (pass) ---------- """

def solution(s):
    res = []
    if len(s) % 2 == 0:                 # 단어가 짝수일 때
        res.append(s[len(s)//2 -1])     # 가운데 두 글자 리턴
        res.append(s[len(s)//2])
    else:                               # 홀수일 때
        res.append(s[len(s)//2])        # 가운데 한 글자 리턴
    res = str(''.join(res))             # 리스트 각 element들 합쳐주기
    print(res)