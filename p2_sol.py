import rbm
import math
import p1_sol
import numpy as np

# By Trey Castle

"""These three functions receive a value, then takes that and inserts it
into the proper location in the matrix to move it along the respective axes"""


def translate_x(val):
    trans = np.array([[1, 0, 0, val],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return trans


def translate_y(val):
    trans = np.array([[1, 0, 0, 0],
                    [0, 1, 0, val],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return trans


def translate_z(val):
    trans = np.array([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, val],
                    [0, 0, 0, 1]])
    return trans


"""these three functions receive a theta value and constructs a matrix which can
be used to rotate a frame around a given axis"""


def rotate_x(theta):
    rot = np.array([[1, 0, 0, 0],
                    [0, math.cos(theta), -math.sin(theta), 0],
                    [0, math.sin(theta), math.cos(theta), 0],
                    [0, 0, 0, 1]])
    return rot


def rotate_y(theta):
    rot = np.array([[math.cos(theta), 0, -math.sin(theta), 0],
                    [0, 1, 0, 0],
                    [-math.sin(theta), 0, math.cos(theta), 0],
                    [0, 0, 0, 1]])
    return rot


def rotate_z(theta):
    rot = np.array([[math.cos(theta), -math.sin(theta), 0, 0],
                    [math.sin(theta), math.sin(theta), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return rot


