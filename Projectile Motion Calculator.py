print("The launching angle is:")
a = float(input())

import numpy as np

def Range(angle,initial_height,initial_speed):
    
    angle_in_radian = (angle*np.pi/180)
    g = 981
    flying_range = np.sin(2*angle_in_radian)*initial_speed**2/g
    return flying_range

h = 108
v = 460

R = Range(a,h,v)
print("The range is:",R)

