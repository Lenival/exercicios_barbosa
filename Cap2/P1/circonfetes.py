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
    #n[:,0:2] = n[:,0:2]*[2*R,2*R] + [x_c,y_c]
    n[:,0:2] = n[:,0:2]*[largura,altura] + [x_c,y_c]
                
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
            
            c.set_source_rgb(0, 0, 0)
        
            c.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
                cairo.FONT_WEIGHT_NORMAL)
            c.set_font_size(int(R/20))
            
            c.move_to(largura/10, R/20+altura/10)
            c.show_text(f"D={2*R}")
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
                        
            c.set_source_rgb(0, 0, 0)
        
            c.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
                cairo.FONT_WEIGHT_NORMAL)
            c.set_font_size(int(R/20))
            
            c.move_to(largura/10, R/20+altura/10)
            c.show_text(f"D={2*R}")
            c.move_to(largura/10, 2*R/20+altura/10)
            c.show_text(f"Nd={np.sum(confete_s)}")
            c.move_to(largura/10, 3*R/20+altura/10)
            c.show_text(f"Nc={np.sum(confete_c)}")
            c.move_to(largura/10, 4*R/20+altura/10)
            c.show_text(f"C=D*(Nc/Nd)={np.round(2*R*np.sum(confete_c)/np.sum(confete_s),2)}")
            c.stroke()
     
    # Retornando razão entre confetes sobre a circunferência e segmento
    return np.sum(confete_c)/np.sum(confete_s)
    
if __name__ == "__main__":
    
    # Parâmetros da simulação
    r = 10       # tamanho dos confetes
    R = 300      # raio da circunferência
    espessura=2 #espessura da linha
    largura=1366 #resolução horizontal
    altura=768 # Resolução vertical
    x_c =largura/2    # x do centro da circunferência
    y_c =altura/2    # y do centro da circunferência
    grade = x_c*y_c # Número total de pontos
    N = 10000   # Número de confetes
    
    simulacoes = 10 # Número de simulações
    temp = 0        # Acumulador de resultados
    for i in range(simulacoes):
        temp = temp + jogar_confete(r, R, x_c, y_c, espessura, largura, altura, N,i==simulacoes-1)
    print(temp/simulacoes)
        
    