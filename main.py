import math
import matplotlib.pyplot as plt
import numpy as np


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
    R1 = 2
    RES1 = 0.7
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
            ax.scatter3D(xTerm, yTerm, zTerm);
            print(xTerm, yTerm, zTerm)

    ax.set_xlim3d(-DIM, DIM)
    ax.set_ylim3d(-DIM, DIM)
    ax.set_zlim3d(-DIM, DIM)
    plt.show()
if __name__ == '__main__':
    #Check first intuitions function for explanation on how to get started thinking about this
    first_intuitions()