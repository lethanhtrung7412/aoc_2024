import csv

result = 0

def is_sequence_safe(seq): 
    if all(x < y for x, y in zip(seq, seq[1:])) or all(x > y for x, y in zip(seq, seq[1:])): 
        return all(1 <= abs(x - y) <= 3 for x, y in zip(seq, seq[1:])) 
    return False

with open('data.csv', newline='') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        data = [int(i) for i in line[0].split()]
        is_safe = is_sequence_safe(data)
        if is_safe:
            result += 1
        


print(result)