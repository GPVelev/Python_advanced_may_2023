from collections import deque

number_petrol_pumps = int(input())
pumps = deque()

for pump in range(number_petrol_pumps):
    pumps.append([int(num) for num in input().split()])

for atempt in range(number_petrol_pumps):

    tank = 0
    failed_attempts = False

    for petrol, distance in pumps:
        tank = tank + petrol - distance
        if tank < 0:
            failed_attempts = True
            break
    if failed_attempts:
        pumps.append(pumps.popleft())
    elif not failed_attempts:
        print(atempt)
        break
