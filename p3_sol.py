import rbm
import math
import p2_sol
import numpy as np

"""By Trey Castle"""


def H_1():
    a = p2_sol.translate_x(2.5)
    b = p2_sol.translate_z(0.5)
    c = p2_sol.translate_y(-1.5)
    # get dot product of a and post multiplied b
    var = np.dot(a, b)
    # post multipy c
    var = np.dot(var, c)
    return var

def H_2():
    a = p2_sol.translate_z(0.5)
    b = p2_sol.translate_x(2.5)
    c = p2_sol.translate_y(-1.5)
    # post multiply b on a
    var = np.dot(a, b)
    # post multiply c
    var = np.dot(var, c)
    return var

def H_3():
    a = p2_sol.translate_x(2.5)
    b = p2_sol.translate_z(0.5)
    c = p2_sol.translate_y(-1.5)
    # pre multiply c on b
    var = np.dot(c, b)
    # pre multiply the previous product on a
    var = np.dot(var, a)
    return var


def H_4():
    a = p2_sol.translate_z(0.5)
    b = p2_sol.translate_x(2.5)
    c = p2_sol.translate_y(-1.5)
    # pre multiply c on b
    var = np.dot(c, b)
    # pre multiply the previous product on a
    var = np.dot(var, a)
    return var


def H_5():
    # rotate by angle pi/2 about current x axis
    a = p2_sol.rotate_x(math.pi / 2)
    # translate 3 across current x axis
    b = p2_sol.translate_x(3)
    # post multiply b on a
    var = np.dot(a, b)
    # translate -3 across current z axis
    c = p2_sol.translate_z(-3)
    # post multipy c with the previous product
    var = np.dot(var, c)
    # rotate by angle -pi/2 about current z axis
    d = p2_sol.rotate_z((-1) * (math.pi / 2))
    # post multiplies d with previous product
    var = np.dot(var, d)
    return var


if __name__ == '__main__':
    np.set_printoptions(precision=5, suppress=True)
    print(H_1())
    print(H_2())
    print(H_3())
    print(H_4())
    print(H_5())