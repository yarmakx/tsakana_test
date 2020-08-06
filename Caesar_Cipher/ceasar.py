def decipher(ciphertext, key):
    """
    Dado un mensaje cifrado y un desplazamiento, la funcion
    devuelva el mensaje original

    Input:
        ciphertext (str): mensaje cifrado
        key (int): desplazamiento

    Returns:
        plaintext (str): mensaje original

    >>> decipher('YDORV D ÑD SÑDBD', 3)
    'VAMOS A LA PLAYA'
    >>> decipher('ABC', -1)
    'BCD'
    """
    # 2 helper mappings, from letters to ints and the inverse
    l2i = dict(zip("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", range(27)))
    i2l = dict(zip(range(27), "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))

    plaintext = ""
    for c in ciphertext.upper():
        if c.isalpha():
            plaintext += i2l[(l2i[c] - key) % 27]
        else:
            plaintext += c

    return plaintext
