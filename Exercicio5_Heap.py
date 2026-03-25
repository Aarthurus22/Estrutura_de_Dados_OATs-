class MaxHeap:
    def __init__(self):
        self.heap = []  # lista do heap

    # Inserir elemento
    def insert(self, value):
        self.heap.append(value)  # adiciona no final
        self.heapify_up(len(self.heap) - 1)  # sobe para ajustar

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i] > self.heap[parent]:
                # troca com o pai
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    # Remover elemento pelo índice
    def delete(self, index):
        if index >= len(self.heap):
            print("Índice inválido!")
            return

        print(f"\nRemovendo: {self.heap[index]}")

        # troca com o último
        self.heap[index], self.heap[-1] = self.heap[-1], self.heap[index]

        # remove último
        self.heap.pop()

        # ajusta o heap
        self.heapify_down(index)

    # Ajustar descendo
    def heapify_down(self, i):
        size = len(self.heap)

        while True:
            maior = i
            esquerda = 2 * i + 1
            direita = 2 * i + 2

            # verifica filho esquerdo
            if esquerda < size and self.heap[esquerda] > self.heap[maior]:
                maior = esquerda

            # verifica filho direito
            if direita < size and self.heap[direita] > self.heap[maior]:
                maior = direita

            # se precisar trocar
            if maior != i:
                self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
                i = maior
            else:
                break

    # Mostrar heap
    def print_heap(self):
        print("Heap:", self.heap)



# Teste
heap = MaxHeap()

valores = [500, 320, 2222, 1230, 420, 635]

for v in valores:
    heap.insert(v)

heap.print_heap()

heap.delete(0)

heap.print_heap()