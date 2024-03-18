import os
import shutil
import time


def criar_pasta(destino):
    os.makedirs(destino, exist_ok=True)


def copia_arquivo_para_local(nome_arquivo_atual, novo_local):
    shutil.copy(nome_arquivo_atual, novo_local)


def obter_nome_primeira_pasta(caminho_pasta_raiz, caminho_pasta_atual):
    relativo = os.path.relpath(caminho_pasta_atual, caminho_pasta_raiz)
    pastas = relativo.split(os.path.sep)

    # Remove qualquer pasta vazia resultante
    pastas = [pasta for pasta in pastas if pasta]

    if pastas:
        return pastas[0]
    else:
        return None


def renomear_ultimo_arquivo_recursivo(caminho_pasta, caminho_pasta_raiz, _):
    # Lista os arquivos e subdiretórios no diretório
    conteudo_pasta = os.listdir(caminho_pasta)

    # Filtra apenas os arquivos, excluindo diretórios
    arquivos = [
        arquivo
        for arquivo in conteudo_pasta
        if os.path.isfile(os.path.join(caminho_pasta, arquivo))
    ]

    if arquivos:
        # Obtém o último arquivo na lista
        ultimo_arquivo = arquivos[-1]

        # Obtém o caminho completo do último arquivo
        caminho_ultimo_arquivo = os.path.join(caminho_pasta, ultimo_arquivo)

        # Obtém o nome da primeira pasta imediatamente após a pasta raiz
        nome_primeira_pasta = obter_nome_primeira_pasta(
            caminho_pasta_raiz, caminho_pasta
        )

        if nome_primeira_pasta:
            # Constrói o novo nome do arquivo usando o nome da primeira pasta
            novo_nome_arquivo = os.path.join(caminho_pasta, nome_primeira_pasta)

            # Renomeia o último arquivo com o nome da primeira pasta
            os.rename(caminho_ultimo_arquivo, novo_nome_arquivo)

            print(
                f"O último arquivo em '{caminho_pasta}' foi renomeado para '{nome_primeira_pasta}'."
            )

            # Cria a pasta 'renameds' no caminho raiz
            caminho_destino_raiz = os.path.join(
                os.path.dirname(caminho_pasta_raiz), "renameds"
            )
            criar_pasta(caminho_destino_raiz)

            # Move o arquivo renomeado para a pasta 'renameds' no caminho raiz
            caminho_destino_final = os.path.join(
                caminho_destino_raiz, nome_primeira_pasta
            )
            copia_arquivo_para_local(novo_nome_arquivo, caminho_destino_final)

    # Recursivamente chama a função para cada subdiretório
    subdiretorios = [
        d for d in conteudo_pasta if os.path.isdir(os.path.join(caminho_pasta, d))
    ]
    for subdiretorio in subdiretorios:
        renomear_ultimo_arquivo_recursivo(
            os.path.join(caminho_pasta, subdiretorio), caminho_pasta_raiz, None
        )


def main():
    print("--- RENOMEAR E MOVER ARQUIVOS ---")

    while True:
        try:
            caminho_for_rename = input("Digite o caminho da pasta:\n")
            renomear_ultimo_arquivo_recursivo(
                caminho_for_rename, caminho_for_rename, None
            )
            print("\n")
            print("\n")
            print("Todos os arquivos foram movidos e renomeados!")
            time.sleep(3)

            continue_while = input("Continuar? [y/N] \n")
            if continue_while is None:
                continue_while = 'N'

            if continue_while == "y" or continue_while == "Y":
                main()
            break
        except FileNotFoundError:
            print("O caminho especificado não foi encontrado. Tente novamente.")


if __name__ == "__main__":
    main()
