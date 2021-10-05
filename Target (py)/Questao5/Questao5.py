string = input("Escreva uma palavra: ")

def inverterString(string):
    string_final = ''
    caracteres = len(string)
    while caracteres:
        caracteres -= 1
        string_final += string[caracteres]
    return print(string_final)


if __name__ == '__main__':
    inverterString(string)
