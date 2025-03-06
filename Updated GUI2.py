import pygame

# pygame setup
pygame.init()
width=1280
height=720
screen = pygame.display.set_mode((1280, 720))
bg_img=pygame.image.load('Software Arch/Surface.png')
bg=pygame.transform.scale(bg_img,(1280,720))
#Menu Set Up
MENU = pygame.display.set_mode((1280,720))
MENU_img=pygame.image.load('Software Arch/MENU.png')
MENU=pygame.transform.scale(MENU_img,(500,500))
#Setting Fps for time
clock = pygame.time.Clock()
#Controller image
controller_img=pygame.image.load('Software Arch/Gizmo.png')
controller=pygame.transform.scale(controller_img,(360,360))
#Moon
moon_img=pygame.image.load('Software Arch/Moon.png')
Moon=pygame.transform.scale(moon_img,(1280,720))
#Lander 
lander_img=pygame.image.load('Software Arch/The Lander.png')
lander=pygame.transform.scale(lander_img,(200,200))
#thruster Fire
Fire_img=pygame.image.load('Software Arch/Fire.png')
Fire=pygame.transform.scale(Fire_img,(200,200))
#Setting up the ability to draw text on the screen
text_font=pygame.font.SysFont("Arial",30)
text_font2=pygame.font.SysFont("Arial",110,True)
def draw_text(text,font,text_col,x,y):
    img = font.render(text,False,text_col)
    screen.blit(img,(x,y))
#Moves the Percent sign to follow the number
def Percent_mover():
    if Fuel>=100:
        draw_text("%",text_font,(0,205,100),192,445)
    if Fuel<100 and Fuel>=10:
        draw_text("%",text_font,(0,205,100),177,445)
    if Fuel <10:
        draw_text("%",text_font,(0,205,100),164,445)
#Lander Y direction
ly=50
#Gravity
G=0.5
#For the screen scrolling
i=0
j=0
#Thrust
Thrust=False
time_s=int(0)
time_m=int(0)
Fuel=int(100)
h=1
velocity=1
running = True

Start=True
dt = 0
Frames=0
#commented out for the meantime: this is the menu
#while Start:
    #screen.blit(Moon,(1,1))
    #for event in pygame.event.get():
          #  if event.type == pygame.QUIT:
        #       Start = False
   # draw_text("Lunar Lander",text_font2,(0,205,100),350,50)
   # screen.blit(MENU,(375,200))
   # pygame.display.update()

#turned the lander sim into a function so it just needs to be called
while running:
    clock.tick(60)
    # poll for events
    # pygame.QUIT event means the user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Thrust=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Thrust=False
    if Thrust==True:
        if Fuel>0:
            Fuel-=0.05
            ly-=3
    #Timer
    Frames+=1
    if Frames==60:
        time_s+=1
        Frames=0
    if time_s==60:
        time_m+=1
        time_s=0 
    screen.fill((0,0,0))

    if ly<100:
        screen.blit(bg,(i,j))
        screen.blit(bg,(width+i,j))
    if ly>100:
        screen.blit(bg,(i,j))
        screen.blit(bg,(width+i,j))
        screen.blit(Moon,(i,height+j))
        screen.blit(Moon,(width+i,height+j))
        j-=0.5
    screen.blit(Moon,(i,height+j))
    screen.blit(Moon,(width+i,height+j))
    screen.blit(controller,(0,360))
    if Thrust==True:
        screen.blit(Fire,(805,ly+25))
    screen.blit(lander,(800,ly))
    if event.type==pygame.KEYDOWN:
        if event.type==pygame.K_SPACE:
            ly+=2
    #Display text
    draw_text("Time: ",text_font,(0,205,100),90,415)
    draw_text("Fuel: ",text_font,(0,205,100),90,445)
    draw_text("Height: ",text_font,(0,205,100),90,475)
    draw_text("Velocity: ",text_font,(0,205,100),90,505)
    draw_text(str(int(Fuel)),text_font,(0,205,100),150,445)
    draw_text(":",text_font,(0,205,100),190,415)
    draw_text(str(int(time_s)),text_font,(0,205,100),200,415)
    draw_text(str(int(time_m)),text_font,(0,205,100),160,415)
    draw_text(str(int(h)),text_font,(0,205,100),200,475)
    draw_text(str(int(velocity)),text_font,(0,205,100),200,505)
    Percent_mover()
    if i==-width:
        screen.blit(bg,(width+1,j))
        i=0
    if j==-height:
        screen.blit(bg,(i,height+1))
        j=0
    i-=0.5
    ly+=G


    pygame.display.update()
pygame.quit()
    