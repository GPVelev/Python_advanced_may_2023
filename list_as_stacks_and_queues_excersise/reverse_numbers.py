input_numbers = input().split()

stack = []

for i in range(len(input_numbers)):
    stack.append(input_numbers.pop())

print(" ".join(stack))
