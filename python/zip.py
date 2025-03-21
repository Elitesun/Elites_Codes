# Example: Iterate over two lists simultaneously
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f'{name}: {score}')