# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "red", player_pos + pygame.Vector2(130, 0), 40)
    pygame.draw.line(screen, "black", player_pos, player_pos + pygame.Vector2(70, 0), 10)
    pygame.draw.line(screen, "black", player_pos, player_pos + pygame.Vector2(30, -70), 10)
    pygame.draw.line(screen, "black", player_pos + pygame.Vector2(30, -70), player_pos + pygame.Vector2(100, -70), 10)

    # Check if player out of screen (left,right,top,down)
    if player_pos.x < 0 or player_pos.x > screen.get_width() or player_pos.y < 0 or player_pos.y > screen.get_height():
        # Print arrow in that direction on the edge of the screen
        edge_pos = pygame.Vector2(player_pos)
        if player_pos.x < 0:
            edge_pos.x = 0
        elif player_pos.x > screen.get_width():
            edge_pos.x = screen.get_width()
        if player_pos.y < 0:
            edge_pos.y = 0
        elif player_pos.y > screen.get_height():
            edge_pos.y = screen.get_height()
        pygame.draw.circle(screen, "white", edge_pos, 5)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
