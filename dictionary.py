def main():
    # dictionnary
    dictio = {
        "nom": "sadey",
        "name": "jesusa",
        "address": {
            "rue": "lebon",
            "cp": 78500
        },
        "hobby": ["cinema", "voyage"]
    }
    print(dictio["address"]["rue"])


if __name__ == '__main__':
    main()
