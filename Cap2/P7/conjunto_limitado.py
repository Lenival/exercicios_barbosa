# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:20:49 2021

@author: LENI
"""
import cairo
import numpy as np
from scipy import spatial

def conjunto_limitado(N, R, x_c, y_c, espessura, largura, altura):
    
    # Guardando tamanho da separação entre as figuras
    separacao = x_c - R  
    # Calculando o offset para o terceiro desenho
    offsetx = 5*R + separacao
    
    
    # Valores aleatórios para inicializar posição e cor dos pontos
    n = (np.random.rand(N,2)-0.5)*2*R+[x_c, y_c]
    
    # Menor casca convexa que contém o conjunto de pontos
    convex = spatial.ConvexHull(n)
    
    # Matriz de distâncias dos vértices do convexo
    matriz_dist = spatial.distance_matrix(n[convex.vertices,:],n[convex.vertices,:])
    # Máxima distância só entre os vértices do convexo
    extremos = np.unravel_index(np.argmax(matriz_dist, axis=None), matriz_dist.shape)
    # Selecionando o centro da circunferência que conterá os pontos
    R_l = matriz_dist[extremos[0],extremos[1]]
    x_l = n[convex.vertices[extremos[0]],0]
    y_l = n[convex.vertices[extremos[0]],1]
    if x_l > n[convex.vertices[extremos[1]],0]:
        x_l = n[convex.vertices[extremos[1]],0]
        y_l = n[convex.vertices[extremos[1]],1]
    x_l = x_l + offsetx
    y_l = y_l + 2*R
  
    
    # Criação do arquivo onde serão salvos os desenhos
    surface = cairo.SVGSurface('conjunto_limitado.svg',largura, altura)
    c = cairo.Context(surface)
    
    
    # Fonte usada nos textos
    c.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
        cairo.FONT_WEIGHT_NORMAL)
    c.set_font_size(int(3*R/20))


    for i in range(3):
        
        # Desenhando casca convexa
        if i == 0 :
            # Desenhando arestas a partir do vértices
            for j in convex.vertices:
                c.line_to(n[j,0], n[j,1])
            c.close_path()
            c.set_source_rgba(1, 0, 0,0.4)
            c.set_dash([4.0,4.0])
            c.set_line_width(espessura)
            c.stroke()
        
        # Desenhando segmento entre os dois pontos mais distantes
        if i == 1:
            c.move_to(n[convex.vertices[extremos[0]],0], n[convex.vertices[extremos[0]],1])
            c.line_to(n[convex.vertices[extremos[1]],0], n[convex.vertices[extremos[1]],1])
            c.set_line_width(espessura)
            c.stroke()
        
        
        c.set_dash([])
        c.set_line_width(espessura)

        
        # Desenho dos pontos
        for j in range(N):
            c.set_source_rgb(0, 0, 0)
            c.arc(n[j,0], n[j,1], 2*espessura, 0, 2*np.pi)
            c.set_line_width(espessura)
            c.fill()
            c.stroke()
            
        if i==2:
            c.move_to(x_l-int(3*R/20), y_l)
            c.show_text("C")
            c.stroke()
            c.set_source_rgba(0, 0, 1,0.8)
            c.arc(x_l, y_l, R_l, 0, 2*np.pi)
            c.set_line_width(espessura)
            c.stroke()
        
        if i == 0 :
            n = n + [0,2*R + separacao]
        if i == 1 :
            n = n + [offsetx,-( separacao)]
        
    
        
    
if __name__ == "__main__":
    R = 150      # raio da circunferência
    espessura=1 #espessura da linha
    largura=1920 #resolução horizontal
    altura=1080 # Resolução vertical
    x_c =220   # x do centro da circunferência
    y_c =220    # y do centro da circunferência
    N = 50
    
    conjunto_limitado(N,R, x_c, y_c, espessura, largura, altura)