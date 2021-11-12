# Import "pygame" module 
import pygame
# Import "time" module
import time
# Initialize "pygame"
pygame.init() 

# Create a screen of size (400, 600)
screen = pygame.display.set_mode((400,600))
# Set the "screen" title as "Counter" 
pygame.display.set_caption("Counter")

# RGB color combinations
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
YELLOW = (255,255,0)

# gdp stands for "Gross Domestic Product"
gdp = [7.862, 8.498, 5.241, 5.456, 6.386, 7.41, 7.996, 8.17, 7.168, 6.811]
yloc = 50

carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
            
    screen.fill(DARKBLUE)
    
    font1 = pygame.font.Font(None, 30)
    text1 = font1.render("India's GDP for the years 2009-2018:", 1, WHITE)
    screen.blit(text1, (20, 10))
    
    for i in gdp:
        font2 = pygame.font.Font(None, 50)
        gdp_rounded = round(i, 2)
        text2 = font2.render(str(gdp_rounded), 1, YELLOW)
        screen.blit(text2, (170, yloc))
        yloc += 40 
        pygame.display.flip()
        time.sleep(2)
    break

pygame.quit()