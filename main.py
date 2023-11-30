# Importing Hell
import fractions
import math

# Quadratics #

# Factors a quadratic equation
def QuadraticFactorer(a, b, c):
    
    # Find the descriminant
    desc = (b*b)+(-4*a*c)

    # Check if the equation is solvable
    if desc < 0:
        raise Exception("This equation is not solvable. Maybe you have a typo in your values? :)")

    # Check if factorable
    if math.sqrt(desc).is_integer():
        print("Factorable")
        print(desc, math.sqrt(desc))
    else:
       raise Exception("This equation cannot be factored. Maybe you have a typo in your values? :)")

    # Find the roots
    root1 = fractions.Fraction((b + math.sqrt(desc))/(2*a))
    root2 = fractions.Fraction((b - math.sqrt(desc))/(2*a))
    print(root1, root2)

    # Factor the equation w/ the roots
    factored_equation = "("
    if root1.denominator == 1:
        factored_equation = factored_equation + "x"
    else:
        factored_equation = factored_equation + str(root1.denominator) + "x"
    if root1.numerator >= 0:
        factored_equation = factored_equation + "+" + str(root1.numerator)
    else:
        factored_equation = factored_equation + str(root1.numerator)
    factored_equation = factored_equation + ")("
    if root2.denominator == 1:
        factored_equation = factored_equation + "x"
    else:
        factored_equation = factored_equation + str(root2.denominator) + "x"
    if root2.numerator >= 0:
        factored_equation = factored_equation + "+" + str(root2.numerator)
    else:
        factored_equation = factored_equation + str(root2.numerator)
    factored_equation = factored_equation + ")"

    # Print out the now factored equation
    return factored_equation #(ax-b)(ax-b)

# Prints out info about the equation
def QuadraticInfo(a, b, c):
    # Find the descriminant
    desc = (b*b)+(-4*a*c)
    if desc < 0:
        raise Exception("This equation is unsolvable. Maybe there is a typo somewhere? The descriminant is", desc)
    
    # Find the roots
    root1 = fractions.Fraction((-b + math.sqrt(desc))/(2*a))
    root2 = fractions.Fraction((-b - math.sqrt(desc))/(2*a))
    
    # Formatting the equation
    if a >= 0:
        astr = str("+" + a)
    else:
        astr = str(a)
    if b >= 0:
        bstr = str("+" + b)
    else:
        bstr = str(b)
    if c >= 0:
        cstr = str("+" + c)
    else:
        cstr = str(c)
    equation = astr + "x²" + bstr + "x" + cstr

    # Print out values
    print("Equation:", equation)
    if desc == 0:
        print("Descriminant:", desc)
        print("Root:", root1)
    else:
        print("Descriminant:", desc)
        print("Root1:", root1)
        print("Root2:", root2)

# Rational Numbers #

# Calculates using fractions
def FractionCalculator(a_num, a_den, b_num, b_den, action):
    # Write the values out as fractions
    a = fractions.Fraction(a_num/a_den)
    b = fractions.Fraction(b_num/b_den)

    # Result Var
    result = 0

    # Find the resulting value
    if action == 1: #Addition
        result = ((a.numerator*b.denominator) + (b.numerator*a.denominator))/(a.denominator*b.denominator)
    elif action == 2: #Subtraction
        result = (a.numerator*b.denominator) - (b.numerator*a.denominator)/(a.denominator*b.denominator)
    elif action == 3: #Multiplication
        result = (a.numerator*b.numerator)/(a.denominator*b.denominator)
    elif action == 4: #Division
        result = (a.numerator*b.denominator)/(a.denominator*b.numerator)
    else:
        raise Exeption("Invalid action. Maybe you have a typo? :)")
    
    result = fractions.Fraction(result)
    
    # Return the result
    return result

# Fractions Simplifier
def FractionsSimplifier(a, b):
    frac = fractions.Fraction(a/b)
    return frac

# Decimal To Fraction Converter
def DecimaltoFraction(a):
    frac = fractions.Fraction(a)
    return frac

# Fraction to Decimal Converter
def FractiontoDecimal(a, b):
    decimal = a/b
    return decimal

# Geometry/Trigonometry #

# Function(sin, cos, tan) to angle
def FunctoAngle(func, val):
    result = 0
    if func == "sin":
        result = math.degrees(math.asin(float(val)))
    elif func == "cos":
        result = math.degrees(math.acos(float(val)))
    elif func == "tg":
        result = math.degrees(math.atan(float(val)))

# Triangle side Calculator w/ angle and side
def SideCalculator(angle, ang_val, side, side_val, ans):
    result = 0

    # Angle - α
    if angle == "a": # angle,side|side_needed(ans)
        if side == "c" and ans == "a": # α,c|a
            result = (math.sin(math.radians(float(ang_val))))*(float(side_val)) # sin α * c = a
        elif side == "c" and ans == "b": # α,c|b
            result = (math.cos(math.radians(float(ang_val))))*(float(side_val))) # cos α * c = b
        elif side == "a" and ans == "b": # α,a|b
            result = ((1)/(math.tan(math.radians(float(ang_val)))))*(float(side_val)) # ctg α * a = b, ctg = 1/tg
        elif side == "a" and ans == "c": # α,a|c
            result = (float(side_val))/(math.sin(math.radians(float(ang_val)))) # a / sin α = c
        elif side == "b" and ans == "a": # α,b|a
            result = (math.tan(math.radians(float(ang_val))))*(float(side_val)) # tg α * b = a
        elif side == "b" and ans == "c": # α,b|c
            result = (float(side_val))/(math.cos(math.radians(float(ang_val)))) # b / cos α = c
        else:
            raise Exception("Your sides are invalid. Maybe you made a typo? :)")
        
    # angle - β
    elif angle == "b":
        if side == "c" and ans == "a": # β,c|a
            result = (math.cos(math.radians(float(ang_val))))*(float(side_val)) # cos β * c = a
        elif side == "c" and ans == "b": # β,c|b
            result = (math.sin(math.radians(float(ang_val))))*(float(side_val)) # sin β * c = b
        elif side == "a" and ans == "c": # β,a|c
            result = (float(side_val))/(math.cos(math.radians(float(ang_val)))) # a / cos β = c
        elif side == "a" and ans == "b": # β,a|b
            result = (math.tan(math.radians(float(ang_val))))*(float(side_val)) # tg β * a = b
        elif side == "b" and ans == "a": # β,b|a
            result = ((1)/(math.sin(math.radians(float(ang_val)))))*(float(side_val)) # ctg β * b = a
        elif side == "b" and ans == "c": # β,b|c
            result = (float(side_val))/(math.sin(math.radians(float(ang_val)))) # b / sin β = c

    else:
        raise Exception("Your angle is invalid. Maybe you made a typo? :)")

    return result
    
# Area Calculators #

# Triangle area calculator
def TriangleAreaCalc(b, h):
    result = (b*h)/2
    return result

# Rectangle/Square/Parellelogram area calculator
def RectAreaCalc(w, h):
    result = w*h
    return result

# Trapezoid area calculator
def TrapezoidAreaCalc(a, b, h):
    result = ((a+b)/2)*h
    return result

# Ellipse area calculator
def EllipseAreaCalc(a, b): # π = 3.14
    result = 3.14*a*b
    return result

# Circle area calculator
def CircleAreaCalc(r):
    result = 3.14*r*r
    return result