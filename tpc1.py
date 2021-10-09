#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('21 FÓSFOROS'
      '\n'
     'Podes retirar 1,2,3 ou 4 fósforos'
      '\n'
     'Vence quem ficar com 0 fósforos na sua jogada')


def pcsegundo():
            a=21
            c=0
            while a>1:
                b=int(input('Que números queres jogar?'))
                a=a-b
                print('\nRestam', a, 'fósforos')
                c=5-b
                a=a-c
                print('\n Tirei', c, 'fósforos')
                if a == 1:
                    print('O segundo jogador ganhou')
                    e=int(input('Queres jogar outra vez? Se sim escreve 1 se não escreve 2'))
                    if e==1:
                        return jogar(pcsegundo,pcprimeiro)
                    else:
                        print('Adeus')
def pcprimeiro():
            a=21
            d=0
            import random
            d=random.randrange(1, 4)
            print('Tirei', d, 'fósforos')
            a=a-d
            b=int(input('Que número queres jogar?'))
            a=a-b
            print ('Restam', a, 'fosforos')
            
            while a>10:
                    d=random.randrange(1, 4)
                    a=a-d
                    print ('tirei', d, 'fósforos')
                    b=int(input('Que número queres jogar?'))
                    a=a-b
                    print ('Restam', a, 'fosforos')
                   
                   
            while a<=10:
                    b=int(input('Que número queres jogar?'))
                    a=a-b
                    print ('Restam', a, 'fosforos')
                    a=a-d
                    if a==10:
                        d=4
                        print('tirei 4 fósforos')
                        print('restam', a)
                    elif a==9:
                        d=3
                        print('tirei 3 fósforos')
                    elif a==8:
                        d=2
                        print('tirei 2 fósforos')
                    elif a==7:
                        d=1
                        print('tirei 1 fósforo')
                    elif a<=6:
                        print('O primeiro jogador ganhou')
                        e=int(input('Queres jogar outra vez? Se sim escreve 1 se não escreve 2'))
                        if e==1:
                            return jogar(pcsegundo,pcprimeiro)
                        else:
                            print('Adeus')    
                            
                    
                    
def jogar (pcsegundo,pcprimeiro):
        j=int(input('\nQueres ser o primeiro ou o segundo?'))
        if j == 1:
            print('Tu és o primeiro e eu o segundo')
            jogar=pcsegundo()
        elif j==2:
             print('Eu sou o primeiro e tu o segundo')
             jogar=pcprimeiro()
                        
jogar(pcsegundo,pcprimeiro)    


# In[ ]:




