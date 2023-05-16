class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def count(self):
        return len(self.stack)

pairs : {
    '{':'}',
    '(':')',
    '[':']'
}

bracket_integers = Stack()
parentheses = input()

balanced = True

for index, bracket in enumerate(parentheses):
    if bracket in pairs.keys