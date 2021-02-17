import math


def calcul_v_box(length, w, h):
    return length * w * h


def calcul_v_sphere(r):
    """
    calculate the volume of a sphere
    """
    volume = 4/3 * math.pi * (r ** 3)
    return volume

