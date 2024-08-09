# pylint: disable=all
import pygame

from cg.cg import Screen, Draw,Texture
from characters.background import Background
from characters.cat import Bullet, Cat
from characters.inicio import imagem


pygame.init()

FPS = 30
clock = pygame.time.Clock()

width = 800
height = 600

screen = Screen(width, height).display


def run():
    # window = [0, 0, 1200, 1000]
    window = [0, 0, 800, 600]
    viewport1 = [0, 0, 800, 600]
   
    viewport2 = [450, 0, 500, 55]

    windows = [window]
    viewports = [viewport1, viewport2]

    space = Background(windows, viewports)
   
  

    


    while True:
        if pygame.event.get(pygame.QUIT): break
        pygame.event.pump()

       

        screen.fill((0, 0, 0))
      
        space.draw(screen)
     
        

      

        # Draw "PY_INVADERS" text
        Draw.draw_text(screen, "PY_INVADERS", width // 2-125 , height // 2 - 50, 50, (255, 255, 255))
        Draw.draw_text(screen,"PRESS ENTER TO PLAY",width//2-200,height//2,50,(255,255,255))
       
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
