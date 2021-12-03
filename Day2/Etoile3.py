length = 0
depth = 0

with open('data.txt', 'r') as f:

    for line in f :

        s = line.split()

        if s[0] == 'forward' :
            length += int(s[1])
        elif s[0] == 'down' :
            depth += int(s[1])
        elif s[0] == 'up' :
            depth -= int(s[1])

print(depth)
print(length)
print(depth*length)