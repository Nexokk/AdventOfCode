aim = 0
length = 0
depth = 0

with open('data.txt', 'r') as f:

    for line in f :

        s = line.split()

        if s[0] == 'forward' :
            length += int(s[1])
            depth += (int(s[1]) * aim)
        elif s[0] == 'down' :
            aim += int(s[1])
        elif s[0] == 'up' :
            aim -= int(s[1])

print(depth)
print(length)
print(depth*length)