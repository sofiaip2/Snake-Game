import sys, pygame, random, os

pygame.init()

size = width, height = 1000, 750
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode(size)

blue = (0, 0, 255)
red = (225, 0, 0)
black = (0, 0, 0,)
white = (255, 255, 255)

xpos = 500
ypos = 375

snake_speed = 30
block_size = 20

score = 0

targetx = round(random.randrange(0, width -block_size) / 10.0) * 10.0
targety = round(random.randrange(0, height - block_size) / 10.0) * 10.0

snake_list = []
snake_length = 1

clock = pygame.time.Clock()

def snake(screen, color, snake_list, block_size):
    for x, y in snake_list:
        pygame.draw.rect(screen, color, [x, y, block_size, block_size])

while 1:
    screen.fill((black))
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    key = pygame.key.get_pressed()

    if (key[pygame.K_LEFT]):
        xpos -= block_size
    elif (key[pygame.K_RIGHT]):
        xpos += block_size
    elif (key[pygame.K_UP]):
        ypos -= block_size
    elif (key[pygame.K_DOWN]):
        ypos += block_size

    if xpos >= width or xpos < 0 or ypos >= height or ypos < 0:
        print("You lost! Score: " + str(score))
        sys.exit()

    pygame.draw.rect(screen, red, [targetx, targety, block_size, block_size])
    head = []
    head.append(xpos)
    head.append(ypos)
    snake_list.append(head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    for k in snake_list[:-1]:
        if k == head:
            print("You lost! Score: " + str(score))
            sys.exit()
    snake(screen, blue, snake_list, block_size)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    my_font = pygame.font.SysFont("Times New Roman", 18)
    score_display = my_font.render("Score: " + str(score), 1, (250, 250, 250))
    screen.blit(score_display, (30, 30))

    pygame.display.update()

    x = abs(targetx - xpos) <= 20
    y = abs(targety - ypos) <= 20

    if x and y:
        score += 1
        targetx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        targety = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        snake_length += 1
    clock.tick(snake_speed)

    pygame.display.update()