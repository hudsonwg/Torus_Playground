import math
import matplotlib.pyplot as plt
import numpy as np
import pygame
from matplotlib import animation


def first_intuitions():
    '''
    FIRST THOUGHTS FOR THE LINEAR ALGEBRA
    - we want to create a donut, let's consider it to be a circle of some radius, rotated across a central axis and displaced some second radius (R2)
    - We can achieve this by sweeping a function across theta=[0,2pi] and phi = [0, 2pi]
    - my first intuition is to accomplish this with a simple nested loop across the ranges of phi and theta, plugging into a function, but what function?
    - turns out you can just use linear algebra, first generate the equation for the circle, then pass it through a transformation matrix (in this case a rotation)
    - the simplified dotted multiplication of this transform on the vector equation for the circle outputs the 3d figure
    - this is illustrated through the slow but functional demo below in which I looped and then plotted the points in a 3d numpy space
    '''
    # R2 is radius of torus rotation
    # R1 is radius of circle within torus
    DIM = 10
    R2 = 8
    R1 = 4
    RES1 = 0.4
    RES2 = 0.2
    # EQUATION FOR CIRCLE COMPONENT OF TORUS IS R2 + R1cos(i), R1sin(i), 0) it is a circle offset by some central radius R2
    # NOT ROTATE IT ABOUT AN AXIS OF ROTATION
    ax = plt.axes(projection='3d')
    for theta in np.arange(0, math.pi * 2, RES1):
        for phi in np.arange(0, math.pi * 2, RES2):
            # plt.plot(y*math.sin(theta)+x*math.cos(theta), math.sin(theta)*(-1)*x + math.cos(theta)*y, 'ro')
            # plt.plot(3, 2, 1, 'ro')
            xTerm = (R2 + R1 * math.cos(theta)) * math.cos(phi)
            yTerm = R1 * math.sin(theta)
            zTerm = -1 * (R2 + R1 * math.cos(theta)) * math.sin(phi)
            ax.scatter3D(xTerm, yTerm, zTerm, color='black');
            print(xTerm, yTerm, zTerm)

    ax.set_xlim3d(-DIM, DIM)
    ax.set_ylim3d(-DIM, DIM)
    ax.set_zlim3d(-DIM, DIM)
    plt.show()
def generate_frame(A, B):
    # R2 is radius of torus rotation
    # R1 is radius of circle within torus
    DIM = 10
    R2 = 8
    R1 = 4
    RES1 = 0.4
    RES2 = 0.2
    # EQUATION FOR CIRCLE COMPONENT OF TORUS IS R2 + R1cos(i), R1sin(i), 0) it is a circle offset by some central radius R2
    # NOT ROTATE IT ABOUT AN AXIS OF ROTATION
    returnFrame = []
    #A = 0.2
    #B = 0.2
    K1 = 4
    K2 = 4
    for theta in np.arange(0, math.pi * 2, RES1):
        for phi in np.arange(0, math.pi * 2, RES2):
            # plt.plot(y*math.sin(theta)+x*math.cos(theta), math.sin(theta)*(-1)*x + math.cos(theta)*y, 'ro')
            # plt.plot(3, 2, 1, 'ro')
            t1 = R2 + R1*math.cos(theta)
            xTerm = t1 * (math.cos(B)*math.cos(phi) + math.sin(A)*math.sin(B)*math.sin(phi)) - R1*math.cos(A)*math.sin(B)*math.sin(theta)
            yTerm = t1 * (math.cos(phi)*math.sin(B) - math.cos(B)*math.sin(A)*math.sin(phi)) + R1*math.cos(A)*math.cos(B)*math.sin(theta)
            zTerm = math.cos(A)*(R2+R1*math.cos(theta))*math.sin(phi) + R1*math.sin(A)*math.sin(theta)

            #NOW CONVERT TO 2D POINT WITH DIMENSION REDUCTION EQUATION
            pair = [(K1*xTerm)/(K2+zTerm), (K1*yTerm)/(K2+zTerm)]
            returnFrame.append([xTerm, yTerm, zTerm])
    print(returnFrame)
    return returnFrame
def generateFramesDemo():
    DIM = 15
    for A in np.arange(0, 2 * math.pi, 0.1):
        data = generate_frame(A, A)
        for x in data:
            plt.scatter(x[0], x[1], color='black')
        plt.xlim(-DIM, DIM)
        plt.ylim(-DIM, DIM)
        plt.show()

def generateAnimation():
    FPS = 15
    width = 1000
    height = 1000
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("First Game")
    x = 50
    y = 50
    vel = 5

    def redrawGameWindow():
        white = (255, 255, 255)
        yellow = (255, 255, 0)
        green = (0, 255, 255)
        orange = (255, 100, 0)
        Font = pygame.font.SysFont('timesnewroman', 30)
        DIM = 15
        for A in np.arange(0, 2 * math.pi, 0.1):

            win.fill((0, 0, 0))  # <--- this is missing
            data = generate_frame(A, A)
            for x in data:
                #plt.scatter(x[0], x[1], color='black')
                #DRAW TO COORDINATE
                win.blit(Font.render(".", False, (255, 255, 255)), (20*x[0] + width/2, 20*x[1] + height/2))
            pygame.time.Clock().tick(FPS)
            pygame.display.update()
    run = True
    while run:
        #pygame.time.delay(100)
        #DRAW ANIMATION HERE
        redrawGameWindow()
    pygame.quit()

if __name__ == '__main__':
    #Check first intuitions function for explanation on how to get started thinking about this
    #first_intuitions()
    #now generate set of tuples with generate frame
    #generateFramesDemo()
    generateAnimation()


