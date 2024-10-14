def palindrome():
    nb1 = 999
    nb2 = 999
    result = 0
    while nb1 >= 100:
        while nb2 >= 100:
            inverse = list(str(nb1 * nb2))
            inverse.reverse()
            inverse = "".join(inverse)
            if inverse == str(nb1 * nb2):
                if result < nb1 * nb2:
                    result = nb1 * nb2
            nb2 -= 1
        nb2 = 999
        nb1 -= 1
    print(result)


palindrome()
