def palindromo(sentence):
    """ Permite conocer si un string es palindromo
    
    Ejemplo:
    >>> palindromo('oso')
    True

    >>> palindromo('reconocer')
    True

    >>> palindromo('hola')
    False
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]