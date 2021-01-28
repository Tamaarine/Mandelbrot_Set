# from tkinter import *
from PIL import Image, ImageDraw

# Define the variable of max_iteration which is the max number of times of iteration we reach before stopping
max_iter = 200

def mandelbrot(c):
    '''
    We define the function mandelbrot to help us determine how many iteration it will take for
    the complex numebr c go out of bound in the function
    z{0} = 0
    z{n+1} = z{n} + c
    '''
    
    z = 0 # z will be used for recycling through the function
    n = 0 # n will be keeping track the number of iteration we have been through so far
    
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c # Do the calculation of z{n} + c
        n += 1 # Increment the iteration
    # We just return the n the higher the iteration is the more likely you are in the mandelbrot set
    return n
    
if __name__ == '__main__':
    
    # Define the resolution of our image
    WIDTH = 1080
    HEIGHT = 720
    
    scale = 0.01
    
    # r(x - h) + k
    # h is the horizontal shifts
    # k is the vertical shifts
    h = 25
    k = 0
    
    # Define the area 
    RE_START = scale * (-2 + h)
    RE_END =  scale * (1 + h)
    IM_START = scale * (-1 - k)
    IM_END = scale * (1 - k)
    
    im = Image.new('RGB', (WIDTH, HEIGHT), (0,0,0))
    draw = ImageDraw.Draw(im)
    
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            # First we create our complex number using the pixels
            complex_num = complex(RE_START + (i / WIDTH) * (RE_END - RE_START),
                                  IM_START + (j / HEIGHT) * (IM_END - IM_START))
                                  
            iteration = mandelbrot(complex_num)
            
            # Then we will color the point based on the number of iteration
            col = 255 - int(iteration * 255 / max_iter)
            
            draw.point([i, j], (col, col, col))
            
    im.save('./output1.png', 'PNG')








'''
# The root of our application
root = Tk()

# Centering the window
win_width = 1080
win_height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cord = int((screen_width/2) - (win_width/2))
y_cord = int((screen_height/2) - (win_height/2))

root.geometry("{}x{}+{}+{}".format(win_width, win_height, x_cord, y_cord))


# Making a canvas so we can draw on it
canvas = Canvas(root, width=win_width, height=win_height, bg='white')
canvas.pack()

# Draws the x axis
canvas.create_line(0, win_height/2, win_width,win_height/2,width=2)
canvas.create_line(win_width/2, 0, win_width/2, win_height, width=2)



root.mainloop()
'''
