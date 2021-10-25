# 044,s4-4
import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        self.stack.pop()

    def out(self):
        print(*self.stack)


s = Stack()

for line in sys.stdin.readlines():
    if '1' == line[0]:
        _, a = map(int, line.split())
        s.push(a)
    else:
        s.pop()
s.out()
