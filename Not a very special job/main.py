#卐
import pygame

window=pygame.display.set_mode((700,500))
pygame.display.set_caption("Slaughter House")
back=pygame.transform.scale(pygame.image.load("background.png"),(700,500))
sprite=pygame.transform.scale(pygame.image.load("sprite.png"),(100,100))
clock=pygame.time.Clock()
run=True
x,y=100,100
speed=7


while run:
    window.blit(back,(0,0))
    window.blit(sprite,(x,y))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed

    if keys[pygame.K_UP] and y<0:
        y+=speed

    if keys[pygame.K_DOWN] and y>400:
        y-=speed

    if keys[pygame.K_RIGHT] and x>600:
        x-=speed
            
    if keys[pygame.K_LEFT] and x<0:
        x+=speed
        

    pygame.display.update()
    clock.tick(60)