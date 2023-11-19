# Importing Hell
import fractions
import math

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# Factors a Quadratic Equation
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

print(QuadraticFactorer(a, b, c))