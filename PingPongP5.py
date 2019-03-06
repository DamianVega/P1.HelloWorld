import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = [1200, 650]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ping-Pong")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Speed of ball
circle_change_x = 2
circle_change_y = 2

rect_x = 1160
rect_y = 325
left_rect_x = 25
left_rect_y = 325
rect_change_x = 0
rect_change_y = 0
left_rect_change_x = 0
left_rect_change_y = 0
circle_x = 590
circle_y = 325
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rect_change_y -= 10
            elif event.key == pygame.K_DOWN:
                rect_change_y += 10
            elif event.key == pygame.K_s:
                left_rect_change_y += 10
            elif event.key == pygame.K_w:
                left_rect_change_y -= 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                rect_change_y = 0
            elif event.key == pygame.K_s or event.key == pygame.K_w:
                left_rect_change_y = 0

    circle_x += circle_change_x
    circle_y += circle_change_y

    rect_x += rect_change_x
    rect_y += rect_change_y
    left_rect_x += left_rect_change_x
    left_rect_y += left_rect_change_y

    if rect_y > 525 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 1100 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if left_rect_y > 525 or left_rect_y < 0:
        left_rect_change_y = left_rect_change_y * -1
    if left_rect_x > 1100 or left_rect_x < 0:
        left_rect_change_x = left_rect_change_x * -1

    if circle_y > 640 or circle_y < 10:
        circle_change_y = circle_change_y * -1
    if circle_x > 1190 or circle_x < 10:
        circle_change_x = circle_change_x * -1

    screen.fill(BLACK)
    left = pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 15, 125])
    right = pygame.draw.rect(screen, WHITE, [left_rect_x, left_rect_y, 15, 125])
    ball = pygame.draw.circle(screen, WHITE, (circle_x, circle_y), 10, 0)

    if left.colliderect(ball):
        circle_change_x = circle_change_x * -1
    if right.colliderect(ball):
        circle_change_x = circle_change_x * -1

    clock.tick(60)

    pygame.display.flip()