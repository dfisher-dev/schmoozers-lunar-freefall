import pygame # type: ignore

# pygame setup
pygame.init()
width=1280
height=720
screen = pygame.display.set_mode((1280, 720))
bg_img=pygame.image.load('Surface.png')
bg=pygame.transform.scale(bg_img,(1280,720))
controller_img=pygame.image.load('Gizmo.png')
controller=pygame.transform.scale(controller_img,(360,360))
text_font=pygame.font.SysFont("Arial",30)
def draw_text(text,font,text_col,x,y):
    img = font.render(text,False,text_col)
    screen.blit(img,(x,y))
i=0
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    screen.blit(bg,(i,0))
    screen.blit(bg,(width+i,0))
    screen.blit(controller,(0,360))
    draw_text("Hello",text_font,(0,205,100),90,415)
    
    if i==-width:
        screen.blit(bg,(width+1,0))
        i=0
    i-=0.5

    pygame.display.update()

pygame.quit()