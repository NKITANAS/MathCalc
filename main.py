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
def FunctoAngle():
    pass

# Triangle side Calculator w/ angle and side
def SideCalculator():
    pass

# Area Calculator
def AreaCalculator():
    pass