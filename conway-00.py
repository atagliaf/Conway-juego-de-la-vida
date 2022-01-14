# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 22:05:42 2020

@author: alberto.tagliaferri
"""
import os, time
M=[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   ]


COLUMNAS=len(M[0])
FILAS=len(M)
DIVISOR='----------------------------------------------------'
DEBUG=False

def mostrar(M):
#    print(M)
    CHAR=[' ','x'] # caracteres a mostrar para celda muerta/viva
    f_range = range(FILAS)
    c_range = range(COLUMNAS)
#     titulo columnas
    os.system('cls')
    mostrar.paso+=1
    print('paso ', mostrar.paso)
    f='   ['
    for j in c_range:
        f=f+str(j)+ ' '
    f=f+']'; print(f)
    
    for i in f_range:      
        f='['+str(i)+']|'
        for j in c_range:
            f=f+CHAR[M[i][j]] + '|'
        print(f)
    time.sleep(1)
    return;

def vecinos(M,i,j):
    if (DEBUG): print('vecinos: ['+str(i)+','+str(j)+']')
    n=   M  [i][j-1]          +M  [i][j+1]   \
        +M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]  \
        +M[i+1][j-1]+M[i+1][j]+M[i+1][j+1]
    return n

def nextcell(M,i,j):
    n=vecinos(M,i,j)
    if(M[i][j] == 1):
        if(n == 2 or n == 3):
            return 1
    elif(n==3):
        return 1
    return 0

def nextgen(M):
    f_range = range(1,FILAS-1)
    c_range = range(1,COLUMNAS-1)
    N=[]
    for i in range(FILAS): 
        N.append([0]*COLUMNAS)
    for i in f_range:         
        for j in c_range:
            N[i][j]=nextcell(M,i,j)
    return N
           
mostrar.paso=0
while(True):
    mostrar(M)
    M=nextgen(M)
    

