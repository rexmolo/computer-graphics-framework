import pygame
import sys
from core.input import Input

class Base(object) :
    def __init__(self, screenSize=[512, 512]) :
        # initialize all pygame modules
        pygame.init()
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        # pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        pygame.display.set_caption("Graphics Window")

        self.running = True
        self.clock = pygame.time.Clock()

        self.input = Input()

    def initialize(self) :
        pass

    def update(self) :
        pass

    def run(self) :
        # startup
        self.initialize()

        # main loop
        while self.running:
            # process input
            if self.input.quit:
                self.running = False

            # update
            self.update()
            #render
            pygame.display.flip()
            # pause if necessary to achieve 60 fps
            self.clock.tick(60)

        # shutdown
        pygame.quit()
        sys.exit()