# Algoritmo de criptografia com Cifra de César
from cifraDeCesar import criptografar_mensagem, descriptografar_mensagem
from forcaBruta import ataque_forca_bruta

if __name__ == '__main__':
    chave = 22

    mensagem = "Mande mantimentos."
    mensagem_crip = criptografar_mensagem(mensagem, chave)

    print("CIFRANDO MENSAGEM\n")

    print("Mensagem original:", mensagem)
    print("Chave:", chave)
    print("Mensagem cifrada:", mensagem_crip)

    print("\nDECIFRANDO MENSAGEM\n")

    mensagem_descrip = descriptografar_mensagem(mensagem_crip, chave)

    print("Mensagem cifrada:", mensagem_crip)
    print("Chave:", chave)
    print("Mensagem decifrada:", mensagem_descrip)

    print("\nATAQUE COM FORÇA BRUTA\n")

    print("Mensagem cifrada:", mensagem_crip)
    ataque_forca_bruta(mensagem_crip)



