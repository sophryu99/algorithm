# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, S, T):
    positions = list(S.split(','))
    hits = list(T.split())
    print(positions)
    print('hits', hits)
    mapp = [i.split() for i in positions]
    print(mapp)

    for ship in range(len(mapp)):
        first, second = mapp[ship][0], mapp[ship][1]
        for num in range(int(first[0: -1]), int(second[0: -1]) + 1):
            for alp in range(ord(first[-1]), ord(second[-1]) + 1):
                mapp[ship].append((str(num) + chr(alp)))
        
        mapp[ship] = list((set(mapp[ship])))
        mapp[ship].append(len(mapp[ship]))

    print(mapp)

    for h in range(len(hits)):
        for ship in range(len(mapp)):
            if hits[h] in mapp[ship]:
                mapp[ship].remove(hits[h])
    
    sunk = 0
    hitship = 0
    for ship in range(len(mapp)):
        if len(mapp[ship]) - 1 == 0:
            sunk += 1
        elif len(mapp[ship]) - 1 != mapp[ship][-1]:
            hitship += 1 

    print('removed', mapp)

    return ("{},{}".format(sunk, hitship))

