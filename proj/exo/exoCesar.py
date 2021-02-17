"""
Methode  ceasar

function to cypher a message
"""


def ceasar(text, offset):
    """
    cypher the message

    arg:
        text: message to cypher
        offset : offset to apply
    """
    msg = list(text)

    for index, el in enumerate(msg):
        msg[index] = (ord(el) + offset) % 1114112
        msg[index] = chr(msg[index])
    msg = "".join(msg)
    return msg


def main():
    """
    cypher a message
    """
    message = input('enter a message: ')
    offset = int(input('enter an offset: '))
    print(ceasar(message, int(offset)))


if __name__ == '__main__':
    main()
