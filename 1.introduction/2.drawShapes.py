""""
Pygame Template

    Import
    Initialize
    Create Window
    Initialize Clock for FPS


    Loop
        Get events
            if quit
                quit pygame
        Apply Logic
        Update Display/Window
        Set FPS



"""

#Import
import pygame

# Initialize
pygame.init()

#Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Main Loop
start = True

while start:
    #Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    # Apply Logic
    window.fill((255,255,255))
    red, green, blue = (255,0,0), (0,255,0), (0,0,255)
    pygame.draw.polygon(window,red,((447,100),(780,100),(900,350),(788,600),(480,600),(342,350)))
    pygame.draw.circle(window,blue,(200,300),57,60)
    pygame.draw.line(window,green,(200,300),(788,600),50)
    pygame.draw.rect(window,blue,(468,347,345,70),border_radius=500)

    # update Display
    pygame.display.update()

    #set FPS
    clock.tick(fps)
