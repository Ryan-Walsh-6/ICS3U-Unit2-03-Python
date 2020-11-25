#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program finds the circumference of a circle
import constants


def main():
    # this program finds the circumference of a circle

    # input
    radius = int(input("Enter the radius of a circle (cm) :"))

    # process
    circumference = (constants.TAU*radius)

    # output
    print()
    print("circumference is {} cm.".format(circumference))


if __name__ == "__main__":
    main()
