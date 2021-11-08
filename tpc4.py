#!/usr/bin/env python
# coding: utf-8

# # TPC3

# ## Frações

# * __Data início__: 2021-11-03
# * __Data fim__:2012-11-05
# * __Supervisor__: José Carlos Ramalho, https://www.di.uminho.pt/~jcr/index.html
# * __Autor__: Alexandra Cordeiro, A94524
# * __Resumo__:O código realizado tem como objetivo criar frações e fazer várias opereções com estas.

# In[207]:


def menu():
     print("""Frações e listas de frações:
          
          (1)Criar fração;
          (2)Simplificar fração;
          (3)Somar frações;
          (4)Subtrair frações;
          (5)dividir frações;
          (6)Multiplicar frações;
          (7)Criar lista de frações aleatória;
          (8)Cirar lista de frações maualmente;
          (9)Simplificar frações de uma dada lista;
          (10)Somar frações de uma lista;
          (11)Subtrair frações de uma lista;
          (12)Encontrar a maior fração numa lista;
          (13)Encontrar a menor fração numa lista;
          ...
          (0)Sair.""")


# In[ ]:


num = int(input("Qual é o numerador?"))
den = int(input("Qual é o denominador?"))
def criarfracao():
    
    return (num , den)


# In[ ]:


def verFracao(f):
    print(str(num)+"/"+str(den))
    
verFracao(f)


# In[ ]:


def mdc(a,b):
    resto = None
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto

    return a
    
def simplificarFracao(f):
    num, den = f
    a=mdc(num, den) 
    return (num/a, den/a)


# In[ ]:


#o resultado é a fração simplicada de f1+f2
n1=int(input("n1:"))
d1=int(input("d1:"))
n2=int(input("n2:"))
d2=int(input("d2:"))
def somaFrac(f1,f2):
    n1, d1 = f1
    n2, d2 = f2
    return simplificarFracao((n1*d2+n2*d1 ,d1*d2))

somaFrac((n1,d1), (n2,d2))


# In[ ]:


n1=int(input("n1:"))
d1=int(input("d1:"))
n2=int(input("n2:"))
d2=int(input("d2:"))
def subtrairFrac(f1,f2):
    n1, d1 = f1
    n2, d2 = f2
    return simplificarFracao((n1*d2-n2*d1 ,d1*d2))

subtrairFrac((n1,d1),(n2,d2))


# In[ ]:


listaFrac = []
res = (0,1)
i=0
while i!=0:
    input("n1:")
    input("n2:")
    for elem in listaFrac:
        res = somaFrac(res, elem)
verFracao(res)


# In[ ]:


n1=int(input("n1:"))
d1=int(input("d1:"))
n2=int(input("n2:"))
d2=int(input("d2:"))
def multiFrac(f1,f2):
    n1, d1 = f1
    n2, d2 = f2
    return simplificarFracao((n1*n2 ,d1*d2))

multiFrac((n1,d1),(n2,d2))


# In[ ]:


n1=int(input("n1:"))
d1=int(input("d1:"))
n2=int(input("n2:"))
d2=int(input("d2:"))
def divFrac(f1,f2):
    n1, d1 = f1
    n2, d2 = f2
    return simplificarFracao((n1*d2 ,d1*n2))

divFrac((2,3),(2,7))


# In[ ]:


def criarListaA():
    lista=[]
    from random import randint
    n=int(input("Quantas frações terá a lista?"))
    for i in range(n):
        num=randint(0, 100)
        den=randint(1,100)
        lista.append((num,den))
    return lista
 
def criarListaM():
    i=0
    lista=[]
    n=int(input("Quantas frações terá a lista?"))
    for i in range(n):
        num=int(input("Introduza o numerador: "))
        den=int(input("Introduza o denominador: "))
        lista.append((num,den))
    return lista


# In[ ]:


def simplificarLista(lis):
    lis2=[]
    for f in lis:
        num , den=f
        a=mdc(num,den)
        lis2.append((num/a,den/a))
    return lis2


# In[ ]:


def somarLista(lis):
    s=(0,1)
    for f in lis:
        s=somaFrações(s, f)
    return simplificarFração(s)    

def subtrairLista(lis):
    s=(0,1)
    f=0
    while f<len(lis):
        s=s+ subtrairFrações(lis[f],lis[f+1])
        f= f+2
    return s


# In[ ]:


def maiorFração(lis):
    La=tuple(lis)
    for i in range(len(lis)):
        num, den= lis[i]
        a=num/den
        lis.insert(i,a)
        lis.remove(lis[i+1])
   
    maior=lis[0]
    for f in lis:
        if maior<f:
            maior=f
        else:
            maior=maior 
    return La[lis.index(maior)]


def menorFração(lis):
    La=tuple(lis)
    for i in range(len(lis)):
        num, den= lis[i]
        a=num/den
        lis.insert(i,a)
        lis.remove(lis[i+1])
   
    menor=lis[0]
    for f in lis:
        if menor<f:
            menor=f
        else:
            menor=menor 
    return La[lis.index(menor)]


# In[ ]:


a=-1
while a!= "0":
    menu()
    a=input("Qual a sua opção?")
    if a=="1":
        f=criarfracao()
        verFracao(f)
    elif a=="2":
        f=simplificarFracao(f)
        verFracao(f)
    elif a=="3":
        ff=criarfracao()
        fff=criarfracao()
        f=somaFrac(ff, fff)
        verFracao(f)
    elif a=="4":
        f1=criarfracao()
        f2=criarfracao()
        f=subtrairFrac(f1, f2)
        verFracao(f)
    elif a=="5":
        f1=criarfracao()
        f2=criarfracao()
        f=divFrac(f1, f2)
        verFracao(f)
    elif a=="6":
        f1=criarfracao()
        f2=criarfracao()
        f=multiFrac(f1, f2)
        verFracao(f)
    elif  a== "7":
        lista=criarListaA()
        print(lista)            
    elif a=="8":
        lista=criarListaM()
        print(lista)               
    elif a == "9":
        listas=simplificarLista(lista)
        print(listas)            
    elif a == "10":
        soma=somarLista(lista)
        verFracao(soma)            
    elif a== "11":
        sub=subtrairLista(lista)
        verFracao(sub)       
    elif a== "12":
        M=maiorfracao(lista)
        verFracao(M)
    elif a== "13":
        Mm=menorfracao(lista)
        verFracao(Mm)
    elif a== "0":
        print("A sair...")
    else:
        print("Opção inválida!")


# In[ ]:





# In[ ]:




