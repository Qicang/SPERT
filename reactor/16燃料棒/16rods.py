# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:42:59 2018

@author: dell

function: to create a input file for material in a 16 rod assembly
"""

i = 48      #number of the segment

wid = 2.159     #width of each segment

l_m = ['R_FUEL','R_CLAD','R_MOD','R_CLAD','R_CLAD']
l_d = [6.86451E-02,4.27639E-02,7.44873E-02,4.27639E-02,4.27639E-02]    #density
l_t = [5.65000E+02,5.65000E+02,5.65000E+02,5.65000E+02,5.65000E+02]    #temperature

file = open('16rods.assignment','w')

j = 0
while j < i:
    file.write('ZGRID   %10.6f   %10.6f   1\n' %(j*wid,(j+1)*wid))
    j = j + 1

file.write('\n')

j = 0
while j < 5:
    file.write('EXTRUDE   %10s   ASM2D%03d\n' %(l_m[j],j+1))
    j = j + 1
    
file.write('\n')

j = 0
k = 0
while k < 5:
    while j < i:
        file.write('ASSEMBLY  ASM2D%03d  REG2D%03d_3D%03d   %10.6f   %10.6f\n' %(k+1,k+1,j+1,j*wid,(j+1)*wid))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')

k = 0
j = 0
while k < 5:
    while j < i:
        file.write('REGION_PROPERTY   REG2D%03d_3D%03d   ATOM_DENSITY   %e\n' %(k+1,j+1,l_d[k]))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')

k = 0
j = 0
while k < 5:
    while j < i:
        file.write('REGION_PROPERTY   REG2D%03d_3D%03d   TEMPERATURE(K)   %e\n' %(k+1,j+1,l_t[k]))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')

k = 0
j = 0
while k < 5:
    while j < i:
        file.write('REGION_ALIAS   REG2D%03d_3D%03d   %s\n' %(k+1,j+1,l_m[k]))
        j = j + 1
    j = 0
    k = k + 1
    file.write('\n')
    