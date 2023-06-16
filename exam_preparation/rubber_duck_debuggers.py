from collections import deque

programmer_time = deque(int(x) for x in input().split())
number_of_tasks = deque(int(x) for x in input().split())

darth_vader_ducky = 0
thor_ducky = 0
big_blue_rubber_ducky = 0
small_yellow_rubber_ducky = 0


while number_of_tasks and programmer_time:
    programmer = programmer_time.popleft()
    task = number_of_tasks.pop()

    if 0 <= programmer * task <= 60:
        darth_vader_ducky += 1
    elif 60 < programmer * task <= 120:
        thor_ducky += 1
    elif 120 < programmer * task <= 180:
        big_blue_rubber_ducky += 1
    elif 180 < programmer * task <= 240:
        small_yellow_rubber_ducky += 1
    else:
        task -= 2
        number_of_tasks.append(task)
        programmer_time.append(programmer)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducky}\n"f"Thor Ducky: {thor_ducky}\n"
            f"Big Blue Rubber Ducky: {big_blue_rubber_ducky}\n"
            f"Small Yellow Rubber Ducky: {small_yellow_rubber_ducky}")
