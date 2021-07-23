# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:25:51 2021

@author: LENI
"""
import cairo
import numpy as np

def equilatero(R,x_c,y_c,espessura,largura,altura):
    
    # Criação do arquivo onde serão salvos os desenhos
    surface = cairo.SVGSurface("equilatero.svg", largura, altura)
    c = cairo.Context(surface)
    
    # Guardando tamanho da separação entre as figuras
    separacao = x_c - R
    
            
    c.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
        cairo.FONT_WEIGHT_NORMAL)
    c.set_font_size(int(3*R/20))


    for i in range(3):
        
        # Triângulo equilátero
        if i > 1:
            c.set_source_rgb(0, 0, 1)
            c.move_to(x_c, y_c)
            c.line_to(x_c+R/2, y_c+np.sqrt(3)*0.5*R)
            c.line_to(x_c+R, y_c)
            c.close_path()
            c.set_line_width(espessura)
            c.stroke()
        
        # Segunda circunferência
        if i > 0:
            c.set_source_rgb(0, 0, 0)
            c.arc(x_c+R, y_c, R, 0, 2*np.pi)
            c.set_line_width(espessura)
            c.stroke()
        
        # Primeira Circunferência
        c.set_source_rgb(0, 0, 0)
        c.arc(x_c, y_c, R, 0, 2*np.pi)
        c.set_line_width(espessura)
        c.stroke()  
        c.move_to(x_c-int(3*R/20), y_c)
        c.show_text("A")
        c.stroke() 
        
        # Desenho dos centros feitos dedpois para ficar por cima das linhas
        c.set_source_rgb(0, 0, 1)
        c.arc(x_c, y_c, 3*espessura, 0, 2*np.pi)
        c.set_line_width(espessura)
        c.fill()
        c.stroke()
        
        if i > 0:
            c.set_source_rgb(1, 0.6, 0)
            c.arc(x_c+R, y_c, 3*espessura, 0, 2*np.pi)
            c.set_line_width(espessura)
            c.fill()
            c.stroke()    
            c.move_to(x_c+R+int(R/20), y_c)
            c.show_text("B")
            c.stroke() 
        
        if i > 1:
            c.set_source_rgb(1, 0, 0)
            c.arc(x_c+R/2, y_c+np.sqrt(3)*0.5*R, 3*espessura, 0, 2*np.pi)
            c.set_line_width(espessura)
            c.fill()
            c.stroke()  
            c.move_to(x_c+R/2-int(R/20), y_c+np.sqrt(3)*0.5*R+int(3*R/20))
            c.show_text("C")
            c.stroke() 
        
        x_c = x_c + 3*separacao + (i+2)*R
        



if __name__ == "__main__":
    R = 100      # raio da circunferência
    espessura=1 #espessura da linha
    largura=1000 #resolução horizontal
    altura=240 # Resolução vertical
    x_c =120   # x do centro da circunferência
    y_c =120    # y do centro da circunferência
    equilatero(R, x_c, y_c, espessura, largura, altura)