import pygame
import physics_objects

pygame.init()
clock = pygame.time.Clock()
# Screen dimensions
screen_width, screen_height = 1080, 649

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

physics_group_1 = pygame.sprite.Group()

physics_objects.physics_box(physics_group_1,
                            mass =534,
                            position = (screen_width/2,screen_height/2),
                            image = pygame.Surface((100,100)),
                            gravity = False,
                            boundaries = True,
                            movement = True,
                            air_resistance=False,
                            initial_velocity = (0,0),
                            constant_force=(1000,0),
                            type_of_motion = "SHM")
# Main loop

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit event
            run = False
    # Fill the screen with a color (optional, e.g., white)
    screen.fill((255, 255, 255))
    

    physics_group_1.update()
    physics_group_1.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

