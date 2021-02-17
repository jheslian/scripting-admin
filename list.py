# arrays
def main():
    listes = ['a', 'b', 'c']
    listes[1] = 't'
    for i in listes:
        print(i)

    # 2dim list
    lists = [
        [0, 1, 2],
        [10, 20, 30]
    ]

    for ligne in lists:
        for contenu in ligne:
            print(contenu)

    #
    # lists1 = []
    # for i in range(10):
    #    lists1.append(i)
    #
    # same as this:
    #
    lis = [i+10 for i in range(10)]
    print(lis)


if __name__ == '__main__':
    main()
