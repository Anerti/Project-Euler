def fibonacci():
    number_1 = 0
    number_2 = 1
    result = [""] * 11
    temp = 0
    i = 0
    while temp < 4000000:
        temp = number_1 + number_2
        if temp % 2 == 0:
            result[i] = temp
            i += 1
        number_1 = number_2
        number_2 = temp
    final_result = 0
    for i in range(11):
        final_result += result[i]
    print(final_result)


fibonacci()
