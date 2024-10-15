# Imports
import pymunk.pygame_util
import pymunk, pygame, math

# Initializing pygame
pygame.init()

# The window props
WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Draw Function
def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()  # Update the display after drawing

def c_ball(space, radius, mass): # Creates Ball
    body = pymunk.Body()
    body.position = (300, 300)
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100) # 4th is transparency
    space.add(body, shape) # shape is attatched to body, so shape cannot be added alone, body can.
    return shape

# Run Function
def run(window, WIDTH, HEIGHT):
    run = True
    clock = pygame.time.Clock()
    fps = 60

    space = pymunk.Space()
    space.gravity = (0, 981)  # Gravity should be a tuple (x, y)

    ball = c_ball(space, 30, 10)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Step the physics engine forward in time
        space.step(1 / fps) # 1 / fps is Delta Time

        # Drawing objects
        draw(space, window, draw_options)

        clock.tick(fps)
    
    pygame.quit()

# So run cannot be imported into other script and called there.
if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)  # Pass the required arguments to the run function
