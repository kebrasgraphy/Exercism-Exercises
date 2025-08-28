def equilateral(sides):
    side1, side2, side3 = sides

    return (side1 == side2 and side2 == side3 and side1 == side3) and 0 not in sides


def isosceles(sides):
    side1, side2, side3 = sides
    is_triangle = False
    triangle_inequality = False
    is_equilateral = (side1 == side2 == side3 != 0)
    is_scalene = side1 != side2 and side2 != side3 and side1 != side3
    
    if (side1 == side2 >= side3) or (side1 == side3 >= side2) or (side2 == side3 >= side1):
        is_triangle = True

    if (side1 + side2 > side3) or (side1 + side3 > side2) or (side2 + side3 > side1):
        triangle_inequality = True
    
    return (is_triangle and triangle_inequality) or (is_equilateral and not is_scalene)


def scalene(sides):
    side1, side2, side3 = sides
    none_equal = side1 != side2 and side1 != side3 and side2 != side3
    
    triangle_inequality = False
    if side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2:
        triangle_inequality = True
    
    return none_equal and triangle_inequality
    