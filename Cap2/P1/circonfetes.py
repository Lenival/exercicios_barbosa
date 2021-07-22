# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 23:07:21 2021

@author: LENI
"""

import cairo
import math
import numpy as np


# Confete simulation rsrsrsr

def jogar_confete(r=3, R=500, x_c=510, y_c=540, espessura=3, largura=1920, altura=1080, N=10000, salvar=0):
    # Valores aleatórios para inicializar posição e cor dos confetes
    n = np.random.rand(N,5)
    
    # Ajustando a referência de posição em relação ao centro da circunferência
    n[:,0:2] = n[:,0:2]-0.5
    # Calculando a posição final dos confetes
    n[:,0:2] = n[:,0:2]*[2*R,2*R] + [x_c,y_c]
    #n[:,0],n[:,1] = R*n[:,0]*np.cos(2*np.pi*n[:,1])+x_c, R*n[:,0]*np.sin(2*np.pi*n[:,1])+y_c
    #n[:,0] = [int(n[:,0])%x_c]+x_c
    #n[:,1] = [int(n[:,1])%y_c]+y_c
                
    # Calculando distância do confete ao centro
    dist_c = np.sqrt(np.sum(np.power(n[:,0:2]-[x_c, y_c],2),axis=1))
    # Verificando onde houve colisão do confete com a circunferência
    confete_c = (dist_c[:] >= (R-r-0.5*espessura)) & (dist_c[:] <= (R+r+0.5*espessura))
    
    # Verificando onde houve colisão do confete com o segmento
    confete_s = ((n[:,0] >= (x_c-R)) & (n[:,0] <= (x_c+R))) & ((n[:,1] >= (y_c-r-0.5*espessura)) & (n[:,1] <= (y_c+r+0.5*espessura)))
    
    # Salvando arquivos svg ilustrando etapas da simulação
    if salvar :
        with cairo.SVGSurface("circunferência.svg", largura, altura) as surface:
            
            c = cairo.Context(surface)
            
            # background
            c.set_source_rgb(1,1,1)
            c.paint()
            
            # Desenhando o cículo com o segmento de referência
            c.set_source_rgb(1,0,1)
            c.arc(x_c, y_c, R, 0, 2*math.pi)
            c.line_to(x_c-R, y_c)
            c.set_line_width(espessura)
            c.set_source_rgb(0,0,0)
            c.stroke()
        
        with cairo.SVGSurface("confetes.svg", largura, altura) as surface:
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
            c.set_line_width(espessura)
            c.set_source_rgb(0,0,0)
            c.stroke()
        
        
        with cairo.SVGSurface("colisões.svg", largura, altura) as surface:
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
            c.arc(x_c, y_c, R, 0, 2*math.pi)
            c.line_to(x_c-R, y_c)
            c.set_line_width(espessura)
            c.set_source_rgb(0,0,0)
            c.stroke()
     
    # Retornando razão entre confetes sobre a circunferência e segmento
    return np.sum(confete_c)/np.sum(confete_s)
    
if __name__ == "__main__":
    
    # Parâmetros da simulação
    r = 3       # tamanho dos confetes
    R = 400      # raio da circunferência
    x_c =800    # x do centro da circunferência
    y_c =450    # y do centro da circunferência
    espessura=3 #espessura da linha
    largura=1600 #resolução horizontal
    altura=900 # Resolução vertical
    grade = x_c*y_c # Número total de pontos
    N = 10000   # Número de confetes
    
    simulacoes = 10 # Número de simulações
    temp = 0        # Acumulador de resultados
    for i in range(simulacoes):
        temp = temp + jogar_confete(r, R, x_c, y_c, espessura, largura, altura, N,i==simulacoes-1)
    print(temp/simulacoes)
        
    