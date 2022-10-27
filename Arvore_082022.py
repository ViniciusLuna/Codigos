class NodoArvore:
#Arvore Binaria
    
    def __init__(self, chave=None, esquerda=None, direita=None): # contrutor 
            self.chave = chave
            self.esquerda = esquerda
            self.direita = direita

    def __repr__(self): 
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)

    
    raiz = NodoArvore(40)
    raiz.esquerda = NodoArvore(20) #folha esq
    raiz.direita = NodoArvore(60) # folha dir

    raiz.direita.esquerda = NodoArvore(50) # Ultima folha 
    raiz.direita.direita = NodoArvore(70) # Ultima folha
    raiz.esquerda.esquerda = NodoArvore(10) # Ultima folha
    raiz.esquerda.direita = NodoArvore(30) # Ultima folha

    
    def em_ordem(raiz):
        if not raiz: #solução trivial
            return
        #Visita filho da esquerda
            em_ordem(raiz.esquerda)
        #Visita nodo corrente
            em_ordem(raiz.chave)
        #Visita filho direita
            em_ordem(raiz.direita)

    
    def insere(raiz, nodo): #inserção
        #inserir um nodo em uma Arvore Binaria
        if raiz is None: # vazia
            raiz = nodo # variavel
        #nodo deve ser inserido na subArvore direita
        elif raiz.chave < nodo.chave:
            if raiz.direita is None: #vazia
                raiz.direta = nodo # variavel
        #nodo deve ser inserido na subArvore esquerda
        elif:
            if raiz.esquerda is None:
                raiz.esquerda = nodo
            else:
                insere(raiz.esquerda, nodo)
                if raiz.esquerda is None:
                    raiz.esquerda = nodo

#Cria uma arvore binaria
    raiz = NodoArvore(40)
    for chave in [20, 60, 50, 70, 10, 30]:
        nodo = NodoArvore(chave)
        insere(raiz, nodo)
#Imprime o caminhamento em ordem da Arvore
        em_ordem(raiz)

    def busca(raiz, chave):
        #Procura por uma chave em uma Arvore Binaria de pesquisa.
        #Trata o caso em que a chave procurada n esta presente
        if raiz is None: #solução trivial #empty
            return None

        #A chave procurada esta na raiz da arvore

        if raiz.chave == chave: #se for igual a ele mesmo então eh raiz
            return raiz
        
        #A chave procurada é maior q a da Raiz

        if raiz.chave < chave:
            return busca(raiz.direita, chave)

        #A chave procurada é menor que a da raiz
        return busca(raiz.esquerda, chave) #retorna busca                                   