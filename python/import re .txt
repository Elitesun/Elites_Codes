import re

a = 'ABCDCDC'
substring = 'CDC'

count = len(re.findall(f'(?={substring})', a))
print(count)

output = 2