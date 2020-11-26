from constraint import *

LINHAS = 'abcdefghi'
COLUNAS = '123456789'
DIGITOS = range(1, 10)
VARIAVEIS = [linha + coluna for linha in LINHAS for coluna in COLUNAS]
GRUPOS_DE_LINHAS = [[linha + coluna for coluna in COLUNAS] for linha in LINHAS]
GRUPOS_DE_COLUNAS = [[linha + coluna for linha in LINHAS] for coluna in COLUNAS]
GRUPO_DE_QUADRADOS = [
    [LINHAS[3 * grupo_linha + k] + COLUNAS[3 * grupo_coluna + j]
     for j in range(3) for k in range(3)]
    for grupo_coluna in range(3) for grupo_linha in range(3)
]

def soluciona(dicas):
    problema = Problem()
    for variavel, dica in zip(VARIAVEIS, dicas):
        # Adiciona variavel com a unica possibilidade da dica, se existir,
        # Caso a dica não exista, adiciona a variável com dígitos possíveis
        problema.addVariables([variavel], [dica] if dica in DIGITOS else DIGITOS)

    for grupos_de_variaveis in [GRUPOS_DE_LINHAS, GRUPOS_DE_COLUNAS, GRUPO_DE_QUADRADOS]:
        for grupo_de_variavel in grupos_de_variaveis:
            # Para cada grupo de variável (linhas, colunas e quadrados), adiciona a constraint
            # de todos differentes (allDifferent)
            problema.addConstraint(AllDifferentConstraint(), grupo_de_variavel)
    return problema.getSolution()


def formata_grid(variavel_para_valor):
    print(variavel_para_valor)
    tabela = ''
    for linhanum, linha in enumerate('abcdefghi'):
        for colunanum, coluna in enumerate('123456789'):
            tabela += str(variavel_para_valor[linha+coluna])
            if colunanum % 3 == 2:
                tabela += ' '
        tabela += '\n'
        if linhanum % 3 == 2:
            tabela += '\n'
    return tabela

dicas = (
    0, 0, 8,  0, 0, 6,  0, 0, 0,
    0, 0, 4,  3, 7, 9,  8, 0, 0,
    5, 7, 0,  0, 1, 0,  3, 2, 0,

    0, 5, 2,  0, 0, 7,  0, 0, 0,
    0, 6, 0,  5, 9, 8,  0, 4, 0,
    0, 0, 0,  4, 0, 0,  5, 7, 0,

    0, 2, 1,  0, 4, 0,  0, 9, 8,
    0, 0, 9,  6, 2, 3,  1, 0, 0,
    0, 0, 0,  9, 0, 0,  7, 0, 0,
)

print(formata_grid(soluciona(dicas)))