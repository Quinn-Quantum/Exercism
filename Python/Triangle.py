def equilateral(sides):
    return sides[0] == sides[1] and sides[0] == sides[2] and sideslengt(sides) and sumOfTheLengths(sides)


def isosceles(sides):
   return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and sideslengt(sides) and sumOfTheLengths(sides) 


def scalene(sides):
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2] and sideslengt(sides) and sumOfTheLengths(sides)


def sideslengt(sides):
    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0

def sumOfTheLengths(sides):
   return sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]