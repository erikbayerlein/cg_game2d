# pylint: disable=all
import pygame

from cg.cg import Screen, Draw, Texture,Color
from characters.background import Background
from characters.cat import Bullet, Cat
from characters.inicio import imagem

pygame.init()

FPS = 30
clock = pygame.time.Clock()

width = 800
height = 600

screen = Screen(width, height).display


def home_screen():
    window = [0, 0, 800, 600]
    viewport1 = [0, 0, 800, 600]
    viewport2 = [450, 0, 500, 55]

    windows = [window]
    viewports = [viewport1, viewport2]

    space = Background(windows, viewports)
    img = imagem(windows, viewports, "spaceinvaders.PNG")

   
    color_filler = Color(screen, width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    instructions()
                    return
                elif event.key == pygame.K_ESCAPE:  
                    running = False

        screen.fill((0, 0, 0))
        img.draw(screen)
        space.draw(screen)
        Draw.circumference(screen, 650, 500, 50, (255, 255, 255))  
        color_filler.flood_fill2(650, 500, (255, 165, 0), animation=False)
       
      

       
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    

def instructions():
    window = [0, 0, 800, 600]
    viewport1 = [0, 0, 800, 600]
    viewport2 = [450, 0, 500, 55]

    windows = [window]
    viewports = [viewport1, viewport2]

    space = Background(windows, viewports)
    img = imagem(windows, viewports, "teste-instrucao.PNG")

   
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    py_invaders()
                    return
                elif event.key == pygame.K_ESCAPE:  
                    running = False

        screen.fill((0, 0, 0))
        img.draw(screen)
        space.draw(screen)
       
       
      

       
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


    
def py_invaders():
    window = [0, 0, 800, 600]
    viewport1 = [0, 0, 800, 600]
    viewport2 = [450, 0, 500, 55]

    windows = [window]
    viewports = [viewport1, viewport2]

    space = Background(windows, viewports)
    cat = Cat(windows, viewports)

    dt = 1

    bullets = []
    cooldown = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_w]:
            cat.move_up(dt)

        if keys[pygame.K_s]:
            cat.move_down(dt)

        if keys[pygame.K_a]:
            cat.move_left(dt)

        if keys[pygame.K_d]:
            cat.move_right(dt)

        screen.fill((0, 0, 0))
        space.draw(screen)
        cat.draw(screen)

        # bullets
        cooldown += clock.get_time()
        if cooldown > 200:
            cooldown = 0

        if keys[pygame.K_SPACE] and cooldown == 0:
            x, _ = cat.polygon.center()
            y = cat.polygon.y_min()
            bullets.append(Bullet(x, y))

        if bullets:
            for bullet in bullets:
                bullet.move(screen)
                if bullet.polygon.y_min() <= 0:
                    bullets.pop(0)
                    del bullet

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


def game_over():
    window = [0, 0, 800, 600]
    viewport1 = [0, 0, 800, 600]
    viewport2 = [450, 0, 500, 55]

    windows = [window]
    viewports = [viewport1, viewport2]

    space = Background(windows, viewports)
    img = imagem(windows, viewports, "game_over.PNG")
   
   

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    py_invaders()
                    return
                elif event.key == pygame.K_ESCAPE:  
                    running = False
                    
        screen.fill((0, 0, 0))
        img.draw(screen)
        space.draw(screen)
       
       
       

       
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



def main():
    home_screen()

if __name__ == "__main__":
    main()
