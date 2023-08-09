from collections import deque

armor_value = deque([int(x) for x in input().split(",")])
strike_strength = deque([int(x) for x in input().split(",")])

killed_monsters = 0

while True:
    if not armor_value or not strike_strength:
        break

    current_armor = armor_value.popleft()
    current_strength = strike_strength.pop()

    if current_armor > current_strength:
        current_armor -= current_strength
        armor_value.append(current_armor)
    elif current_armor <= current_strength:
        current_strength -= current_armor
        if strike_strength:
            strike_strength[-1] += current_strength
        elif current_strength > 0:
            strike_strength.append(current_strength)
        killed_monsters += 1


if not armor_value:
    print("All monsters have been killed!")
if not strike_strength:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")