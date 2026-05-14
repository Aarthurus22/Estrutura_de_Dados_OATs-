"""
INSTITUIÇÃO: UNEX (Sistemas de Informação)
DISCIPLINA: Estrutura de Dados
ALUNO: Arthur de Aquino Costa
"""

from Tree import Tree

def main():
    tree = Tree()

    # Inserindo os mesmos valores. O algoritmo AVL vai organizá-los 
    # e mantê-los balanceados durante o processo.
    valores = [50, 30, 70, 20, 40, 60, 80]
    
    for valor in valores:
        tree.inserir(valor)

    print("Travessia Pós-Ordem (Esquerda -> Direita -> Raiz):")
    tree.travessia_post_order()

    print("\nTravessia Em Ordem (mostrando a altura h de cada nó):")
    tree.travessia_in_order()

if __name__ == "__main__":
    main()