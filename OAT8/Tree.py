from TreeNode import TreeNode

class Tree:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = TreeNode(valor)
        else:
            # Atualiza a raiz principal caso haja uma rotação
            self.raiz = self.raiz.inserir(valor)

    def travessia_in_order(self):
        if self.raiz is not None:
            self.raiz.travessia_in_order()
            print()

    def travessia_post_order(self):
        if self.raiz is not None:
            self.raiz.travessia_post_order()
            print()