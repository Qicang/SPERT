# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:42:13 2018

@author: dell

function: to create a input file for material in a control assembly
"""

i = 48      #number of the segment

wid = 2.159     #width of each segment

l_m = ['POISON','BROSS','POISON']
l_d = [1,2,3]    #density
l_t = [900,900,900]    #temperature

file = open('control.assignment','w')

j = 0
while j < i:
    file.write('ZGRID   %10.6f   %10.6f   1\n' %(j*wid,(j+1)*wid))
    j = j + 1

file.write('\n')

j = 0
while j < 3:
    file.write('EXTRUDE   %10s   ASM2D%03d\n' %(l_m[j],j+1))
    j = j + 1
    
file.write('\n')

j = 0
k = 0
while k < 3:
    while j < i:
        file.write('ASSEMBLY  ASM2D%03d  REG2D%03d_3D%03d   %10.6f   %10.6f\n' %(k+1,k+1,j+1,j*wid,(j+1)*wid))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')

k = 0
j = 0
while k < 3:
    while j < i:
        file.write('REGION_PROPERTY   REG2D%03d_3D%03d   ATOM_DENSITY   %s\n' %(k+1,j+1,l_m[k]))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')

k = 0
j = 0
while k < 3:
    while j < i:
        file.write('REGION_PROPERTY   REG2D%03d_3D%03d   TEMPERATURE(K)   %s\n' %(k+1,j+1,l_t[k]))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')

k = 0
j = 0
while k < 3:
    while j < i:
        file.write('REGION_ALIAS   REG2D%03d_3D%03d   %s\n' %(k+1,j+1,l_m[k]))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')
    