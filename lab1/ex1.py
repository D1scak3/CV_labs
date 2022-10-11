
import pygame as pg
from pygame.locals import *
from OpenGL.GL import *


if __name__ == "__main__":
    
    # initialise window 
    pg.init()

    # set window size
    windowsize = (640, 480)
    
    # generate window
    pg.display.set_mode(windowsize, DOUBLEBUF | OPENGL | RESIZABLE)

    # define window color
    glClearColor(0.0, 1.0, 0.0, 1.0)

    # something

    # start event handler cycle
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            
            # it allows to change buffers, since OpenGL uses 2 buffers
            # to make rendering faster
            glClear(GL_COLOR_BUFFER_BIT)   # send everything from buffers to gpu
            pg.display.flip()   # switch buffers
