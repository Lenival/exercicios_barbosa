# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:07:21 2021

@author: LENI
"""

import cairo
import math
import numpy as np


# Confete simulation rsrsrsr

# Parâmetros da simulação
r = 0.5       # tamanho dos confetes
R = 500      # raio da circunferência
x_c =960    # x do centro da circunferência
y_c =540    # y do centro da circunferência
grade = x_c*y_c # Número total de pontos
N = 100000   # Número de confetes

# Valores aleatórios para inicializar posição e cor dos confetes
n = np.random.rand(N,5)

# Ajustando a referência de posição em relação ao centro da circunferência
n[:,0:2] = n[:,0:2]-0.5
# Calculando a posição final dos confetes
n[:,0:2] = n[:,0:2]*[2*R,2*R] + [x_c,y_c]
#n[:,0:2] = n[:,0:2]*grade
#n[:,0] = [int(n[:,0])%x_c]+x_c
#n[:,1] = [int(n[:,1])%y_c]+y_c
            
# Calculando distância do confete ao centro
dist_c = np.sqrt(np.sum(np.power(n[:,0:2]-[x_c, y_c],2),axis=1))
# Verificando onde houve colisão do confete com a circunferência
confete_c = (dist_c[:] >= (R-r)) & (dist_c[:] <= (R+r))

# Verificando onde houve colisão do confete com o segmento
confete_s = ((n[:,0] >= (x_c-R)) & (n[:,0] <= (x_c+R))) & ((n[:,1] >= (y_c-r)) & (n[:,1] <= (y_c+r)))


with cairo.SVGSurface("circunferência.svg", 1920, 1080) as surface:
    
    c = cairo.Context(surface)
    
    # background
    c.set_source_rgb(1,1,1)
    c.paint()
    
    # Desenhando o cículo com o segmento de referência
    c.set_source_rgb(1,0,1)
    # x, y, radius, start_angle, stop_angle
    c.arc(x_c, y_c, R, 0, 2*math.pi)
    c.line_to(x_c-R, y_c)
    c.set_line_width(1)
    c.set_source_rgb(0,0,0)
    c.stroke()

with cairo.SVGSurface("confetes.svg", 1920, 1080) as surface:
    c = cairo.Context(surface)
    # Jogando os confetes
    for i in n:
        # Cor aleatória para os confetes
        c.set_source_rgb(i[2],i[3],i[4])
        # Posição aleatória para os confetes
        c.arc(i[0], i[1], r, 0, 2*math.pi)
        c.fill_preserve()
        c.stroke()
    
    # Desenhando o cículo com o segmento de referência
    c.set_source_rgb(1,0,1)
    # x, y, radius, start_angle, stop_angle
    c.arc(x_c, y_c, R, 0, 2*math.pi)
    c.line_to(x_c-R, y_c)
    c.set_line_width(1)
    c.set_source_rgb(0,0,0)
    c.stroke()


with cairo.SVGSurface("colisões.svg", 1920, 1080) as surface:
    c = cairo.Context(surface)       
    # Destacando os confetes na circunferência
    for i in n[confete_c,:]:
        # Cor aleatória para os confetes
        c.set_source_rgb(i[2],i[3],i[4])
        # Posição aleatória para os confetes
        c.arc(i[0], i[1], r, 0, 2*math.pi)
        c.fill_preserve()
        c.stroke()
    
    
    # Destacando os confetes no segmento de referência
    for i in n[confete_s,:]:
        # Cor aleatória para os confetes
        c.set_source_rgb(i[2],i[3],i[4])
        # Posição aleatória para os confetes
        c.arc(i[0], i[1], r, 0, 2*math.pi)
        c.fill_preserve()
        c.stroke()
        
    # Desenhando o cículo com o segmento de referência
    c.set_source_rgb(1,0,1)
    # x, y, radius, start_angle, stop_angle
    c.arc(x_c, y_c, R, 0, 2*math.pi)
    c.line_to(x_c-R, y_c)
    c.set_line_width(1)
    c.set_source_rgb(0,0,0)
    c.stroke()
  
# printing message when file is saved
print(np.sum(confete_c)/np.sum(confete_s))