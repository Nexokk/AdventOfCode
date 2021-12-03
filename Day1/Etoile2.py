increase = 0
decrease = 0

previous = [0, 0, 0]

with open('input.txt') as f:
    for i in range(3):
        line = f.readline()

        if not line :
            break

        previous[i] = int(line)

    while True :
        actual = [0, 0, 0]

        for i in range(2):
            actual[i] = previous[i+1]

        line = f.readline()

        if not line :
            break

        actual[2] = int(line)

        if sum(previous) < sum(actual) :
            increase += 1
        elif sum(previous) > sum(actual) :
            decrease += 1

        previous = actual

print(increase)
print(decrease)