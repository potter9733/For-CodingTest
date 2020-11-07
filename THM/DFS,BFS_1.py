#스택

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

#큐

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

#재귀함수의 종료

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료함')
    
recursive_function(1)

