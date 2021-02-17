"""
Module (name)

description
"""


def main():
    """
    entry point of the script
    """
    #
    # ask user input for a word to be encoded
    #
    text = input('enter a word: ')
    print('word to be encoded: ' + text)
    #
    # 1.transform text into a list
    #
    text = list(text)
    print('tranformation to a list',  text)
    #
    # 2.replace list into unicode
    #
    for index, let in enumerate(text):
        text[index] = ord(let)
    print('on unicode: ', text)
    #
    # 3. Transform the list on binary
    #
    for index, let in enumerate(text):
        text[index] = bin(let)
    print('on binary: ', text)
    #
    # 4. remove 0b from the list
    #
    for index, let in enumerate(text):
        text[index] = let[2:8]
    print('text 6bit: ', text)
    #
    # 5. add zeros on elements to complete the octet
    #
    for index, let in enumerate(text):
        text[index] = let.zfill(8)
    print('1 oct : ', text)
    #
    # 6.list to string
    #
    text = "".join(text)
    print(text)
    #
    # 7. string to list w/ 6 char
    #
    tex = []
    for index in range(0, len(text), 6):
        tex.append(text[index:index+6])
    print(tex)

    #
    # 8. complete 6 char
    #
    texa = []
    for index in tex:
        if len(index) % 6 == 0:
            texa.append(index)
        elif len(index) % 6 != 0:
            texa.append(index.ljust(6, "0"))
    print(texa)
    #
    # 9. convert list into decimal
    #
    texb = []
    for index in tex:
       texb.append(int(index,2))
    print('converted to dec: ', texb)
    #
    # 10. transform into base 64
    #
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    text_base64 = []
    for index, let in enumerate(alpha):
        for letters in texb:
            if index == letters:
                text_base64.append(let)
    print('converted to base64', text_base64)
    #
    # 11. transform to string
    #
    text = "".join(text_base64)
    print('bsae64 string:', text)
    #
    # 12. final output
    # La chaine de caractÃ¨re finale doit avoir une longueur multiple de 4: Indice: reste de la division, //
    #
    output = list(text)
    if len(output) % 4 != 0:
        output.append('=')
        if len(output) % 4 != 0:
            output.append('=')
    output = "".join(output)
    print(output)


if __name__ == '__main__':
    #
    # calls the main function
    #
    main()
