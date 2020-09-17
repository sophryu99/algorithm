# Stack

- 스택 선형구조: 자료 간의 관계가 1대 1의 관계를 가짐
- 기본적 연산
  - 자료를 꺼내거나 삽입
  - Last-in-first-out (LIFO): last elemented inserted can be popped first
- 마지막 삽입된 원소의 위치를 top 이라고 함



> Stack Basics

```python
# push
def push(item):
  s.append(item)
  
# pop
def pop():
  if len(s) == 0:
    # underflow
    return
  else:
    return s.pop(-1)
```



<u>리스트를 사용하여 스택을 구현할 때의 문제점: 리스트의 크기를 변경하는 작업은 많은 시간이 소요된다</u>

- 해결책 1. 리스트의 크기를 미리 배열처럼 정해놓고 사용하는 방법

- 해결책 2. 동적 연결리스트를 이용하여 저장소를 동적으로 할당하여 스택을 구현하는 방법



### Memoization

- 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술
- <u>Dynamic programming</u>의 핵심이 됨



```python
def fibo1(n):
  global memo
  if n >=2 and len(memo) <= n:
    memo.append(fibo1(n-1) + fibo1(n-2))
  return memo[n]

memo[0,1]
```



### Dynamic Programming

- 최적화 문제를 해결하는 알고리즘

1. recursive method: fibo1()
2. iterative method: fibo2()



### DFS (Depth First Search)

- 시작 정점의 한 방향으로 갈 수 있는 경로까지 깊이 탐색
- 더 이상 갈 곳이 없게되면 가장 마지막에 만났던 갈림길 간선이 있던 곳으로 되돌아옴
- 다른 방향의 정점을 탐색하여 모든 정점 방문하며 순회
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이우선 탐색을 반복해야함으로 후입선출 구조의 스택을 사용한다

