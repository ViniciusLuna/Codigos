Class Arvore
#Cria uma arvore binaria de pesquisa
raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

#Procura por valores na arvore
for chave in [-50, 10, 30, 70, 100]
    resultado = busca(raiz, chave)
    if resultado
        print("Busca pela chave {}: Sucesso".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))