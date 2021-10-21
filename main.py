import sys, pygame

pygame.init()

size = width, height = 1280, 720
width = 1280
height = 720
backgroud = pygame.image.load("./map/(name of the map)")
main_stabby = pygame.image.load("./characters_model/main_front_character.jpg")
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Island's Kingdom")
clock = pygame.time.Clock()
x =  (width * 0.45)
y = (height * 0.8)
x_change = 0

def movements(x, y):
    screen.blit(main_stabby, (x,y))
speed = [10 , 10]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit(0)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -2
        elif event.key == pygame.K_RIGHT:
            x_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    screen.fill(backgroud)
    pygame.display.flip()