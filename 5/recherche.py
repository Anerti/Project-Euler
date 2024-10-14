def main():  #recherche trop long, algorithme à améliorer
    nb = 21
    temp = 0
    while temp != 20:
        for i in range(1, 21):
            temp = i
            if nb % i != 0:
                break
        nb += 1
    print(nb - 1)


main()
