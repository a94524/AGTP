#!/usr/bin/env python
# coding: utf-8

# # TPC3

# ## Bubble Sort

# * __Data início__: 2021-10-23
# * __Data fim__:2012-10-24
# * __Supervisor__: José Carlos Ramalho, https://www.di.uminho.pt/~jcr/index.html
# * __Autor__: Alexandra Cordeiro, A94524
# * __Resumo__:O código realizado tem como objetivo ler aleatoriamente dois números de uma lista escrita pelo utilizador ou aleatória até percorrer a lista inteira e todos os números dessa lista estarem por ordem crescente.
#     

# In[24]:


def menu():
    print("""Gestão de lista de inteiros
(1) Introduza a lista à mão";
(2) Gerar lista com valores aleatórios;
(3) Maior elemento da lista;
(4) Ordenar a lista
(0) Sair""")


# In[25]:


def criarListaM():
    n=int(input('Introduza o nº de elementos da lista: '))
    lista=[]
    for i in range(n):
        numero=int(input('Introduza o elemento ' + str(i+1) + ': '))
        lista.append(numero)
    return lista


# In[26]:


def criarListaA():
    from random import randint
    n=int(input('Introduza o nº de elementos da lista: '))
    lista=[]
    for i in range(n):
        numero=randint(0,100)     
        lista.append(numero)
    return lista


# In[27]:


def maiorElemento(list):
    i=0
    maior=list[0]
    while i<(len(list)-1):
        if list[i]<list[i+1] and list[i+1]>maior:
            maior=list[i+1]
            i=i+1
        else:
            i=i+1
    return maior


# In[36]:


def bubbleSort(list):
    i=1
    trocar=1
    while i < len(list) and trocar<=1:
        if list[i-1]>list[i]:
            x=list[i-1]
            y=list[i]
            list[i-1]=y
            list[i]=x
            trocar=trocar-1
        else:
            i=i+1
    if trocar<1:
        return bubbleSort(list)
    return(list)
    


# In[ ]:


op="1"
menu()
while op != '0':
    op=input('Qual é a sua opção? ')
    if op=="1":
        list=criarListaM()
        print(list)
    elif op=="2":
        list=criarListaA()
        print(list)
    elif op=="3":
        m=maiorElemento(list)
        print(m)
    elif op=="4":
        list=bubbleSort(list)
        print(list)
    elif op=="0":
        print('Até a próxima!')
    else:
        print('Opção inválida')


# In[ ]:





# In[ ]:




