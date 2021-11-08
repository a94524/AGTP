#!/usr/bin/env python
# coding: utf-8

# # TPC2

# ## Adivinha o número

# * __Data início__: 2021-10-12
# * __Data fim__:2012-10-
# * __Supervisor__: José Carlos Ramalho, https://www.di.uminho.pt/~jcr/index.html
# * __Autor__: Alexandra Cordeiro, A94524
# * __Resumo__: <p> O código realizado tem como objetivo adivinhar um número de 0 a 100 em que uma pessoa pensou em apenas 7 tentativas. <p> A pessoa apenas pode dizer se o número é maior ou menor.<p> 
# 
#     Foi criado com base na estratégia de dividir sucessivamente os números por 2 e ir somando ou subtraindo números de acordo com as indicações que a pessoa dá.
# 

# In[ ]:


def adivinha():
    z=50
    print (z)
    a=input('O número em que pensaste é menor ou maior?')
    while a=='menor':
        if  a=='menor':
            print(z/2)
        b=input('O número em que pensaste é menor ou maior?')
        if a==b and a=='menor':
            print(z/2-5)
        if a!=b and a=='menor':
            print(z/2+5)
        c=input('O número em que pensaste é menor ou maior?')
        if b==c and b=='maior':
            print(z/2+15)
        if b==c and b=='menor':
            print(z/2-15)
        if b!=c and b=='maior':
            print(z/2+2)
        if b!=c and b=='menor':
            print(z/2-2)
        d=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and b=='maior':
            print(z/2+20)
        if b==c and c==d and b=='menor':
            print(z/2-20)
        if b!=c and c!=d and b=='maior':
            print(z/2+3)
        if b!=c and c!=d and b=='menor':
            print(z/2-3)
        if b!=c and c==d and b=='maior':
            print(z/2+1)
        if b!=c and c==d and b=='menor':    
            print(z/2-1)
        if b==c and c!=d and b=='maior':
            print(z/2+10)
        if b==c and c!=d and b=='menor':
            print(z/2-10)
        e=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and d==e and b=='maior':
            print(z/2+22)
        if b==c and c==d and d==e and b=='menor':
            print(z/2-22)
        if b==c and c==d and d!=e and b=='maior':
            print(z/2+18)
        if b==c and c==d and d!=e and b=='menor':
            print(z/2-18)
        if b==c and c!=d and d==e and b=='maior':
            print(z/2+8)
        if b==c and c!=d and d==e and b=='menor':
            print(z/2-8)
        if b==c and c!=d and d!=e and b=='maior':
            print(z/2+12)
        if b==c and c!=d and d!=e and b=='menor':
            print(z/2-12)
        if b!=c and c!=d and d==e and b=='menor':
            print(z/2-4) 
        if b!=c and c!=d and d==e and b=='maior':
            print(z/2+4)
        f=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and d==e and e==f and b=='maior':
            print(z/2+23)
        if b==c and c==d and d==e and e==f and b=='menor':
            print(z/2-23)
        if b==c and c==d and d==e and e!=f and b=='maior':
            print(z/2+21)
        if b==c and c==d and d!=e and e==f and b=='maior':
            print(z/2+17)
        if b==c and c==d and d!=e and e==f and b=='menor': 
            print(z/2-17)
        if b==c and c==d and d==e and e!=f and b=='menor':
            print(z/2-21)
        if b==c and c==d and d!=e and e!=f and b=='maior':
            print(z/2+19)
        if b==c and c==d and d!=e and e!=f and b=='menor': 
            print(z/2-19)
        if b==c and c!=d and d!=e and e==f and b=='maior':
            print(z/2+13)
        if b==c and c!=d and d!=e and e==f and b=='menor':
            print(z/2-13)
        if b==c and c!=d and d!=e and e!=f and b=='maior':
            print(z/2+11)
        if b==c and c!=d and d!=e and e!=f and b=='menor':
            print(z/2-11)
        if b==c and c!=d and d==e and e!=f and b=='maior':
            print(z/2+9)
        if b==c and c!=d and d!=e and e!=f and b=='maior':
            print(z/2-9)
        if b==c and c!=d and d==e and e==f and b=='maior':
            print(z/2+7)
        if b==c and c!=d and d==e and e==f and b=='menor':
            print(z/2-7)
        g=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and d==e and e==f and f==g and b=='maior':
            print(z/2+24)
        if b==c and c==d and d==e and e==f and f==g and b=='menor':
            print(z/2-24)
        if b==c and c==d and d!=e and e==f and f==g and b=='maior':
            print(z/2+16)
        if b==c and c==d and d!=e and e==f and f==g and b=='menor':
            print(z/2-16)
        if b==c and c!=d and d!=e and e==f and f==g and b=='maior':
            print(z/2+14)
        if b==c and c!=d and d!=e and e==f and f==g and b=='menor':
            print(z/2-14)
        if b==c and c!=d and d==e and e==f and f==g and b=='maior':
            print(z/2+6)
        if b==c and c!=d and d==e and e==f and f==g and b=='menor':
            print(z/2-6)
    z=50
    print(z)
    a=input('O número em que pensaste é menor ou maior?')
    while a=='maior':
        if a=='maior':
            print(z+25)
        b=input('O número em que pensaste é menor ou maior?')
        if a==b and a=='maior':
            print(z+25+5)
        if a!=b and a=='maior':
            print(z+25-5)
        c=input('O número em que pensaste é menor ou maior?')
        if b==c and b=='maior':
            print(z+25+15)
        if b==c and b=='menor':
            print(z+25-15)
        if b!=c and b=='maior':
            print(z+25+2)
        if b!=c and b=='menor':
            print(z+25-2)
        d=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and b=='maior':
            print(z+25+20)
        if b==c and c==d and b=='menor':
            print(z+25-20)
        if b!=c and c!=d and b=='maior':
            print(z+25+3)
        if b!=c and c!=d and b=='menor':
            print(z+25-3)
        if b!=c and c==d and b=='maior':
            print(z+25+1)
        if b!=c and c==d and b=='menor':    
            print(z+25-1)
        if b==c and c!=d and b=='maior':
            print(z+25+10)
        if b==c and c!=d and b=='menor':
            print(z+25-10)
        e=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and d==e and b=='maior':
            print(z+25+22)
        if b==c and c==d and d==e and b=='menor':
            print(z+25-22)
        if b==c and c==d and d!=e and b=='maior':
            print(z+25+18)
        if b==c and c==d and d!=e and b=='menor':
            print(z+25-18)
        if b==c and c!=d and d==e and b=='maior':
            print(z+25+8)
        if b==c and c!=d and d==e and b=='menor':
            print(z+25-8)
        if b==c and c!=d and d!=e and b=='maior':
            print(z+25+12)
        if b==c and c!=d and d!=e and b=='menor':
            print(z+25-12)
        if b!=c and c!=d and d==e and b=='menor':
            print(z+25-4) 
        if b!=c and c!=d and d==e and b=='maior':
            print(z+25+4)
        f=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and d==e and e==f and b=='maior':
            print(z+25+23)
        if b==c and c==d and d==e and e==f and b=='menor':
            print(z+25-23)
        if b==c and c==d and d==e and e!=f and b=='maior':
            print(z+25+21)
        if b==c and c==d and d!=e and e==f and b=='maior':
            print(z+25+17)
        if b==c and c==d and d!=e and e==f and b=='menor': 
            print(z+25-17)
        if b==c and c==d and d==e and e!=f and b=='menor':
            print(z+25-21)
        if b==c and c==d and d!=e and e!=f and b=='maior':
            print(z+25+19)
        if b==c and c==d and d!=e and e!=f and b=='menor': 
            print(z+25-19)
        if b==c and c!=d and d!=e and e==f and b=='maior':
            print(z+25+13)
        if b==c and c!=d and d!=e and e==f and b=='menor':
            print(z+25-13)
        if b==c and c!=d and d!=e and e!=f and b=='maior':
            print(z+25+11)
        if b==c and c!=d and d!=e and e!=f and b=='menor':
            print(z+25-11)
        if b==c and c!=d and d==e and e!=f and b=='maior':
            print(z+25+9)
        if b==c and c!=d and d!=e and e!=f and b=='maior':
            print(z+25-9)
        if b==c and c!=d and d==e and e==f and b=='maior':
            print(z+25+7)
        if b==c and c!=d and d==e and e==f and b=='menor':
            print(z+25-7)
        g=input('O número em que pensaste é menor ou maior?')
        if b==c and c==d and d==e and e==f and f==g and b=='maior':
            print(z+25+24)
        if b==c and c==d and d==e and e==f and f==g and b=='menor':
            print(z+25-24)
        if b==c and c==d and d!=e and e==f and f==g and b=='maior':
            print(z+25+16)
        if b==c and c==d and d!=e and e==f and f==g and b=='menor':
            print(z+25-16)
        if b==c and c!=d and d!=e and e==f and f==g and b=='maior':
            print(z+25+14)
        if b==c and c!=d and d!=e and e==f and f==g and b=='menor':
            print(z+25-14)
        if b==c and c!=d and d==e and e==f and f==g and b=='maior':
            print(z+25+6)
        if b==c and c!=d and d==e and e==f and f==g and b=='menor':
            print(z+25-6)
        
        
adivinha() 


# In[ ]:




