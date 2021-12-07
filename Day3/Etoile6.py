with open('data.txt') as f:

    lines = f.readlines()
    linesbis = lines.copy()

    for j in range(12) :

        zero = 0
        un = 0

        for i in lines :
            
            if i[j] == '1' :
                un += 1
            elif i[j] == '0' :
                zero += 1

        if(zero > un) :
            for elem in list(lines) :
                if elem[j] != '0' :
                    lines.remove(elem)

        else :
            for elem in list(lines) :
                if elem[j] != '1' :
                    lines.remove(elem)

        if len(lines) == 1 :
            break

    for j in range(12) :

        zero = 0
        un = 0

        for i in linesbis :
            if i[j] == '1' :
                un += 1
            elif i[j] == '0' :
                zero += 1

        if(zero <= un) :
            for elem in list(linesbis) :
                if elem[j] != '0' :
                    linesbis.remove(elem)

        else :
            for elem in list(linesbis) :
                if elem[j] != '1' :
                    linesbis.remove(elem)

        if len(linesbis) == 1 :
            break

    print(lines)
    print(linesbis)