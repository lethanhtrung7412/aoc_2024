import csv

result = 0

def is_sequence_safe(seq): 
    if all(x < y for x, y in zip(seq, seq[1:])) or all(x > y for x, y in zip(seq, seq[1:])): 
        return all(1 <= abs(x - y) <= 3 for x, y in zip(seq, seq[1:])) 
    return False

def can_made_it_safe(seq):
    if is_sequence_safe(seq):
        return True
    for i in range(len(seq)):
        modified_seq = seq[:i] + seq[i+1:]
        if is_sequence_safe(modified_seq):
            return True
    
    return False

with open('test.csv', newline='') as file:
    csvFile = csv.reader(file)

    for line in csvFile:
        data = [int(i) for i in line[0].split()]
        is_safe = is_sequence_safe(data)
        if is_safe:
            result += 1
        else:
            if can_made_it_safe(data):
                result += 1


print(result)