import random

def newpop(Nnd, cromlim):
    """
    Gera população inicial aleatória
    
    Parâmetros:
    Nnd: número de indivíduos
    cromlim: matriz [Ncrom x 2] com limites dos cromossomos
    """
    
    Ncrom = len(cromlim)  # tamanho da matriz de limites
    
    # Inicializa população
    populacao = []
    
    # Para cada indivíduo
    for j in range(Nnd):
        individuo = []
        
        # Para cada cromossomo
        for i in range(Ncrom):
            inf = cromlim[i][0]  # limite inferior
            sup = cromlim[i][1]  # limite superior
            
            # Gera valor aleatório
            valor = random.uniform(inf, sup)
            individuo.append(valor)
        
        populacao.append(individuo)
    
    return populacao


# Exemplo de uso
cromlim = [
    [0, 10],    # cromossomo 1: entre 0 e 10
    [-5, 5],    # cromossomo 2: entre -5 e 5
    [1, 100]    # cromossomo 3: entre 1 e 100
]

Nnd = 5  # 5 indivíduos

populacao = newpop(Nnd, cromlim)

# Exibir resultado
for i, ind in enumerate(populacao):
    print(f"Indivíduo {i+1}: {[round(v, 2) for v in ind]}")
