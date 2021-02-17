"""
Methode main

for loop samples
"""


def main():

    loops = 'jesusa'
    #
    # normal loop
    #
    for loop in loops:
        print(loop)

    #
    # loop w/ enumeration
    #
    for n, char in enumerate(loops):
        affiche = f"Index {n + 1} - {char}"
        print(affiche)

    #
    # print 1-5 by 2
    #
    for index in range(1, 5, 2):
        print(index)

    # loop for integer
    for i in range(5):
        print(i)

    # while loop
    count = 2
    while count <= 5:
        print(count)
        count += 1


if __name__ == '__main__':
    main()
