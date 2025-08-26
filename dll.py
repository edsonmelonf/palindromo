"""
Opção 2: Verificador de Palíndromos
● Conceito: Criar um programa que determina se uma palavra ou frase é
um palíndromo (lê-se da mesma forma nos dois sentidos) utilizando a
eficiência de uma DLL.
● Requisitos Mínimos:

1. Implementar uma DLL onde cada nó armazena um único caractere.

2. Criar uma função que carrega uma string para dentro da DLL.

3. Implementar a função eh_palindromo(), que deve percorrer a
lista a partir das duas extremidades (head e tail)
simultaneamente, comparando os caracteres até o centro da lista
para determinar o resultado.

4. Escrever um pequeno relatório (no próprio código ou em um
arquivo anexo) explicando por que a complexidade desta solução é
O(n) e por que uma abordagem similar com uma lista
simplesmente encadeada seria O(n2).

"""
import unicodedata
import string

class Node:
    def __init__(self, char):
        self.char = char
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 2. Criar uma função que carrega uma string para dentro da DLL
    def insert_at_dll(self, caracteres):
        caracteres = str(caracteres.upper())
        caracteres = unicodedata.normalize("NFD", caracteres)
        caracteres = ''.join(c for c in caracteres if unicodedata.category(c) != 'Mn')
        caracteres = ''.join(c for c in caracteres if c not in string.punctuation)
        caracteres = caracteres.replace(' ', '')

        for c in caracteres:
            new_node = Node(c)

            if self.head is None:  
                self.head = new_node
                self.tail = new_node
            else:  
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node


    def eh_palindromo(self):
        left = self.head
        right = self.tail

        while left and right and left != right and left.prev != right:
            if left.char != right.char:
                return False
            left = left.next
            right = right.prev

        return True

    def print_dll(self):
        current = self.head
        while current:
            print(current.char, end=" - ")
            current = current.next

# ----------------------------------------------------------------------------------------------------------------------------------------
"""
- "Socorram-me, subi no ônibus em Marrocos."
- "Anotaram a data da maratona."
"""

dll = DoublyLinkedList()

dll.insert_at_dll("Anotaram a data da maratona.")

dll.print_dll()

if dll.eh_palindromo() is True:
    print("É palíndromo ", end=" ")
else:
    print("Não é um palindromo")



