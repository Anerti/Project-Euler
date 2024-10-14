def prime():  #Programme lent
    a = 1
    compte = 0
    while compte != 10001:
        i = 1
        nbDivision = 0
        while i <= a:
            if a % i == 0:
                nbDivision += 1
            i += 1
        if nbDivision == 2:
            compte += 1
            print(f"Prime number N°{compte} is {a}")
        a += 1


prime()
