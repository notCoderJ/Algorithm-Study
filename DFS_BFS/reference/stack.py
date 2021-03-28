# 스택(Stack) 자료구조를 직접 만들어보자!
# 스택에는 자료구조 안에 데이터를 넣는 'Push'연산과 데이터를 꺼내는 'Pop'연산이 필요하다.

# 부록:
#   *args는 함수가 몇 개의 인자를 전달받을지 모를 때 사용할 수 있다.
#   *args로 전달받은 인자는 Tuple형태로 함수에 전달된다.
#   ex) def A(*args) => A(1,2,3) => *args = (1, 2, 3)

#   **kwargs는 *args와 비슷하나 인자를 전달할 때 'key=value'형태로 전달하고
#   **kwargs로 전달받은 인자는 Dictionary형태로 함수에 전달된다.
#   ex) def A(**kwargs) => A(a='1', b='2', c='3') => **kargs = {'a':'1', 'b':'2', 'c':'3'}

class Stack(object):
    def __init__(self, *args):
        self.stack = []
        for i in args:
            self.stack.append(i)
        self.length = len(self.stack)

    def pop(self):
        if self.length == 0: # 스택이 비어있으면 아무것도 꺼내지 않는다
            return
        last_value = self.stack[-1]
        del self.stack[-1]
        self.length = len(self.stack)
        return last_value

    def push(self, *args):
        for i in args:
            self.stack.append(i)
        self.length = len(self.stack)

my_stack = Stack(1, 2, 3, 4, 5)
my_stack.pop()
my_stack.pop()
my_stack.push(7, 8, 9)
my_stack.pop()
my_stack.push(1)
print (my_stack.length, my_stack.stack[::-1]) # 스택의 길이와 스택의 최상단 데이터부터 출력한다

# 사실, 파이썬에서 위와 같이 스택을 만들 필요가 없다.
# 아래와 같이 이미 구현되어있는 리스트의 'append'와 'push'메소드를 사용하면 간단히 스택을 사용할 수 있다.

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.pop()
stack.pop()
stack.append(7)
stack.append(8)
stack.append(9)
stack.pop()
stack.append(1)
print (len(stack), stack[::-1])
