inp_string = list(input())

stack = []

for i in range(len(inp_string)):
    stack.append(inp_string.pop())

print("".join(stack))
