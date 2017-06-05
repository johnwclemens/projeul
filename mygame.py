import pygame
import math
import random
from pygame.locals import *

exp=0

#a=1
#while a==1:
def calc_exp():
    print" you killed a bandit"
    xp=random.randint(10, 30)
    exp+=xp
    print"you got, "+str(exp)+" xp"
    if exp>=500<1000:
        print"congradulations you are level 2"
    if exp>=1000<2000:
    	print"congradulations you are level 3"
    if exp>=2000:
    	print"congradulations you are level 4"



def Load_Images_and_Audio(images):
	print "Load_Images_and_Audio"
	for key in images:
		if key == 'p':
			images[key] = pygame.image.load("resources/images/dude.png")
		elif key == 'g':
			images[key] = pygame.image.load("resources/images/grass.png")

#2 
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos=[100,100]
acc=[0,0]
arrows=[]
badtimer=100  
badtimer1=0
badguys=[[640,100]]
healthvalue=194
pygame.mixer.init()

images = {'p':'', 'g':'', 'c':'', 'a':'', 'b':'', 'hb':'', 'h':'', 'go':'', 'y':'', }
Load_Images_and_Audio(images)

#player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")
badguyimg = pygame.image.load("resources/images/badguy.png")
healthbar = pygame.image.load("resources/images/healthbar.png") 
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")
xpBar2 = pygame.image.load("resources/images/xpBar2.png")

hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
pygame.mixer.music.load('resources/audio/moonlight.wav')

hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)
#4 
running = 1
exitcode = 0
while running:
    badtimer-=1
    screen.fill(0)
    #8
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True
        #elif=else if
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position=pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
    
        if event.type==pygame.QUIT:
            pygame.quit()   
            exit(0)
 #----------------------------------------------------------------------       
    print("p[0]=%d, p[1]=%d" % (playerpos[0], playerpos[1]))
    print("p_x", playerpos[0], "p_y", playerpos[1])
#-----------------------------------------------------------------------

    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

    for x in range(width/images['g'].get_width()+1):
            for y in range(height/images['g'].get_height()+1):
                screen.blit(images['g'],(x*100,y*100))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))
    screen.blit(xpBar2, (160, 415))
    #screen.blit(player, playerpos)
    #6.1
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(images['p'], 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
    #6.2
    for bullet in arrows:
        index=0
        velx=math.cos(bullet[0])*10
        vely=math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
            #6.3
    if badtimer==0:
        badguys.append([640, random.randint(50,430)])
        badtimer=100-(badtimer1*2)
        if badtimer1>=35:
            badtimer1=35
        else:
            badtimer1+=5
    index=0
    for badguy in badguys:
        if badguy[0]<-64:
            badguys.pop(index)
        badguy[0]-=7
        # 6.3.1 - Attack castle
        badrect=pygame.Rect(badguyimg.get_rect())
        badrect.top=badguy[1]
        badrect.left=badguy[0]
        if badrect.left<64:
            hit.play()
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        #6.3.2 - Check for collisions
        index1=0
        for bullet in arrows:
            bullrect=pygame.Rect(arrow.get_rect())
            bullrect.left=bullet[1]
            bullrect.top=bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0]+=1
                badguys.pop(index)
                arrows.pop(index1)
            index1+=1    
        # 6.3.3 - Next bad guy
        index+=1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
    # 6.4 - Draw clock
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)
    # 6.5 - Draw health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+8,8))
        for event in pygame.event.get():
if event.type == pygame.QUIT:
    exit_game()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            paused = not paused
    elif (  event.type == pygame.MOUSEBUTTONDOWN and
            pygame.mouse.get_pressed()[0]):
        for creep in creeps:
            creep.mouse_click_event(pygame.mouse.get_pos())
    def mouse_click_event(self, pos):
    """ The mouse was clicked in pos.
    """
    if self._point_is_inside(vec2d(pos)):
        self._decrease_health(3)    
    def _point_is_inside(self, point):
    """ Is the point (given as a vec2d) inside our creep's
        body?
    """
    img_point = point - vec2d(
        int(self.pos.x - self.image_w / 2),
        int(self.pos.y - self.image_h / 2))

    try:
        pix = self.image.get_at(img_point)
        return pix[3] > 0
    except IndexError:
        return False
    pygame.display.flip()
#--------------------------------------------------------
    #10 - Win/Lose check
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0
# 11 - Win/lose display        
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
