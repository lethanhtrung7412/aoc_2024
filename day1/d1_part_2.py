import csv

left = []

right = []

with open('data.csv', newline='') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        a, b = line[0].split()

        left.append(int(a))
        right.append(int(b))

right_dict = {}

for item in right:
    if item in right_dict:
        right_dict[item] += 1
    else:
        right_dict[item] = 1

compare_dict = {item: right_dict.get(item, 0) for item in left}

result = 0

for i in range(len(left)):
    if left[i] in compare_dict:
        result += left[i] * compare_dict[left[i]]

print(result)
