"""
Module calcul_v_sphere(r)

functions.py
"""
# from func_volumes import calcul_v_box - using 1 func from func_volumes file
# imports all function from func_volumes
import func_volumes as fv


def main():
    # prints the functions.py
    print('volume of a sphere ', fv.calcul_v_sphere(10))
    # print('vol of a box ', calcul_v_box(length = 2, w = 3, h = 5)) or ->
    print('vol of a box ', fv.calcul_v_box(2, 3, 5))


if __name__ == '__main__':
    main()
