import os

# Caminho para a área de trabalho
caminho_area_trabalho = os.path.join(os.path.expanduser('~'), 'Desktop')

# Nome da pasta que você deseja criar
nome_pasta = 'MinhaPasta'

# Caminho completo para a nova pasta
caminho_nova_pasta = os.path.join(caminho_area_trabalho, nome_pasta)

# Criação da pasta
os.makedirs(caminho_nova_pasta, exist_ok=True)
pasta = os.path.join(caminho_nova_pasta)
for i in range(20):
    # Nome da pasta que você deseja criar
    nome_subpasta = f'subpasta-{i}'
    caminho_nova_subpasta = os.path.join(caminho_nova_pasta, nome_subpasta)
    os.makedirs(caminho_nova_subpasta, exist_ok=True)
    for j in range(20):
        nome_subpasta_sub01 = f'subpasta-subpasta-{i}'
        caminho_nova_subpasta_sub = os.path.join(caminho_nova_subpasta, nome_subpasta_sub01)
        os.makedirs(caminho_nova_subpasta_sub, exist_ok=True)
        for g in range(20):
            nome_subpasta_sub02 = f'subpasta-subpasta-sub02-{i}'
            caminho_nova_subpasta_sub02 = os.path.join(caminho_nova_subpasta_sub, nome_subpasta_sub02)
            os.makedirs(caminho_nova_subpasta_sub02, exist_ok=True)
            for h in range(20):
                nome_subpasta_sub03 = f'subpasta-subpasta-sub03-{i}'
                caminho_nova_subpasta_sub03 = os.path.join(caminho_nova_subpasta_sub02, nome_subpasta_sub03)
                os.makedirs(caminho_nova_subpasta_sub03, exist_ok=True)
                # Caminho completo para o novo arquivo de texto
                caminho_arquivo_txt = os.path.join(caminho_nova_subpasta_sub03, f'meuarquivo-{i}.txt')
                # Criação do arquivo de texto e escrita de algo nele
                with open(caminho_arquivo_txt, 'w') as arquivo:
                    arquivo.write("Olá, este é um arquivo de texto criado com Python!")

print(f"Pasta '{nome_pasta}' criada na área de trabalho.")
