# A mini shooting game
# author: Yiyun Chen
# ref http://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python
import time
import pygame
from pygame.locals import *
import sys 
# 2 - Initialize the game
pygame.init()
width, height = 800, 600
screen=pygame.display.set_mode((width, height))
pygame.display.set_caption('Mini STG')
youhealth = 10
keys = [False, False, False, False]
playerpos=[350,500]
bosspos = [350,0]
arrows=[]
arrowws=[]
arrowwws=[]
boss_left=True
boss_health = 500
# 3 - Load images
player = pygame.image.load("resources/image/player1.png")
background = pygame.image.load("resources/image/background2.jpg")
arrow = pygame.image.load("resources/image/bullet1.png")
bossding = pygame.image.load("resources/image/bossding.png")
healthbar = pygame.image.load("resources/image/healthbar.png")
health = pygame.image.load("resources/image/health.png")
healthbar2 = pygame.image.load("resources/image/healthbar2.png")
health2 = pygame.image.load("resources/image/health2.png")
ping = pygame.image.load("resources/image/ping.png")
youwin = pygame.image.load("resources/image/youwin.png")
gameover = pygame.image.load("resources/image/gameover.png")
shoot_freq = 0
shoot_freq_2 = 0
rotfreq = 0
clock = pygame.time.Clock()
arroww = pygame.transform.scale(pygame.image.load("resources/image/bullet2.png"), (60,51))
arrowww = pygame.transform.scale(pygame.image.load("resources/image/bullet3.png"), (35,35))
# 4 - keep looping through

running = 1
exitcode = 0

while running:
	clock.tick(60)
	# 5 - clear the screen before drawing it again
	screen.fill(0)
	
	# 6 - draw the screen elements
	screen.blit(background, (0, 0))
	screen.blit(player, playerpos)
	screen.blit(bossding, bosspos)
	screen.blit(healthbar, (0,0))
	if boss_health < 300:
		screen.blit(ping, (550,0))
		if shoot_freq_2 % 65 == 0:
			arrowws.append([bosspos[0]+70,bosspos[1]+186,0,6,1])
			arrowws.append([bosspos[0]+70,bosspos[1]+186,3,8,0])
			arrowws.append([bosspos[0]+70,bosspos[1]+186,-3,8,0])
			arrowws.append([bosspos[0]+70,bosspos[1]+186,-6,6,1])
			arrowws.append([bosspos[0]+70,bosspos[1]+186,6,6,1])
			arrowws.append([bosspos[0]+70,bosspos[1]+186,9,8,0])
			arrowws.append([bosspos[0]+70,bosspos[1]+186,-9,8,0])
		shoot_freq_2 += 1
		if shoot_freq_2 > 64:
			shoot_freq_2 = 0
	for health1 in range(boss_health):
		screen.blit(health, (health1+3,3))
	screen.blit(healthbar2, (0,500))
	for health1 in range(youhealth):
		screen.blit(health2, (3,500+health1*10))
	index=0
	for bullet in arrows:
		bullet[1] -= 10
		screen.blit(arrow, (bullet[0], bullet[1]))
		if bullet[1] < 0:
			arrows.pop(index)		
		index += 1
	index2 = 0
	remv = []
	rotfreq += 1
	if rotfreq > 35:
		rotfreq = 0;
	for bullet in arrowws:
		bullet[1] += bullet[3]
		bullet[0] += bullet[2]
		if bullet[4] == 1:
			arroww1 = pygame.transform.rotate(arroww, rotfreq*10)
			screen.blit(arroww1, (bullet[0], bullet[1]))
		else:
			arrowww1 = pygame.transform.rotate(arrowww, rotfreq*10)
			screen.blit(arrowww1, (bullet[0], bullet[1]))
		if bullet[1] > 600 or bullet[1] < 0:
			if bullet[4] == 1:
				remv.append(index2)
			else:	
				bullet[3] = -bullet[3]
		if bullet[0] < 0 or bullet[0] > 800:
			if bullet[4] == 1:
				remv.append(index2)
			else:			
				bullet[2] = -bullet[2]
		
		index2 += 1
	for id in sorted(remv, reverse=True):
		arrowws.pop(id)
	# 7 - update the screen
	pygame.display.flip()
	# 8 - loop through the events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)	
		if event.type == pygame.KEYDOWN:
			if event.key==K_UP:
				keys[0]=True
			elif event.key==K_LEFT:
				keys[1]=True
			elif event.key==K_DOWN:
				keys[2]=True
			elif event.key==K_RIGHT:
				keys[3]=True
		if event.type == pygame.KEYUP:
			if event.key==pygame.K_UP:
				keys[0]=False
			elif event.key==pygame.K_LEFT:
				keys[1]=False
			elif event.key==pygame.K_DOWN:
				keys[2]=False
			elif event.key==pygame.K_RIGHT:
				keys[3]=False
	if shoot_freq % 5 == 0:
		arrows.append([playerpos[0]+10,playerpos[1]])
		arrows.append([playerpos[0]+30,playerpos[1]])
	shoot_freq += 1
	if shoot_freq > 4:
		shoot_freq = 0
	# 9 - Move player
	if keys[0]:
		playerpos[1]-=5
	elif keys[2]:
		playerpos[1]+=5
	if keys[1]:
		playerpos[0]-=5
	elif keys[3]:
		playerpos[0]+=5
	if playerpos[0] < 0:
		playerpos[0] = 0
	if playerpos[1] < 0:
		playerpos[1] = 0
	if playerpos[0] > 750:
		playerpos[0] = 750
	if playerpos[1] > 575:
		playerpos[1] = 575
	#move boss ding
	if boss_left:
		bosspos[0] -= 3
	else:
		bosspos[0] += 3
	if bosspos[0] < 0:
		bosspos[0] = 0
		boss_left = False
	if bosspos[0] >650:
		bosspos[0] = 650
		boss_left = True
	
	bossrect=pygame.Rect(bossding.get_rect())
	bossrect.top=bosspos[1]
	bossrect.left=bosspos[0]
	playerrect=pygame.Rect(player.get_rect())
	playerrect.top=playerpos[1]
	playerrect.left=playerpos[0]	
	index1=0
	for bullet in arrows:
		bullrect=pygame.Rect(arrow.get_rect())
		bullrect.left=bullet[0]
		bullrect.top=bullet[1]
		
		if bossrect.colliderect(bullrect):
			arrows.pop(index1)
			boss_health -= 3
		index1+=1
	index2 = 0	
	remv = []
	for bullet in arrowws:
		if bullet[4] == 1:
			bullrect=pygame.Rect(arroww.get_rect())
			bullrect.left=bullet[0]
			bullrect.top=bullet[1]
			if playerrect.colliderect(bullrect):
				youhealth -= 2
				remv.append(index2)	
		else:
			bullrect=pygame.Rect(arrowww.get_rect())
			bullrect.left=bullet[0]
			bullrect.top=bullet[1]			
			if playerrect.colliderect(bullrect):
				youhealth -= 1	
				remv.append(index2)		
		index2 += 1
	for id in sorted(remv, reverse=True):
		arrowws.pop(id)
	if youhealth < 0:
		running = 0
	if playerrect.colliderect(bossrect):
		running = 0
	if boss_health < 0:
		running = 0
		exitcode = 1
	pygame.font.init()
	mfont = pygame.font.SysFont(None,22)
	text = mfont.render("You have"+str(youhealth)+"HP left!", True, (0,0,0), (255,255,255))
	screen.blit(text, (50,50))	

if exitcode==0:
	screen.blit(gameover, (0,0))    
else:
	screen.blit(youwin, (0,0))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()	