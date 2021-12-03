increase = 0
decrease = 0

with open('data.txt') as f:
    line = f.readline()

    if not line :
        exit()

    previous = int(line)

    while line:
        line = f.readline()

        if not line :
            break
        
        if previous < int(line) :
            increase += 1
        elif previous > int(line) :
            decrease += 1

        previous = int(line)

print(increase)
print(decrease)