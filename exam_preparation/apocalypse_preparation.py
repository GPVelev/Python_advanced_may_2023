from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

created_items = {"MedKit": 0, "Bandage": 0, "Patch": 0}

while True:
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
        break
    if not textiles:
        print("Textiles are empty.")
        break
    if not medicaments:
        print("Medicaments are empty.")
        break

    textile = textiles.popleft()
    medicament = medicaments.pop()

    sum_materials = textile + medicament
    if sum_materials == 30:
        created_items["Patch"] += 1
    elif sum_materials == 40:
        created_items["Bandage"] += 1
    elif sum_materials == 100:
        created_items["MedKit"] += 1
    elif sum_materials > 100:
        created_items["MedKit"] += 1
        sum_materials -= 100
        medicaments[-1] += sum_materials
    else:
        medicament += 10
        medicaments.append(medicament)


sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
