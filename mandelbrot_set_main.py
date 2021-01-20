# Import statements
import pygame
import threading

# We are going to make a class that will have everything about mandelbrot set about it in it
class MandelbrotSet:
    
    def __init__(self):
        # Variables that define the range of the graph that the mandelbrot is being plotted on
        self.RE_START = -2
        self.RE_END = 1
        self.IM_START = 1
        self.IM_END = -1
        self.WIDTH = 1080
        self.HEIGHT = 720
        self.MAX_ITERATION = 200
        
        # We also init pygame here
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        
        # Set up some variables for the zoom in square that we are going to be using
        self.ZOOMSQUARE_WIDTH = 100
        self.ZOOMSQUARE_HEIGHT = 100
        
        
    def mandelbrot(self, c):
        '''
        We define the function mandelbrot to help us determine how many iteration it will take for
        the complex numebr c go out of bound in the function
        z{0} = 0
        z{n+1} = z{n} + c
        
        This is the main calculation function to doing the mandelbrot set
        '''
    
        z = 0 # z will be used for recycling through the function
        n = 0 # n will be keeping track the number of iteration we have been through so far
        
        while abs(z) <= 2 and n < self.MAX_ITERATION:
            z = z*z + c # Do the calculation of z{n} + c
            n += 1 # Increment the iteration
            
        # We just return the n the higher the iteration is the more likely you are in the mandelbrot set
        return n
        
        
    def render_mandelbrot(self):
        '''
        This function will render the mandelbrot set using the current defined variable through pygame
        '''
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                # First we turn the pixel into coordinate on the plane
                
                # The formula basicallys make each pixel into a percentage out of 500
                # and be multiplied by the range. So x_cord and y_cord will be RE_START to RE_END
                # and IM_START to IM_END depending on the x and y value
                x_cord = self.RE_START + (x / self.WIDTH) * (self.RE_END - self.RE_START)
                y_cord = self.IM_START + (y / self.HEIGHT) * (self.IM_END - self.IM_START)
                
                # Calling the mandelbrot function to calculation how many iteration it will take
                # for the point to be remain bounded or escape
                iteration = self.mandelbrot(complex(x_cord, y_cord))                
                
                # This formula basically maps the iteration to a color.
                # If the iteration is the MAX_ITERATION. Say 80, then iteration and MAX_ITERATION
                # will cancel out. Making it 255 - 255 which equals to 0. And that color is black in RGB
                # However, if the iteration is 0 meaning that it escaped immediately, then it will be white
                color = 255 - int(iteration * 255 / self.MAX_ITERATION)
                
                # Then we will draw using pygame
                self.screen.set_at((x, y), (color, color, color))
                
            # After drawing a row update it
            pygame.display.update()
                
        
    def update_self_variables(self):
        
        mouse_coordinte = pygame.mouse.get_pos()
        
        range_diff_x = self.RE_END - self.RE_START
        range_diff_y = self.IM_END - self.IM_START
        
        # We begin to update the variables set for rendering the mandelbrot set
        newReStart = self.RE_START + ((mouse_coordinte[0] - self.ZOOMSQUARE_WIDTH / 2) / self.WIDTH) * range_diff_x
        newReEnd = self.RE_START + ((mouse_coordinte[0] + self.ZOOMSQUARE_WIDTH / 2) / self.WIDTH) * range_diff_x
        
        newImStart = self.IM_START + ((mouse_coordinte[1] - self.ZOOMSQUARE_HEIGHT / 2) / self.HEIGHT) * range_diff_y
        newImEnd = self.IM_START + ((mouse_coordinte[1] + self.ZOOMSQUARE_HEIGHT / 2) / self.HEIGHT) * range_diff_y
        
        self.RE_START = newReStart
        self.RE_END = newReEnd
        self.IM_START = newImStart
        self.IM_END = newImEnd
        


# Entrance to our program
if __name__ == "__main__":
    
    # Variable used to stop if the pygame program is exited
    running = True 
    
    # We make our Mandelbrotset class object here
    mandelbrot_app = MandelbrotSet()
    
    # Make a separate initial thread that will render the mandelbrot for the first time.
    # This way then we can still press the x button while it is rendering, otherwise it will freeze up everything
    # until the mandelbrot is finish rendering
    first_render_thread = threading.Thread(target=mandelbrot_app.render_mandelbrot, daemon=True)
    
    # Starting the thread
    first_render_thread.start()
        
    # A loop to keep track of the event from user
    while running:
        
        # Getting the event from the user
        for event in pygame.event.get():
            
            # If the event is QUIT then we simply make the running false and stop the update
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # If the application is clicked, update the variables
                mandelbrot_app.update_self_variables()
                
                # Then we have to render the mandelbrot set again using the newly defined variable
                rendering_thread = threading.Thread(target=mandelbrot_app.render_mandelbrot, daemon=True)
                rendering_thread.start()
        
        pygame.display.update()
    
    # If we are here then we will quit pygame
    pygame.quit()