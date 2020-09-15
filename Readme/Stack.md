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



