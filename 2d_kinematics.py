from roboticstoolbox import ET2
import robotictoolbox as rtb
import math

# Joint angles (rad)
pi = math.pi
q = [pi/6, 0.8]
a1 = 1
a2 = 1

# 2-DOF Robot using homogenous transformation matrices
T_01 = ET2.R(q[0], 'rad') * ET2.tx(a1)
T_02 = ET2.R(q[1], 'rad') * ET2.tx(a2)
T_02 = T_01 * T_02
K_2d= T_02.fkine([])
print("2-DOF planar robot (2D space) - FK")
print(K_2d)

# RR planar robot from library
robot1 = rtb.models.ETS.Planar2()
T = robot1.fkine(q)
print("2-DOF planar robot (library) - FK")
print(T)
robot1.plot(q, black=True)