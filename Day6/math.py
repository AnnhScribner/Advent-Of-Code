MULT = "*"
SUM = "+"

matrix = []
with open("Day6/input.txt") as file:
    for line in file:
        l = line.strip()
        
        matrix.append(l.split())

width = len(matrix[0])
height = len(matrix)

elements = []
for h in range(width):
    e = []
    for w in range(height):
        e.append(matrix[w][h])
    elements.append(e)
    
total = 0
for i in range(len(elements)):
    line = elements[i]

    if MULT in line:
        multiplication = 1
        for j in range(0, len(line) - 1):
            num = int(line[j])
            multiplication *= num

        total += multiplication

    if SUM in line:
        for j in range(0, len(line) - 1):
            num = int(line[j])
            total += num

print(total)
