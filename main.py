import pygame
for i in range(0, 10):
	print()
from pygame import Vector2
from particles import ParticleEmitter
import globals as gb
pygame.init()

doExit = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode(gb.SCREEN_SIZE)

fireFade = ParticleEmitter(
	pos = Vector2(gb.SCREEN_SIZE)//2,
	updateAttributes = [
		["dragOverLife", [.15, .2, .2, .2, .5, 1, 5]],
		["sizeOverVelo", [6.5, [5, 6, 7, 8, 9, 9]]],
		["gravity", .02],
		["randVelo", 2.5],
		["deleteOnColor", [(0, 0, 0), 15]],
		["colorOverVelo", [6.5, [(0, 0, 0), (50, 10, 100), (255, 75, 20), (255, 100, 50), (255, 125, 50), (255, 200, 75)]]],
	],
	initAttributes = [
		["randAngle"],
		["moveOnAngle", 1500],
		["randVelo", 900]
	],
	maxVelo = 15,
	maxVeloAdjust = 5,
	maxParticles = 1000,
	ppf = 7.5*2,
	particleLifetime = 1000,
	spawnType = "onMove",
	ppfMaxVelo = 2.5,
	threaded = True,
	maxThreads = 50
)

transLight = ParticleEmitter(
	updateAttributes = [
		["colorOverDistance", [250, [
			(91, 206, 250),
			(91, 206, 250),
			(0, 0, 0),
			(245, 169, 184),
			(245, 169, 184),
			(0, 0, 0),
			(255, 255, 255),
			(255, 255, 255),
			(0, 0, 0),
			(245, 169, 184),
			(245, 169, 184),
			(0, 0, 0),
			(91, 206, 250),
			(91, 206, 250),
			(12, 12, 12)
		]]],
		["sizeOverLife", [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0]],
		["deleteOnSize", [0, 1]],
	],
	initAttributes = [
		["randAngle"],
		["moveOnAngle", 35]
	],
	particleLifetime = 250,
	maxParticles = 1000,
	ppf = 5,
)

snow = ParticleEmitter(
	updateAttributes = [
		["gravity", .05],
		["randAdjustSize", [2, [1, 4.5]]],
		["randXVelo", 5]
	],
	initAttributes = [
		["randVelo", [75, 10]]
	],
	particleLifetime = 500,
	maxParticles = 1000,
	ppf = 5,
	cull = [False, True, True, True],
)

spiderverseCircles = ParticleEmitter(
	updateAttributes = [
		["randAdjustColor", [50, [(0, 0, 0), (255, 25, 255)]]],
		["deleteOnVelo", [0, .25]],
		["sizeOverVelo", [10, [0, 50]]],
		["drag"],
	],
	initAttributes = [
		["randColor"],
		["randYVelo", 200],
	]
)

flashlight = ParticleEmitter(
	updateAttributes = [
		["sizeOverDistance", [250, [10, 9, 0]]],
		["colorOverLife", [(255, 255, 150), (255, 255, 200), (200, 200, 150)]],
	],
	initAttributes = [
		["randAngle"],
		["moveOnAngle", 50],
	],
	maxParticles = 1000,
	particleLifetime = 250,
	ppf = 10,
)

testEmitter = ParticleEmitter(
	ppf = 10,
	maxParticles = 1000,
	updateAttributes = [
		# ["randColor", [None, "color"]]
	],
	initAttributes = [
		["randAngle"],
		["moveOnAngle", 20],
	],
	maxVelo = Vector2(20, 20),
	threaded=False
)

class TextDisplay:
	def __init__(self, text, x, y, font = None):
		if text == None: text = ""
		self.text = text
		self.x = x
		self.y = y
		self.font = font #not set up. don't use different fonts.

	def update(self, screen, text = "None"):
		if not text == "None":
			self.text = text
		font = pygame.font.Font(None, 74)
		renderedText = font.render(str(self.text), 1, (255, 255, 255))
		screen.blit(renderedText, (self.x, self.y))

fps = TextDisplay("", 10, 10)
numOfParticles = TextDisplay("", 10, 20+74)

while not doExit:
	delta = clock.tick(gb.FPS) / 1000
	
	# print(clock.get_fps(), fireFade.numOfParticles)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit parogram
	screen.fill((0, 0, 0))
	fps.update(screen, f"{int(clock.get_fps())}")
	numOfParticles.update(screen, f"{fireFade.numOfParticles}")

	# testEmitter.update(screen, delta, pos = pygame.mouse.get_pos(), velo = -Vector2(pygame.mouse.get_rel())/7.5)
	# transLight.update(screen, delta, pos = pygame.mouse.get_pos(), velo = -Vector2(pygame.mouse.get_rel())/7.5)
	# flashlight.update(screen, delta, pos = pygame.mouse.get_pos())
	fireFade.update(screen, delta, pos = pygame.mouse.get_pos(), velo = -Vector2(pygame.mouse.get_rel())/7.5)
	# snow.update(screen, delta, pos = Vector2(SCREEN_SIZE[0]//2, -100))
	# spiderverseCircles.update(screen, delta, pos = pygame.mouse.get_pos())

	pygame.display.flip()
pygame.quit()