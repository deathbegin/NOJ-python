# 044,s4-4
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if not self.stack:
            return
        self.stack.pop()

    def out(self):
        print(*self.stack)
        # print(' '.join(str(i) for i in self.stack))


s = Stack()
while(1):
    # li = input()
    try:
        li = input()
    except:
        break
    if '1' == li[0]:
        s.push(int(li[2:]))
    elif '2'==li[0]:
        s.pop()
    elif li[0] == '0':
        break
s.out()
