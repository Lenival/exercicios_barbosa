# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 18:46:35 2021

@author: LENI
"""

import cairo
import numpy as np


# Confete simulation rsrsrsr

def multi_circunscrito(N=3, R=500, x_c=510, y_c=540, espessura=3, largura=1920, altura=1080, salvar=0):
    separacao = x_c - R
    # Salvando arquivos svg ilustrando etapas da simulação
    if salvar :
        with cairo.SVGSurface("poligono_circunscrito.svg", largura, altura) as surface:
            for m in range(2):            
                for n in range(3+m*(N-1),N+1+m*2*N,1+2*m):
                    
                        
                    theta_v = (2*np.pi/n)*np.arange(0,n)
                    vertices = np.zeros((n,2))
                    vertices[:,:] = np.transpose([R*np.cos(theta_v[:]),R*np.sin(theta_v[:])])
                    vertices = vertices + [x_c,y_c]
        
                    c = cairo.Context(surface)
        
                    # Desenhando o cículo com o segmento de referência
                    c.set_source_rgb(1,0,1)
                    c.arc(x_c, y_c, R, 0, 2*np.pi)
                    c.set_line_width(espessura)
                    c.set_source_rgb(0,1,0)
                    c.stroke()
                    
                    # lines
                    c.set_source_rgb(0,0,0)
                    c.move_to(x_c + R, y_c)
                    # Desenhando arestas a partir do vértices
                    for i in vertices:
                        c.line_to(i[0], i[1])
                    c.close_path()
                    c.set_line_width(espessura)
                    c.stroke()
                    
                    for i in vertices:
                        c.set_source_rgba(0,0,1,0.5)
                        c.arc(i[0], i[1], 1.5*espessura, 0, 2*np.pi)
                        c.fill_preserve()
                        c.stroke()
                            
                    c.set_source_rgba(0,0,0,1)
                    c.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
                        cairo.FONT_WEIGHT_NORMAL)
                    c.set_font_size(int(3*R/20))
                    
                    c.move_to(x_c-int(3*R/20), y_c)
                    c.show_text(f"n={n}")
                    
                    
                    x_c = x_c + separacao + 2*R
                x_c = separacao + R
                y_c = y_c + separacao + 2*R

if __name__ == "__main__":
    
    R = 100      # raio da circunferência
    espessura=2 #espessura da linha
    largura=1366 #resolução horizontal
    altura=768 # Resolução vertical
    x_c =120   # x do centro da circunferência
    y_c =120    # y do centro da circunferência
    n = 7   # Número de confetes
    multi_circunscrito(n,R, x_c, y_c, espessura, largura, altura,1)
        