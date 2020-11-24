import numpy as np

grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 0, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 0],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 7, 0]]


def possivel(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def soluciona():
    global grid
    for y in range(9):
        for x in range(9):
            # Procura quadradinhos vazios
            if grid[y][x] == 0:
                for n in range(1, 10):
                    # Se for possivel colocar algum valor no quadradinho vazio
                    if possivel(y, x, n):
                        # Preenche com o valor
                        grid[y][x] = n
                        # Aqui nós reduzimos o problema, então é uma boa chamada para recursao
                        soluciona()
                        # Se ele nao consegui completar a solucao, é porque foi uma escolha ruim
                        # Entao a gente remove o valor, da um passo pra tras (backtracking)
                        grid[y][x] = 0
                # Se ele tentou todos os valores possiveis para um vazio
                # e não deu certo, então ele retorna sem solucão
                return
    for linha in grid:
        print(linha)
    input("Mais solucao? ")

soluciona()