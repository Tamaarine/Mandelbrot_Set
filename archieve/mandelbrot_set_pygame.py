import pygame
import pygame.gfxdraw

# Initialize pygame
pygame.init()

# Set up the drawing window, 500x500
screen = pygame.display.set_mode((500, 500))

# Boolean to keep track of whether or not the game should be running
running = True

MAX_ITERATION = 80

def mandelbrot(c):
    '''
    We define the function mandelbrot to help us determine how many iteration it will take for
    the complex numebr c go out of bound in the function
    z{0} = 0
    z{n+1} = z{n} + c
    '''
    
    z = 0 # z will be used for recycling through the function
    n = 0 # n will be keeping track the number of iteration we have been through so far
    
    while abs(z) <= 2 and n < MAX_ITERATION:
        z = z*z + c # Do the calculation of z{n} + c
        n += 1 # Increment the iteration
    # We just return the n the higher the iteration is the more likely you are in the mandelbrot set
    return n
    
    
def render_mandelbrot():
    
    
    
if __name__ == '__main__':
    
    RE_START = -2
    RE_END = 1
    IM_START = 1
    IM_END = -1
    
    clock = pygame.time.Clock()
    
    screen.fill((255, 255, 255))
        
    # for x in range(500):
    #     for y in range(500):
    #         complex_num = complex(RE_START + (x / 500) * (RE_END - RE_START),
    #                                 IM_START + (y / 500) * (IM_END - IM_START))
            
    #         iteration = mandelbrot(complex_num)
            
    #         color = 255 - int(iteration * 255 / MAX_ITERATION)

            
    #         pygame.gfxdraw.pixel(screen, x, y, (color, color, color))
            
    while running:
        
        # Getting the event from user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("Mouse button pressed")    
            
        pygame.display.update()
        
    pygame.quit()