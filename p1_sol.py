import rbm
import math
import numpy as np

# By Trey Castle


"""Function calls on RBM in order to perform a fixed frame rotation along all 3 axes
As they are fixed frame it multiplies them in the following order:
variable = Z rotation * Y Rotation * X Rotation"""
def roll_pitch_yaw(xr, yr, zr):
    np.set_printoptions(precision=5, suppress=True)
    # takes x input and gets a rotation matrix for it
    xt = rbm.rot_x(xr)
    # takes y input and gets a rotation matrix for it
    yt = rbm.rot_y(yr)
    # takes z input and gets a rotation matrix for it
    zt = rbm.rot_z(zr)
    var = np.matmul(yt, xt)
    var = np.matmul(zt, var)

    return var


if __name__ == '__main__':
    test = roll_pitch_yaw(math.pi/2, math.pi/2, math.pi/2)
    np.set_printoptions(precision=5, suppress=True)
    print(test)
