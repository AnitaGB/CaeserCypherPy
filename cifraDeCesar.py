# Alfabeto latino
import unicodedata

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']


def gerar_alfabeto_cifrado(chave):
    novo_alfabeto = {}

    for letra in alfabeto:

        # Recupera o índice da letra
        indice = alfabeto.index(letra)
        # Limita que o novo indice esteja nos limites de tamanho do alfabeto
        novo_indice = (indice + chave) % len(alfabeto)
        nova_letra = alfabeto[novo_indice]
        novo_alfabeto[letra] = nova_letra

    return novo_alfabeto


def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')


def criptografar_mensagem(mensagem, chave):
    mensagem = remover_acentos(mensagem)
    alfabeto_dict = gerar_alfabeto_cifrado(chave)
    nova_mensagem = []

    for caractere in mensagem:

        if caractere.lower() in alfabeto:
            # Se a letra existir no alfabeto
            novo_caractere = alfabeto_dict[caractere.lower()]
            # Preserva o tipo da letra, ou seja, se a letra for maiúscula, continua sendo maiúscula.
            nova_mensagem.append(novo_caractere.upper() if caractere.isupper() else novo_caractere)

        else:
            # Se houver caractere que não pôde ser cifrado (caracteres especiais ou acentuados)
            nova_mensagem.append(caractere)

    # retorna um array transformado em uma sequência de caracteres
    return ''.join(nova_mensagem)


def descriptografar_mensagem(mensagem, chave):
    return criptografar_mensagem(mensagem, chave * -1)