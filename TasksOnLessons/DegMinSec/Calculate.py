from math import pi
from math import floor
def deg_to_gms(deg, formats='string'):
    min = (deg - floor(deg)) * 60
    sec = (min - floor(min)) * 60
    return floor(deg), floor(min), sec

def gms_to_deg(deg, min, sec):
    return deg + min/60 + sec/3600

def deg_to_rad(deg):
    return deg * (pi / 180)

def rad_to_deg(rad):
    return rad * (180 / pi)

if __name__=='__main__':
    print(deg_to_gms(45.23))
    print(gms_to_deg(45, 13, 48))
    print(deg_to_rad(45.23))
    print(rad_to_deg(deg_to_rad(45.23)))