from collections import deque

fireworks_effects = deque(int(x) for x in input().split(", "))
explosive_power = deque(int(x) for x in input().split(", "))

created_fireworks = {"Palm firework": 0, "Willow firework": 0, "Crossette firework": 0}
while True:
    if not fireworks_effects:
        break
    if not explosive_power:
        break
    current_firework_effect = fireworks_effects.popleft()
    current_explosive_power = explosive_power.pop()
    if current_firework_effect <= 0:
        explosive_power.append(current_explosive_power)
        continue
    if current_explosive_power <= 0:
        fireworks_effects.appendleft(current_firework_effect)
        continue

    sum_firework = current_firework_effect + current_explosive_power

    if sum_firework % 3 == 0:
        if sum_firework % 5 == 0:
            created_fireworks["Crossette firework"] += 1
            continue
        if sum_firework % 5 != 0:
            created_fireworks["Palm firework"] += 1
            continue
    elif sum_firework % 3 != 0 and sum_firework % 5 == 0:
        created_fireworks["Willow firework"] += 1
        continue
    else:
        current_firework_effect -= 1
        fireworks_effects.append(current_firework_effect)
        explosive_power.append(current_explosive_power)
        continue

if created_fireworks["Palm firework"] >= 3 and created_fireworks["Willow firework"] >= 3 and created_fireworks["Crossette firework"] >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f'Firework Effects left: {", ".join(str(x) for x in fireworks_effects)}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(str(x) for x in explosive_power)}')

print(f'Palm Fireworks: {created_fireworks["Palm firework"]}')
print(f'Willow Fireworks: {created_fireworks["Willow firework"]}')
print(f'Crossette Fireworks: {created_fireworks["Crossette firework"]}')
