import re

def buscar_sequencias(arquivo, sequencias):
    sequencias_encontradas = []

    with open(arquivo, 'r') as f:
        conteudo = f.read()
        for sequencia in sequencias:
            matches = re.finditer(sequencia, conteudo)
            for match in matches:
                conteudo_encontrado = match.group()
                sequencias_encontradas.append(conteudo_encontrado)
                print(f'Sequência "{sequencia}" encontrada: {conteudo_encontrado}')

    with open('chaves.txt', 'w') as file:
        for linha in sequencias_encontradas:
            file.write(linha + '\n')  # Adiciona uma quebra de linha entre as sequências

# Substitua 'caminho/do/arquivo.txt' pelo caminho real do seu arquivo
caminho_do_arquivo = input('Por digite o nome do arquivo txt que deseja extrair as notas : ')
sequencias_procuradas = [r'\d{44}']  # Exemplos de sequências

buscar_sequencias(caminho_do_arquivo, sequencias_procuradas)
