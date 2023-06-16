from collections import deque


eggs = deque(int(x) for x in input().split(", "))
papers = deque(int(x) for x in input().split(", "))

boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    paper = papers.pop()

    if egg == 13:
        papers.append(paper)
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    wrapped_egg = egg + paper
    if wrapped_egg <= 50:
        boxes += 1
    else:
        continue

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(egg) for egg in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
