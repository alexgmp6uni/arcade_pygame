import pygame
import letras
import os
import time
from pygame.locals import *
import sprites


# Constantes de game over
__ANCHO = 640
__ALTO = 480
__VX=2

# Inicializaciones y variables globales
pygame.init()
font_name ="WONDER.TTF"
screen = pygame.display.set_mode((__ANCHO,__ALTO))
pygame.display.set_caption("game over arcade")
reloj = pygame.time.Clock()
fondo = pygame.image.load("data/fondo_game_over.jpeg")



def main():
    init_letras = letras.Letra()

    sprites = init_letras.text_banner("Game Over")
    
    exit = False   
    vx = 2
    
    while exit != True:    
        #screen.fill((0, 0, 0))
        screen.blit(fondo, (0, 0))
        for sprite in sprites:
            sprite.move(-vx,0)
            sprite.update(screen)
            
            if sprites[-1].rect.left < -45:
                sprites = init_letras.text_banner("Game Over")
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return "QUIT"
            elif event.type == KEYDOWN and event.key != K_ESCAPE:
                
                return "RESTART"
                
        reloj.tick(144)     


        
        



            
                
           
                  
        

       
 

# INICIO
if __name__ == '__main__':
    main()

