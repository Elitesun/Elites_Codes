x, y = input("Enter two numbers separated by a space: ").split()
x, y = int(x), int(y)
print(f"The sum of {x} and {y} is {x + y}.")



print("Enter a list of items, one per line (type 'done' to finish):")
items = []
while True:
    item = input()
    if item.lower() == 'done':
        break
    items.append(item)
print(f"You entered: {items}")