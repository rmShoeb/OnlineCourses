import re

file_open = open('text3.txt', 'r')
total = 0
for line in file_open:
    numbers = re.findall('[0-9]+', line.rstrip())
    if len(numbers)>0:
        for number in numbers:
            total = total+int(number)
print(total)
