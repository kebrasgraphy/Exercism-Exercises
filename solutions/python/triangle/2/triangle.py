def triangle_inequality(sides):
    side1, side2, side3 = sides
    
    return side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2


def not_zero(sides):
    side1, side2, side3 = sides

    return side1 != 0 and side2 != 0 and side3 != 0


def equal_sides(sides):
    side1, side2, side3 = sides
    
    return side1 == side2 == side3


def equilateral(sides):
    side1, side2, side3 = sides
    
    return equal_sides(sides) and not_zero(sides)
    

def scalene(sides):
    side1, side2, side3 = sides
    none_equal = side1 != side2 and side1 != side3 and side2 != side3
        
    return triangle_inequality(sides) and not equilateral(sides) and none_equal
   

def isosceles(sides):
    side1, side2, side3 = sides
    two_equal = side1 == side2 or side1 == side3 or side2 == side3
    
    return triangle_inequality(sides) and not_zero(sides) and two_equal