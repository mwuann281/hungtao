import pygame
import random
pygame.init()

running = True

fps = pygame.time.Clock()

screen = pygame.display.set_mode((600,600))

white = (255,255,255)
red = (250,0,0)
blue = (0,0,255)
black = (0,0,0)

points = 0 
live = 3

font = pygame.font.Font("freesansbold.ttf",24)

px=300
py=500

ex = random.randint(0,550)
ey = 50

ex1 = random.randint(0,550)
ey1 = 50

while running:
	mousex, mousey = pygame.mouse.get_pos()
	if live>0:
		fps.tick(15)

		pointdisplay = "Points:" + str(points)
		text_point = font.render(pointdisplay,True,white)

		livedisplay = "Lives:" + str(live)
		text_live = font.render(livedisplay,True,white)

		screen.fill(black)
		screen.blit(text_live,(500,20))
		screen.blit(text_point,(50,20))
		
		pygame.draw.rect(screen,blue,(px,py,200,20))
		pygame.draw.rect(screen,red,(ex,ey,50,50))
		pygame.draw.rect(screen,red,(ex1,ey1,50,50))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					px -= 40	
				elif event.key ==pygame.K_RIGHT:
					px += 40     
		if px+250>ex>px-50 and py+25>ey>py-50:
			points += 1
			ey = 50
			ex = random.randint(0,550)
		if px+250>ex1>px-50 and py+25>ey1>py-50:
			points += 1
			ey1 = 50
			ex1 = random.randint(0,550)

		if ey >= 0 and ey<600:
			if 0<=points<=30:
				ey+=15
			if 30<points<=60:
				ey+=16
			if 60<points<=100:
				ey+=17
			if 100<points:
				ey+=18
		else:
			live -= 1
			ey = 40
			ex = random.randint(0,550)
		if ey1 >= 0 and ey1<600:
			if 0<=points<=30:
				ey1+=5
			if 30<points<=60:
				ey1+=6
			if 60<points<=100:
				ey1+=7
			if 100<points:
				ey1+=8
		else:
			live -= 1
			ey1 = 40
			ex1 = random.randint(0,550)
	
	if live<1:
		screen.fill(black)
		text_reset = font.render("Play agian?",True, white,blue)
		screen.blit(text_reset,(200,300))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if 200<mousex<300 and 300<mousey<400:
					live=3 
					points = 0
					ey = 40
					ex = random.randint(0,550)
					ey1 = 40
					ex1 = random.randint(0,550)

	pygame.display.update()	
	
	
