
arr = []
for i in range(100):
    arr.append(i)

start = 50
count = 0

with open('Dec1/rotations.txt', 'r') as file:
    lines = file.readlines()
    direction = ''
    moves = 0
    
    for line in lines:
        l = line.strip()
        direction = l[0]
        moves = int(l[1:])
        
        if direction == 'R':
            start = (start + moves) % len(arr)
        elif direction == 'L':
            start = (start - moves) % len(arr)

        number_in_arr = arr[start]
        if number_in_arr == 0:
            count += 1

print(count)