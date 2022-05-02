# -*- coding: utf-8 -*-


import math

class Figura:
    
    def __init__(self,tipo,comprimento,largura,px=-1,py=-1):
        self.tipo=tipo
        self.l=largura
        self.c=comprimento
        self.posx=px
        self.posy=py
        
        
    def area(self):
        if self.tipo=="circulo":
            self.c=self.l
            A=(((self.l)*2)**2)*math.pi
            return A
        
        if self.tipo=="retangulo":
            A=self.c*self.l
            return A
        
    
class Superficie:
    
    def __init__(self,comprimento,largura):
        self.c=comprimento
        self.l=largura
        self.lista=[]
        self.area=comprimento*largura
        self.matriz=[]
        
        for linha in range(self.c):
            linha=[]
            for j in range(self.l):
                linha.append(0)
            self.matriz.append(linha) 
            
            
    def adicionar(self,figura,px,py):
        
        if self.sobreposição(figura.c,figura.l,px,py)==True:
            
            if figura.l>(self.l-px) or figura.c>(self.c-py) or figura.area()>self.area:
                return False
            else:
                figura.posx=px
                figura.posy=py
                self.matriz_met(figura.c,figura.l,px,py,1)
                self.lista.append(figura)
                self.area-=figura.area()
                return True
            
        else:
            return False
    
    
    def mover(self,figura,px,py):
        
        self.matriz_met(figura.c,figura.l,figura.posx,figura.posy,0)
        self.area+=figura.area()
        
        if self.adicionar(figura,px,py)==True:
            self.adicionar(figura,px,py)
        
        else:
            self.adicionar(figura,figura.posx,figura.posy)
            return False
        
        
    def matriz_met(self,comprimento,largura,px,py,x):
        
        for linha in range(len(self.matriz)):
            for coluna in range(len(self.matriz[0])):
                if linha<(py+largura) and linha>=py:
                    if coluna<(px+comprimento) and coluna>=px:
                        self.matriz[linha][coluna]=x
                        
        
    def sobreposição(self,comprimento,largura,px,py):
        x=0
        
        for linha in range(len(self.matriz)):
            for coluna in range(len(self.matriz[0])):
                if linha<(py+largura) and linha>=py:
                    if coluna<(px+comprimento) and coluna>=px:
                        if self.matriz[linha][coluna]==1:
                            x+=1
                            
        if x!=0:
            return False
        
        else:
            return True
        
    
    def colocar_automaticamente(self,figura):
        px=0
        py=0
        
        while px<=self.c and py<=self.l:
            
            if self.adicionar(figura,px,py)==False:
                if px!=self.c:
                    px+=1
                elif px==self.c:
                    py+=1
                    px=0
                    
            else:
                figura.posx=px
                figura.posy=py
                return True
                
                break
            
    def rodar(self,figura):
        
        self.matriz_met(figura.c,figura.l,figura.posx,figura.posy,0)
        if self.sobreposição(figura.l,figura.c,figura.posx,figura.posy)==True:
            
        
            if figura.c>self.l or figura.l>self.c or figura.area()>self.area:
                return False
            
            else:
                t=figura.l
                figura.l=figura.c
                figura.c=t
                self.mover(figura,figura.posx,figura.posy)
                return True
        else:
            self.matriz_met(figura.c,figura.l,figura.posx,figura.posy,1)
            return False
                
                
    def area_livre(self):
        return self.area