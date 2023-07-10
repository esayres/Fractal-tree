# ###############################################
# A fractal tree using pygame and trigonometry
#
# by Elijah Sayres
#
# ###############################################

import pygame
from math import cos, radians, sin

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 980))
clock = pygame.time.Clock()
running = True
starting_log = pygame.Vector2(screen.get_width() / 2, 980)

##########################
# FRACTAL TREE BUILDING
##########################

try:
    def right_branch(length, x, y, starting_point_branch, angle, amount_of_branches):
        if length < amount_of_branches:
            # prevents freezing of the window and allows you to quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            return
        starting_branch = starting_point_branch

        # It calculates the change in x and y coordinates (Dx and Dy) based on the length and angle using trigonometric functions
        Dx = length * cos(radians(angle))
        Dy = length * sin(radians(angle))

        pygame.draw.line(screen, "white", starting_branch, (x + Dx, y - Dy))
        pygame.time.delay(85)
        pygame.display.update()

        length *= 0.67  # shortens length of branch by 2/3
        starting_branch = (x + Dx, y - Dy)  # moves where the starting point of the drawing line should be

        # changes the x, y to move to next new point
        x += Dx
        y -= Dy

        # uses recursion to call the function again. once with an angle of decreased by 45 and again with an angle increased by 45 degrees
        right_branch(length, x, y, starting_branch, angle - 45, amount_of_branches)
        right_branch(length, x, y, starting_branch, angle + 45, amount_of_branches)


    def left_branch(length, x, y, starting_point_branch, angle, amount_of_branches):
        if length < amount_of_branches:
            # prevents freezing of the window and allows you to quit window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            return
        starting_branch = starting_point_branch
        # It calculates the change in x and y coordinates (Dx and Dy) based on the length and angle using trigonometric functions
        Dx = length * cos(radians(angle))
        Dy = length * sin(radians(angle))

        pygame.draw.line(screen, "white", starting_branch, (x - Dx, y - Dy))
        pygame.time.delay(85)
        pygame.display.update()

        length *= 0.67  # shortens length of branch by 2/3
        starting_branch = (x - Dx, y - Dy)  # moves where the starting point of the drawing line should be

        # changes the x, y to move to next new point
        x -= Dx
        y -= Dy

        # uses recursion to call the function again. once with an angle of decreased by 45 and again with an angle increased by 45 degrees
        left_branch(length, x, y, starting_branch, angle - 45, amount_of_branches)
        left_branch(length, x, y, starting_branch, angle + 45, amount_of_branches)


    #######################
    # MAIN PYGAME LOOP
    #######################

    # Branch Variables
    length = 150  # Changing Length variable changes how long the Branches will be in the Tree
    x_point = 600
    y_point = 600
    branch_starting_endpoint_cords = (600, 700)
    angle = 45  # the angle at which the branches are placed (45 degrees)
    amount_of_branches = 10  # Changing Amount of branches changes how many branches will be drawn on to the tree

    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        pygame.draw.line(screen, "white", starting_log, (screen.get_width() / 2, 700))
        pygame.display.flip()

        # the functions that draw the right branches and the left branches of the Fractal tree
        right_branch(length, x_point, y_point, branch_starting_endpoint_cords, angle, amount_of_branches)
        left_branch(length, x_point, y_point, branch_starting_endpoint_cords, angle, amount_of_branches)

        pygame.time.delay(1600)  # delays how long the tree will show before redrawing from the start
        clock.tick(60)  # limits FPS to 60

    pygame.quit()

except pygame.error:
    pass
