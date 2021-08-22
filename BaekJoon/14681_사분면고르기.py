# https://www.acmicpc.net/problem/14681

x= int(input())
y= int(input())

if x > 0 and y > 0 :	# x,y: 양수
    print('1')
elif x < 0 and y > 0 :	# x:음수, y:양수
    print('2')
elif x < 0 and y < 0 :	# x,y: 음수
    print('3')
else:
    print('4')
