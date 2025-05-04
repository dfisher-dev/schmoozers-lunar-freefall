import pygame,sys
import time
from freeFallNew import run_mission_increment
from freeFallNew import create_new_mission


# pygame setup
pygame.init()
width=1280
height=720
screen = pygame.display.set_mode((1280, 720))
bg_img=pygame.image.load('Surface.png')
bg=pygame.transform.scale(bg_img,(1280,720))
#Menu Set Up
MENU = pygame.display.set_mode((1280,720))
MENU_img=pygame.image.load('MENU.png')
MENU=pygame.transform.scale(MENU_img,(500,500))
#Setting Fps for time
clock = pygame.time.Clock()
#Controller image
controller_img=pygame.image.load('Gizmo.png')
controller=pygame.transform.scale(controller_img,(360,360))
#Moon
moon_img=pygame.image.load('Moon.png')
Moon=pygame.transform.scale(moon_img,(1280,720))
#Lander 
lander_img=pygame.image.load('The Lander.png')
lander=pygame.transform.scale(lander_img,(200,200))
#Lander Shadow
shadow_img=pygame.image.load('Shadow.png')
shadow=pygame.transform.scale(shadow_img,(300,300))
sy=550
#thruster Fire
Fire_img=pygame.image.load('Fire.png')
Fire=pygame.transform.scale(Fire_img,(200,200))
#kaboom 
Kaboom_img=pygame.image.load('Kaboom.png')
Kaboom=pygame.transform.scale(Kaboom_img,(250,250))
#Setting up the ability to draw text on the screen
text_font=pygame.font.SysFont("Arial",30)
text_font2=pygame.font.SysFont("Arial",110,True)
text_font3=pygame.font.SysFont("Arial",120,True)
text_font4=pygame.font.SysFont("Arial",50,True)
def draw_text(text,font,text_col,x,y):
    img = font.render(text,False,text_col)
    screen.blit(img,(x,y))
ly=50
#Gravity
G=1
#Terminal velocity
tv=1
#Thrust exponential
te=0
#For the screen scrolling
i=0
j=0
z=0
#Thrust
Thrust=False
time_s=int(0)
time_m=int(0)
endheight=False


running = True

Start=True
dt = 0
Frames=0

#--------------------------------------------------------this is where the menu code starts
user_ip=""
user_ip2=""
user_ip3=""
continue_button=pygame.Rect(500,600,280,32)
input_rect=pygame.Rect(570,320,140,32)
input_rect2=pygame.Rect(570,420,140,32)
input_rect3=pygame.Rect(570,520,140,32)
color_active=pygame.Color(0,205,100)
color_passive=pygame.Color(0,100,0)
active=False
active2=False
active3=False
color=pygame.Color(0,0,0)
color2=pygame.Color(0,0,0)
color3=pygame.Color(0,0,0)
error=False
while Start:
    clock.tick(60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Start = False
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active=True
                else:
                    active=False
                if input_rect2.collidepoint(event.pos):
                    active2=True
                else:
                    active2=False
                if input_rect3.collidepoint(event.pos):
                    active3=True
                else:
                    active3=False
                if continue_button.collidepoint(event.pos):
                    if user_ip.isdigit() and user_ip2.isdigit() and user_ip3.isdigit():
                        initial_height=int(user_ip)
                        initial_mass=int(user_ip2)
                        initial_fuel=int(user_ip3)
                        Start=False
                    else:
                        error=True

            if event.type == pygame.KEYDOWN:
                if active2==True:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip2=user_ip2[:-1]
                    else:
                        user_ip2+=event.unicode
                if active==True:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip=user_ip[:-1]
                    else:
                        user_ip+=event.unicode
                if active3==True:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip3=user_ip3[:-1]
                    else:
                        user_ip3+=event.unicode
    if active:
        color=color_active
    else:
        color=color_passive
    if active2:
        color2=color_active
    else:
        color2=color_passive
    if active3:
        color3=color_active
    else:
        color3=color_passive
    screen.fill((0,0,0))
    screen.blit(Moon,(1,1))
    text_surface=text_font.render(user_ip,True,(0,0,0))
    text_surface2=text_font.render(user_ip2,True,(0,0,0))
    text_surface3=text_font.render(user_ip3,True,(0,0,0))
    draw_text("Lunar ",text_font3,(0,100,0),340,50)
    draw_text("Lander ",text_font3,(0,100,0),610,50)
    draw_text("Lunar Lander",text_font2,(0,205,100),350,50)
    screen.blit(MENU,(375,200))
    draw_text("Height:",text_font4,(0,0,0),570,260)
    draw_text("Mass: ",text_font4,(0,0,0),570,360)
    draw_text("Fuel: ",text_font4,(0,0,0),570,460)
    pygame.draw.rect(screen,(color),input_rect,)
    pygame.draw.rect(screen,(color2),input_rect2,)
    pygame.draw.rect(screen,(color3),input_rect3,)
    pygame.draw.rect(screen,(144, 238, 144),continue_button,)
    draw_text("Continue ",text_font,(0,0,0),500,600)
    screen.blit(text_surface,(input_rect))
    screen.blit(text_surface2,(input_rect2))
    screen.blit(text_surface3,(input_rect3))
    input_rect.w=max(150,text_surface.get_width()+10)
    input_rect2.w=max(150,text_surface2.get_width()+10)
    input_rect3.w=max(150,text_surface3.get_width()+10)
    if error:
        draw_text("INTEGERS ONLY!",text_font4,(0,0,0),900,300)

    pygame.display.update()


create_new_mission(initial_height, initial_mass, initial_fuel)


while running:
    clock.tick(15)
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
    if endheight==False:
        if Thrust==True:
            if Fuel>0:
             #Fuel-=0.05
             tv-=0.05
             te-=0.025
             ly+=te
    
    
    # each loop will get the mission data, used below
    if endheight==False:
        dataList = run_mission_increment(Thrust)
        velocity = dataList[0]
        thrustConstant = dataList[1]
        altitude = dataList[2]
        fuelRemaining = dataList[3]

    # change Fuel to correspond to fuelRemaining
    Fuel = fuelRemaining



    
    #Timer
    Frames+=1
    if Frames==15:
        time_s+=1
        Frames=0
    if time_s==60:
        time_m+=1
        time_s=0 
    screen.fill((0,0,0))

    if endheight==False:
        if z==0:
            screen.blit(bg,(i,j))
            screen.blit(bg,(width+i,j))
        if z==1:
            screen.blit(Moon,(i,j))
            screen.blit(Moon,(width+i,j))
        screen.blit(Moon,(i,height+j))
        screen.blit(Moon,(width+i,height+j))
        j-=2
    else:
        screen.blit(Moon,(i,j))
        screen.blit(Moon,(width+i,j))
    screen.blit(Moon,(i,height+j))
    screen.blit(Moon,(width+i,height+j))
    screen.blit(controller,(0,360))
    if endheight==False:
        if Thrust==True:
            if Fuel > 0:
                screen.blit(Fire,(805,ly+25))
    screen.blit(lander,(800,ly))
    screen.blit(shadow,(770,sy))
    #Display text
    draw_text("Time: ",text_font,(0,205,100),90,415)
    draw_text("Fuel: ",text_font,(0,205,100),90,445)
    draw_text("Height: ",text_font,(0,205,100),90,475)
    draw_text("Velocity: ",text_font,(0,205,100),90,505)
    draw_text(str(int(Fuel)),text_font,(0,205,100),150,445)
    draw_text(":",text_font,(0,205,100),190,415)
    draw_text(str(int(time_s)),text_font,(0,205,100),200,415)
    draw_text(str(int(time_m)),text_font,(0,205,100),160,415)
    draw_text(str(int(altitude)),text_font,(0,205,100),200,475)
    draw_text(str(int(velocity)),text_font,(0,205,100),200,505)
    #Percent_mover()
    if i==-width:
       screen.blit(Moon,(width+1,j))
       i=0
       z=1
    if j==-height:
       screen.blit(Moon,(i,height+1))
       j=0
       z=1
    i-=0.5
    if endheight==False:
        if tv!=G:
            if Thrust==False:
                if te<1:
                    te+=0.025
                tv+=0.05
                ly+=tv
        else:
            ly+=G
    if altitude<2000:
        if velocity<0:
            if sy>ly+30:
                sy-=2
    else:
        if sy<550:
            sy+=2
    if altitude<0:
        endheight=True
        if velocity<-5:
            screen.blit(Kaboom,(800,ly))
            # time.sleep(5)
           # break
       # break



    pygame.display.update()
pygame.quit()
    