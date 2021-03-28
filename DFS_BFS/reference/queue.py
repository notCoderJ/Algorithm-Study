# 큐(Queue) 자료구조를 직접 만들어보자!
# 큐에는 자료구조 안에 데이터를 넣는 'Enqueue'연산과 데이터를 꺼내는 'Dequeue'연산이 필요하다.

class Queue(object):
    def __init__(self, *args):
        self.queue = []
        for i in args:
            self.queue.append(i)
        self.length = len(self.queue)

    def enqueue(self, *args):
        for i in args:
            self.queue.append(i)
        self.length = len(self.queue)
    
    def dequeue(self):
        if self.length == 0: # 큐가 비어있으면 아무것도 꺼내지 않는다.
            return
        first_value = self.queue[0] # 물론 return self.queue.pop(0)도 가능하다.
        del self.queue[0]
        return first_value

my_queue = Queue(1, 2, 3, 4, 5)
my_queue.dequeue()
my_queue.dequeue()
my_queue.enqueue(7, 8, 9)
my_queue.dequeue()
my_queue.enqueue(1)
print (my_queue.length, my_queue.queue[:]) # 큐의 길이와 맨 앞의 데이터부터 출력한다.

# 큐의 경우 파이썬의 collections 모듈에서 제공하는 deque 자료구조를 사용하면 된다.
# deque은 스택과 큐의 장점을 모두 합한 것으로 데이터를 넣고 뺴는 속도가 리스트에 비해 효율적이다
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.popleft()
queue.popleft()
queue.append(7)
queue.append(8)
queue.append(9)
queue.popleft()
queue.append(1)
print (len(queue), queue)

