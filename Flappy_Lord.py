import pygame, sys, random
#CONST
pipe_height = range(300,550)

#FUNCTION:
def create_pipe():
	pipe_pos_y = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop = (450 , pipe_pos_y))
	top_pipe = pipe_surface.get_rect(midtop = (450 , pipe_pos_y - 750))	
	return bottom_pipe, top_pipe
def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 4
	return pipes
def draw_pipes(pipes):
	for pipe in pipes:
		if pipe.top > 200:
			screen.blit(pipe_surface, pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_surface, False, True)
			screen.blit(flip_pipe, pipe)
def check(pipes):
	for pipe in pipes:
		if bird_rect.colliderect(pipe):
			hit_sound.play()
			return False
	if bird_rect.top <= -70 or bird_rect.bottom >= 600:
		return False
	return True
def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird, -bird_movement*3, 1)
	return new_bird
def score_display(game_state):
	if game_state == True:
		score_surface = game_font.render(str(int(score)), True, (255,255,255))
		score_rect = score_surface.get_rect(center = (216,100))
		screen.blit(score_surface, score_rect)
	if game_state == False:
		score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))
		score_rect = score_surface.get_rect(center = (216,100))
		screen.blit(score_surface, score_rect)

		high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255,0,0))
		high_score_rect = high_score_surface.get_rect(center = (216,200))
		screen.blit(high_score_surface, high_score_rect)

#VARIABLE:
pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 2, buffer = 512)
pygame.init()
screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
gravity = 0.2
bird_movement = 0
count = 0
game_active = True
score = 0
high_score = 0
game_state = 'main game'
start = False

#background
bg = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/background-morning.png').convert()
bg = pygame.transform.scale2x(bg)
bg1 = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/background-morning1.png').convert()
bg1 = pygame.transform.scale2x(bg1)
bg2 = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/background-morning2.png').convert()
bg2 = pygame.transform.scale2x(bg2)
bg3 = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/background-night.png').convert()
bg3 = pygame.transform.scale2x(bg3)

#end game screen
end_screen = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/gameover.png').convert_alpha()
end_screen = pygame.transform.scale2x(end_screen)
end_screen_rect = end_screen.get_rect(center = (216, 520))

#start game screen
start_screen = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/message.png').convert_alpha()
start_screen = pygame.transform.scale2x(start_screen)
start_screen_rect = start_screen.get_rect(center = (216, 384))

#floor
floor = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

#bird
bird0 = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/doge11.png').convert_alpha()
#bird = pygame.transform.scale2x(bird0)
bird0_rect = bird0.get_rect(center = (100,250))
bird1 = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/doge22.png').convert_alpha()
#bird = pygame.transform.scale2x(bird)
bird1_rect = bird1.get_rect(center = (100,250))
bird = bird0
bird_rect = bird0_rect

#pipeline
pipe_surface = pygame.image.load('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

#create timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)

#Font
game_font = pygame.font.Font('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/04B_19.ttf', 40)
game_font2 = pygame.font.Font('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/04B_19.ttf', 17)
game_font3 = pygame.font.Font('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/04B_19.ttf', 20)

#Music
flap_sound = pygame.mixer.Sound('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/sound/sfx_wing.wav')
hit_sound = pygame.mixer.Sound('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('C:/Python/Dunglailaptrinh_Python/Flappy_Lord_PYGAME/FileGame/sound/sfx_point.wav')
countdown = 100

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				start = True

	#background
	if count >= 0 and count < 26:
		screen.blit(bg,(0,0))
	if count >= 26 and count < 60:
		screen.blit(bg1,(0,0))
	if count >= 60 and count < 88:
		screen.blit(bg2,(0,0))
	if count >= 88:
		screen.blit(bg3,(0,0))
	if count == 130:
		count = 0
	
	#floor
	floor_x_pos -= 1
	if floor_x_pos == -240:
		floor_x_pos = 0
	screen.blit(floor,(floor_x_pos,600))

	screen.blit(start_screen, start_screen_rect)

	guide = game_font2.render(f'Click mouse to start', False, (255,255,255))
	guide_rect = guide.get_rect(center = (216,690))
	screen.blit(guide, guide_rect)

	guide = game_font3.render(f'Press SPACE to jump', False, (255,255,255))
	guide_rect = guide.get_rect(center = (216,725))
	screen.blit(guide, guide_rect)

	if start == True: break

	pygame.display.update()
	clock.tick(120)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and game_active:
				bird_movement = 0
				bird_movement = -8
				count += 1
				flap_sound.play()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1 and game_active == False:
				score = 0
				game_active = True
				pipe_list.clear()
				if count%2 == 0:
					bird_rect = bird1_rect
					bird = bird1
				if count%2 == 1:
					bird_rect = bird0_rect
					bird = bird0
				bird_rect.center = (100,250)
				bird_movement = 0
		if event.type == spawnpipe:
			pipe_list.extend(create_pipe())

	#background
	if count >= 0 and count < 26:
		screen.blit(bg,(0,0))
	if count >= 26 and count < 60:
		screen.blit(bg1,(0,0))
	if count >= 60 and count < 88:
		screen.blit(bg2,(0,0))
	if count >= 88:
		screen.blit(bg3,(0,0))
	if count == 130:
		count = 0

	if game_active:
		#pipe
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)
		
		#bird
		bird_movement += gravity
		bird_rect.centery += bird_movement
		rotated_bird = rotate_bird(bird)
		screen.blit(rotated_bird, bird_rect)
		score += 0.008
		if int(score)%10 == 0 and int(score) > 0:
			score_sound.play()
		if score > high_score:
			high_score = score
		#check
		game_active = check(pipe_list)
		#score music
	
	#floor
	floor_x_pos -= 1
	if floor_x_pos == -240:
		floor_x_pos = 0
	screen.blit(floor,(floor_x_pos,600))

	score_display(game_active)

	if game_active == False:
		screen.blit(end_screen, end_screen_rect)
		guide = game_font2.render(f'Click mouse to continue', False, (255,255,255))
		guide_rect = guide.get_rect(center = (216,690))
		screen.blit(guide, guide_rect)

	pygame.display.update()
	clock.tick(120)

pygame.quit()
