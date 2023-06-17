from collections import deque


tools = deque(int(x) for x in input().split())
substances = deque(int(x) for x in input().split())
challenges = list(int(x) for x in input().split())

while True:
        if not substances or not tools or not challenges:
            break
        tool = tools.popleft()
        substance = substances.pop()
        crafted = tool * substance


        for challenge in challenges:
            if crafted == challenge:
                challenges.remove(challenge)
                break

        else:
            tool += 1
            tools.append(tool)
            substance -= 1
            if substance > 0:
                substances.append(substance)



if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(tool) for tool in tools)}")
if substances:
    print(f"Substances: {', '.join(str(substance) for substance in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(challenge) for challenge in challenges)}")





