#20
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
print(result)

#21
words = ["Ajay", "Python", "Django"]
lengths = [len(word) for word in words]
print(lengths)


#22
files = ["data.csv", "report.pdf", "image.png"]
extensions = [file.split(".")[1] for file in files]
print(extensions)

#23
ascii_dict = {ch: ord(ch) for ch in "ABC"}
print(ascii_dict)

#24
keys = ['a', 'b', 'c']
values = [1, 2, 3]
result = {k: v for k, v in zip(keys, values)}
print(result)


#25
primes = [n for n in range(2, 101)
          if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print(primes)

#26
pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pairs)

#27
palindromes = [n for n in range(1, 101) if str(n) == str(n)[::-1]]
print(palindromes)

#28
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = [x + y for x, y in zip(list1, list2)]
print(result)

#29
students = [
    {'name': 'Ajay', 'marks': 80},
    {'name': 'Riya', 'marks': 90}
]
names = [student['name'] for student in students]
print(names)


#30
palindromes = [n for n in range(1, 1001) if str(n) == str(n)[::-1]]
print(palindromes)

#31
words = ['apple', 'ant', 'banana', 'ball']
result = [word for word in words if word.startswith('a')]
print(result)

#32
numbers = [n for n in range(1, 21) if n % 2 == 0 or n % 3 == 0]
print(numbers)

#33
coordinates = [[x, y] for x in range(3) for y in range(3)]
print(coordinates)