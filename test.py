#!/usr/bin/env python3

# Created By: Titwech Wal
# Date:may 20. 2022
# program tells user the radius of a
# sphere with their input


from colorama import Fore
import math


def calc_surface_area(radius):

    # calaculae area
    suface_area = 4 * math.pi * radius ** 2

    return suface_area


def calc_diameter(radius_dia):

    # calcuate diameter
    diameter = 2 * radius_dia

    return diameter


def main():

    # get the input from the user
    radius_str = input("Enter a number for the radius: ")
    radius_dia_str = input("Enter the number for the diameter: ")
    print("")

    try:
        # input to int
        radius_float = float(radius_str)
        radius_dia_float = float(radius_dia_str)

        if radius_float > 0 and radius_dia_float > 0:

            # call the function above
            area = calc_surface_area(radius_float)
            sphere_diameter = calc_diameter(radius_dia_float)

            print(Fore.GREEN + "The surface area of a shpere is {:,.2f} cm."
                  . format(area))

            print(Fore.GREEN + "And the diameter of a shpere is {:,.2f} cm."
                  . format(sphere_diameter))

        else:
            print(Fore.RED + "Enter a postive number")

    except Exception:
        print(Fore.RED + "Please enter a vaild number.")


if __name__ == "__main__":
    main()
