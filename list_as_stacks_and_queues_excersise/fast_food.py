from collections import deque

food_quantity_for_the_day = int(input())
food_quantity = deque(map(int, input().split()))

too_much_orders = False

print(max(food_quantity))

for order in range(len(food_quantity)):
    if food_quantity_for_the_day - food_quantity[0] >= 0:
        food_quantity_for_the_day -= food_quantity.popleft()
    else:
        too_much_orders = True
        print(f"Orders left:", ' '.join([str(order) for order in food_quantity]))
        break
if not too_much_orders:
        print("Orders complete")




