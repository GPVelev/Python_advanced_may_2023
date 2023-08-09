def stock_availability(list_items, *args):
    items_list = []
    for items in list_items:
        items_list.append(items)
    if args[0] == 'delivery':
        for product in args[1:]:
            items_list.append(product)
    elif args[0] == 'sell':
        if len(args) < 2:
            items_list.remove(items_list[0])
        if len(args) >= 2:
            for action in args[1:]:
                if isinstance(action, int):
                    for times in range(int(action)):
                        items_list.remove(items_list[0])
                if isinstance(action, str):
                    if action in items_list:
                        items_list.remove(action)

    return items_list



print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
