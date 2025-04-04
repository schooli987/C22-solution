import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Pymunk Space Setup
space = pymunk.Space()
space.gravity = (0, 900)
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Load Images
bird_image = pygame.image.load('bird.png')
background_image = pygame.image.load('background.jpg')


# Resize Images
background_image = pygame.transform.scale(background_image, (800, 600))
bird_image = pygame.transform.scale(bird_image, (40, 40))


# Create Bird
def create_bird(x, y):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
    body.position = x, y
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.8
    shape.friction = 0.5
    space.add(body, shape)
    return body, shape

bird_body, bird_shape = create_bird(150, 500)


# Draw function
def draw_objects():
    
    screen.blit(background_image, (0, 0))  # Draw Background

    # Draw Bird
    bird_pos = bird_body.position
    screen.blit(bird_image, (bird_pos.x - 20, bird_pos.y - 20))

    # Draw Ground
   # pygame.draw.line(screen, (0, 0, 0), (0, 580), (800, 580), 5)

# Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    space.step(1 / 60.0)
    draw_objects()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
