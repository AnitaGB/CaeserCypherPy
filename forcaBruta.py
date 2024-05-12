from cifraDeCesar import alfabeto, descriptografar_mensagem


def ataque_forca_bruta(mensagem_cifrada):
    for chave in range(len(alfabeto)):
        mensagem_descriptografada = descriptografar_mensagem(mensagem_cifrada, chave)
        print(f"Tentativa com chave {chave}: {mensagem_descriptografada}")