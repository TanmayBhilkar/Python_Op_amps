import itertools
numbers = [45, 35, 138, 43, 67]
result = []
for permutation in itertools.permutations(str(number) for number in numbers):
   result.append(''.join(permutation))
maximum = max(result, key=int)
print(int(maximum))