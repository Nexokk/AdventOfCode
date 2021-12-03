zero = [0 for x in range(12)]
un = [0 for x in range(12)]

gamma = 0
epsilon = 0

with open('data.txt') as f:

    for line in f :
        caractere = 0

        for i in line :
            if i == '1' :
                un[caractere] += 1

            elif i == '0' :
                zero[caractere] += 1
            
            caractere += 1

    for i in range(12) :

        if zero[i] < un[i] :
            gamma = gamma * 10 + 1
            epsilon = epsilon * 10

        else :
            gamma = gamma * 10
            epsilon = epsilon * 10 + 1


print(un)
print(zero)

print("\n")

print(gamma) #3340
print(epsilon) #755