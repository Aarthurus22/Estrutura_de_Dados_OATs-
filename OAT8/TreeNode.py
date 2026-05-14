class TreeNode:
    def __init__(self, dado):
        self.dado = dado
        self.filho_esquerdo = None
        self.filho_direito = None
        # Requisito 1: Controle de altura (novo nó começa com altura 1)
        self.altura = 1

    # Funções auxiliares para AVL
    def get_altura_no(self, no):
        if not no:
            return 0
        return no.altura

    def get_balanceamento(self):
        # Requisito 2: Fator de balanceamento (esquerda - direita)
        return self.get_altura_no(self.filho_esquerdo) - self.get_altura_no(self.filho_direito)

    # Requisito 3: Rotações obrigatórias
    def rotacao_direita(self):
        novo_pai = self.filho_esquerdo
        subarvore = novo_pai.filho_direito

        # Realiza a rotação
        novo_pai.filho_direito = self
        self.filho_esquerdo = subarvore

        # Atualiza as alturas
        self.altura = 1 + max(self.get_altura_no(self.filho_esquerdo), self.get_altura_no(self.filho_direito))
        novo_pai.altura = 1 + max(self.get_altura_no(novo_pai.filho_esquerdo), self.get_altura_no(novo_pai.filho_direito))

        return novo_pai

    def rotacao_esquerda(self):
        novo_pai = self.filho_direito
        subarvore = novo_pai.filho_esquerdo

        # Realiza a rotação
        novo_pai.filho_esquerdo = self
        self.filho_direito = subarvore

        # Atualiza as alturas
        self.altura = 1 + max(self.get_altura_no(self.filho_esquerdo), self.get_altura_no(self.filho_direito))
        novo_pai.altura = 1 + max(self.get_altura_no(novo_pai.filho_esquerdo), self.get_altura_no(novo_pai.filho_direito))

        return novo_pai

    def inserir(self, valor):
        # Requisito 4: Inserção balanceada (como na BST)
        if valor == self.dado:
            return self

        if valor < self.dado:
            if self.filho_esquerdo is None:
                self.filho_esquerdo = TreeNode(valor)
            else:
                self.filho_esquerdo = self.filho_esquerdo.inserir(valor)
        else:
            if self.filho_direito is None:
                self.filho_direito = TreeNode(valor)
            else:
                self.filho_direito = self.filho_direito.inserir(valor)

        # Atualiza a altura do nó atual após a inserção
        self.altura = 1 + max(self.get_altura_no(self.filho_esquerdo), self.get_altura_no(self.filho_direito))

        # Verifica o balanceamento deste nó
        balanceamento = self.get_balanceamento()

        # Aplica as rotações se necessário (Requisito 3 e 4)
        
        # Caso Esquerda-Esquerda
        if balanceamento > 1 and valor < self.filho_esquerdo.dado:
            return self.rotacao_direita()

        # Caso Direita-Direita
        if balanceamento < -1 and valor > self.filho_direito.dado:
            return self.rotacao_esquerda()

        # Caso Esquerda-Direita
        if balanceamento > 1 and valor > self.filho_esquerdo.dado:
            self.filho_esquerdo = self.filho_esquerdo.rotacao_esquerda()
            return self.rotacao_direita()

        # Caso Direita-Esquerda
        if balanceamento < -1 and valor < self.filho_direito.dado:
            self.filho_direito = self.filho_direito.rotacao_direita()
            return self.rotacao_esquerda()

        return self

    def travessia_in_order(self):
        if self.filho_esquerdo is not None:
            self.filho_esquerdo.travessia_in_order()

        # Adicionado a impressão da altura para validar o funcionamento da AVL
        print(f"{self.dado}(h={self.altura}), ", end="")

        if self.filho_direito is not None:
            self.filho_direito.travessia_in_order()

    def travessia_post_order(self):
        if self.filho_esquerdo is not None:
            self.filho_esquerdo.travessia_post_order()

        if self.filho_direito is not None:
            self.filho_direito.travessia_post_order()
            
        print(f"{self.dado}, ", end="")

    # Mantendo todos os seus getters e setters
    def get_dado(self):
        return self.dado

    def set_dado(self, dado):
        self.dado = dado

    def get_filho_esquerdo(self):
        return self.filho_esquerdo

    def set_filho_esquerdo(self, filho_esquerdo):
        self.filho_esquerdo = filho_esquerdo

    def get_filho_direito(self):
        return self.filho_direito

    def set_filho_direito(self, filho_direito):
        self.filho_direito = filho_direito