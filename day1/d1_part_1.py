import csv

left = []

right = []

with open('data.csv', newline='') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        a, b = line[0].split()
        
        left.append(int(a))
        right.append(int(b))

result = 0
left.sort()
right.sort()

for i in range(len(left)):
    result += abs(left[i] - right[i])

print(result)