alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def decifrar(cifrado, chave):

    m = ''
    for c in cifrado:
        if c in alfabeto:
            indice = alfabeto.index(c)
            m += alfabeto[(indice - chave) % len(alfabeto)]
        else:
            m += c
    return m


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(decifrar("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq "
                   "glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu "
                   "ynnjw ml rfc spj", -2))
    print("***")
    print(decifrar("def", -2))
    print(decifrar("map", -2))
